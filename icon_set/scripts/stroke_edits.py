"""Versioned handoffs from the gallery to Python authoring tools.

These are pending edits, never published geometry. They are rows of the gallery
database's stroke_edits table (one per icon and source SVG version), each holding
the same versioned JSON document the old per-file store wrote. Consumers can check
effective validation (including a bound human override), then reconcile anchors
and relationships before adopting the graph.
"""
from contextlib import closing
from copy import deepcopy
from datetime import datetime, timezone
import hashlib
import json
import math
from pathlib import Path

if __package__:
    from . import state_db
else:
    import state_db


class EditConflict(ValueError):
    pass


GRAPH_FIELDS = ('icon_id', 'name', 'family', 'profile', 'canvas_size', 'keyshape',
                'keyshape_bounds', 'style', 'primitives', 'contours', 'anchors',
                'relationships', 'human_figures', 'composition_class', 'children',
                'semantic_role', 'semantic_kind', 'category', 'free_keyshape',
                'sizing_mode', 'canvas_width', 'canvas_height')


def grid_number(value):
    value = round(value, 6)
    return int(value) if value == int(value) else value


def stroke_groups(icon):
    """A contour moves as a whole; ungrouped primitives are individual strokes."""
    primitives = icon.get('primitives') or []
    ids = {p['element_id'] for p in primitives}
    if not primitives or any(p.get('kind') not in ('line', 'arc', 'bezier') for p in primitives):
        raise ValueError('This icon has no editable stroke geometry.')
    groups, used = [], set()
    for contour in icon.get('contours', []):
        members = contour['members']
        if not members or not set(members) <= ids or used.intersection(members):
            raise ValueError('This icon has unsupported overlapping contours.')
        groups.append({'id': 'contour:' + contour['contour_id'], 'members': members})
        used.update(members)
    groups.extend({'id': 'primitive:' + p['element_id'], 'members': [p['element_id']]}
                  for p in primitives if p['element_id'] not in used)
    return groups


def normalized_scales(icon, scales):
    groups = {g['id'] for g in stroke_groups(icon)}
    if not isinstance(scales, dict) or not set(scales) <= groups:
        raise ValueError('Unknown stroke in resize.')
    result = {}
    for key, scale in scales.items():
        if (not isinstance(scale, list) or len(scale) != 2 or
                any(type(n) not in (int, float) or not math.isfinite(n) or not .05 <= n <= 20 for n in scale)):
            raise ValueError('Stroke scale must be between 5% and 2000%.')
        if scale != [1, 1]:
            result[key] = scale
    return result


def normalized_geometry(icon, geometry):
    """Editable coordinates and cubic subdivision; profile, IDs and arc flags stay authored."""
    if geometry is None:
        return None
    original = icon['primitives']
    if not isinstance(geometry, list) or len(geometry) != len(original):
        raise ValueError('Edited geometry must keep the original strokes.')
    def number(value, positive=False):
        if type(value) not in (int, float) or not math.isfinite(value) or abs(value) > 4096 or (positive and value <= 0):
            raise ValueError('Edited coordinates must be finite and within 4096 units; radii must be positive.')
        return grid_number(value)
    def point(value):
        if not isinstance(value, list) or len(value) != 2:
            raise ValueError('Edited points must have two coordinates.')
        return [number(n) for n in value]
    result = []
    for source, candidate in zip(original, geometry):
        coordinates = {'start', 'end'} | ({'segments'} if source['kind']=='bezier' else
                                         {'radius_x', 'radius_y'} if source['kind']=='arc' else set())
        if (not isinstance(candidate, dict) or set(candidate) != set(source) or
                any(candidate[key] != value for key, value in source.items() if key not in coordinates)):
            raise ValueError('Edited geometry cannot change stroke IDs, kinds, or authored metadata.')
        primitive = deepcopy(source)
        primitive.update(start=point(candidate['start']), end=point(candidate['end']))
        if source['kind']=='bezier':
            segments = candidate['segments']
            if not isinstance(segments, list) or not 1 <= len(segments) <= max(256, len(source['segments'])*5) or any(not isinstance(segment, list) or len(segment)!=3 for segment in segments):
                raise ValueError('Edited curves must have a bounded number of cubic segments.')
            primitive['segments'] = [[point(p) for p in segment] for segment in segments]
            if primitive['segments'][-1][-1] != primitive['end']:
                raise ValueError('The last curve knot must match its endpoint.')
        elif source['kind']=='arc':
            primitive.update(radius_x=number(candidate['radius_x'], True), radius_y=number(candidate['radius_y'], True))
        result.append(primitive)
    return result


def normalized_deleted_strokes(icon, deleted):
    groups = stroke_groups(icon)
    ids = {g['id'] for g in groups}
    if (not isinstance(deleted, list) or any(not isinstance(key, str) or key not in ids for key in deleted)
            or len(set(deleted)) != len(deleted)):
        raise ValueError('Choose existing strokes to delete.')
    if len(deleted) == len(groups):
        raise ValueError('Keep at least one stroke in the icon.')
    return [g['id'] for g in groups if g['id'] in deleted]


def without_strokes(graph, groups, deleted):
    """Remove entire strokes and declarations that reference their geometry."""
    removed = {member for group in groups if group['id'] in deleted for member in group['members']}
    removed.update(c['contour_id'] for c in graph.get('contours', []) if any(m in removed for m in c['members']))
    graph['primitives'] = [p for p in graph['primitives'] if p['element_id'] not in removed]
    if 'contours' in graph:
        graph['contours'] = [c for c in graph['contours'] if c['contour_id'] not in removed]
    if 'relationships' in graph:
        graph['relationships'] = [r for r in graph['relationships'] if not any(m in removed for m in r['members'])]
    if 'human_figures' in graph:
        graph['human_figures'] = [f for f in graph['human_figures'] if f['head'] not in removed and f['torso'] not in removed]
    return graph


def edited_graph(icon, offsets, scales=None, geometry=None, deleted_strokes=None):
    groups = {g['id']: g for g in stroke_groups(icon)}
    deleted_strokes = normalized_deleted_strokes(icon, [] if deleted_strokes is None else deleted_strokes)
    if not isinstance(offsets, dict) or not set(offsets) <= groups.keys():
        raise ValueError('Unknown stroke in edit.')
    scales = normalized_scales(icon, {} if scales is None else scales)
    scale_by_member = {member: scales.get(key, [1, 1]) for key, group in groups.items() for member in group['members']}
    normalized, by_member = {}, {}
    for key, offset in offsets.items():
        if (not isinstance(offset, list) or len(offset) != 2 or
                any(type(n) not in (int, float) or not math.isfinite(n) or abs(n) > 1024 for n in offset)):
            raise ValueError('Stroke offsets must be two finite numbers between -1024 and 1024.')
        if offset != [0, 0]:
            normalized[key] = offset
            by_member.update({member: offset for member in groups[key]['members']})
    graph = {key: deepcopy(icon[key]) for key in GRAPH_FIELDS if key in icon}
    geometry = normalized_geometry(icon, geometry)
    if geometry is not None:
        graph['primitives'] = geometry
    for primitive in graph['primitives']:
        dx, dy = by_member.get(primitive['element_id'], (0, 0))
        sx, sy = scale_by_member[primitive['element_id']]
        center = icon['canvas_size'] / 2
        def move(point):
            return [grid_number(center + (point[0] - center) * sx + dx),
                    grid_number(center + (point[1] - center) * sy + dy)]
        primitive['start'] = move(primitive['start'])
        primitive['end'] = move(primitive['end'])
        if primitive['kind'] == 'bezier':
            primitive['segments'] = [[move(point) for point in segment] for segment in primitive['segments']]
        elif primitive['kind'] == 'arc':
            primitive['radius_x'] = grid_number(primitive['radius_x'] * sx)
            primitive['radius_y'] = grid_number(primitive['radius_y'] * sy)
    return normalized, without_strokes(graph, groups.values(), deleted_strokes)


def load_edit(path, *, expected_svg_sha256=None):
    """Read a local or downloaded handoff, refusing a different source version."""
    return check_edit(json.loads(Path(path).read_text(encoding='utf-8')), expected_svg_sha256=expected_svg_sha256)


def check_edit(document, *, expected_svg_sha256=None):
    if document.get('schema') not in ('pictographic.stroke-edit.v1', 'pictographic.stroke-edit.v2'):
        raise ValueError('Unsupported stroke edit schema.')
    if expected_svg_sha256 is not None and document['source_svg_sha256'] != expected_svg_sha256:
        raise EditConflict('The edit belongs to a different SVG version.')
    return document


def graph_sha256(graph):
    return hashlib.sha256(json.dumps(graph, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def effective_validation_status(document):
    """Acceptance for Python consumers; retain validation.status as machine evidence."""
    digest = graph_sha256(document['edited_graph'])
    override = document.get('validation_override') or {}
    if (override.get('graph_sha256') == digest and
            override.get('source_svg_sha256') == document.get('source_svg_sha256') and
            override.get('reviewed_by') and override.get('reviewed_at') and
            isinstance(override.get('reason'), str)):
        return 'pass'
    report = document.get('validation') or {}
    return report.get('status', 'not-run') if report.get('graph_sha256') == digest else 'not-run'


class StrokeEditStore:
    """Saved gallery edits in the stroke_edits table of `database` (the gallery SQLite file)."""

    def __init__(self, database, contracts_path=None):
        self.database = Path(database)
        self.contracts_path = Path(contracts_path) if contracts_path else None
        self.database.parent.mkdir(parents=True, exist_ok=True)
        with closing(state_db.connect(self.database)) as connection, connection:
            state_db.init_store_tables(connection)

    def connect(self):
        return closing(state_db.connect(self.database))

    def graph_for(self, icon, data, old=None):
        if data.get('svg_sha256') != icon['svg_sha256']:
            raise EditConflict('The icon changed. Reload before checking or saving edits.')
        old = old or {}
        scales = normalized_scales(icon, data.get('scales', old.get('scales', {})))
        deleted = normalized_deleted_strokes(icon, data.get('deleted_strokes', old.get('deleted_strokes', [])))
        offsets, graph = edited_graph(icon, data.get('offsets'), scales, data.get('geometry', old.get('geometry')), deleted)
        keyshape = data.get('keyshape', old.get('keyshape', icon.get('keyshape')))
        if keyshape is not None:
            if not isinstance(keyshape, str):
                raise ValueError('Choose a keyshape for this profile.')
            if keyshape == 'FREE' and icon.get('keyshape') == 'FREE':
                graph['keyshape'] = keyshape
            else:
                if self.contracts_path and self.contracts_path.is_file():
                    rules = json.loads(self.contracts_path.read_text())
                else:
                    folder = Path(__file__).resolve().parents[1] / 'model/contracts'
                    rules = {'profile': json.loads((folder / 'icon-profile.v1.json').read_text()),
                             'keyshapes': json.loads((folder / 'keyshapes.v1.json').read_text())}
                profile = icon.get('profile')
                shapes = rules['keyshapes']['resolved'].get(profile, {})
                choices = rules['profile']['profiles'].get(profile, {}).get('keyshape_choices', list(shapes))
                if keyshape not in shapes or (keyshape not in choices and keyshape != icon.get('keyshape')):
                    raise ValueError('That keyshape is not available for this profile.')
                graph['keyshape'] = keyshape
                graph['keyshape_bounds'] = shapes[keyshape]['visible_bounds']
                graph.pop('free_keyshape', None)
        return offsets, scales, graph

    def validate(self, icon, data):
        _, _, graph = self.graph_for(icon, data)
        if __package__:
            from .edit_validation import validate_graph
        else:
            from edit_validation import validate_graph
        return validate_graph(graph)

    def get(self, key, sha):
        with self.connect() as connection:
            row = connection.execute('SELECT document FROM stroke_edits WHERE icon=? AND source_svg_sha256=?',
                                     (key, sha)).fetchone()
        return check_edit(json.loads(row[0])) if row else None

    def previous_versions(self, key, sha):
        with self.connect() as connection:
            rows = connection.execute('SELECT source_svg_sha256, updated_at FROM stroke_edits '
                                      'WHERE icon=? AND source_svg_sha256<>?', (key, sha)).fetchall()
        return [{'source_svg_sha256': source, 'updated_at': at} for source, at in rows]

    def save(self, icon, data, user):
        if data.get('svg_sha256') != icon['svg_sha256']:
            raise EditConflict('The icon changed. Reload before editing this version.')
        if type(data.get('revision')) is not int or data['revision'] < 0:
            raise ValueError('A saved edit revision is required.')
        key, sha = icon['key'], icon['svg_sha256']
        # Optimistic: validate outside any lock, then write only if nobody saved in between.
        old = self.get(key, sha)
        if data['revision'] != (old['revision'] if old else 0):
            raise EditConflict('Someone saved newer edits. Download your draft, then reload saved edits.')
        # Older clients can still translate an edit without erasing its resize.
        offsets, scales, graph = self.graph_for(icon, data, old)
        geometry = normalized_geometry(icon, data.get('geometry', (old or {}).get('geometry')))
        deleted = normalized_deleted_strokes(icon, data.get('deleted_strokes', (old or {}).get('deleted_strokes', [])))
        override = (old or {}).get('validation_override')
        if override and (override.get('graph_sha256') != graph_sha256(graph) or
                         override.get('source_svg_sha256') != sha):
            override = None
        if 'validation_override' in data:
            requested = data['validation_override']
            override = None
            if requested is not None:
                reason = requested.get('reason', '') if isinstance(requested, dict) else None
                if not isinstance(reason, str) or len(reason) > 2000:
                    raise ValueError('The optional human override note must be text of at most 2000 characters.')
                override = {'reason': reason.strip(), 'reviewed_by': user,
                            'reviewed_at': datetime.now(timezone.utc).isoformat(),
                            'source_svg_sha256': sha, 'graph_sha256': graph_sha256(graph)}
        validation = {'status': 'not-run', 'note': 'Run validation on these edits before publishing.'}
        if data.get('validate') is True or override:
            validation = self.validate(icon, dict(data, scales=scales, keyshape=graph.get('keyshape'), geometry=geometry, deleted_strokes=deleted))
        document = {
            'schema': 'pictographic.stroke-edit.v2', 'icon': key,
            'source_svg_sha256': sha, 'python_source': icon.get('python_source'),
            'revision': data['revision'] + 1,
            'updated_at': datetime.now(timezone.utc).isoformat(), 'updated_by': user,
            'status': 'pending', 'offsets': offsets, 'scales': scales, 'geometry': geometry, 'deleted_strokes': deleted,
            'scale_origin': [icon['canvas_size'] / 2, icon['canvas_size'] / 2],
            'stroke_groups': stroke_groups(icon),
            'original_graph': {k: deepcopy(icon[k]) for k in GRAPH_FIELDS if k in icon},
            'edited_graph': graph,
            'validation': validation,
            'validation_override': override,
        }
        document['effective_validation_status'] = effective_validation_status(document)
        if graph.get('keyshape'):
            document['keyshape'] = graph['keyshape']
        with self.connect() as connection, connection:
            connection.execute('BEGIN IMMEDIATE')
            current = connection.execute('SELECT revision FROM stroke_edits WHERE icon=? AND source_svg_sha256=?',
                                         (key, sha)).fetchone()
            if (current[0] if current else 0) != data['revision']:
                raise EditConflict('Someone saved newer edits. Download your draft, then reload saved edits.')
            json.dumps(document, allow_nan=False)  # refuse NaN before it reaches storage
            state_db.put_stroke_edit(connection, document)
        return document
