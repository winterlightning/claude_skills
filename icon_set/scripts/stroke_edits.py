"""Versioned, atomic JSON handoffs from the gallery to Python authoring tools.

These are pending edits, never published geometry. A consumer must validate the
edited graph and reconcile its anchors/relationships before adopting it.
"""
from contextlib import contextmanager
from copy import deepcopy
from datetime import datetime, timezone
import fcntl
import hashlib
import json
import math
import os
from pathlib import Path
import tempfile


class EditConflict(ValueError):
    pass


GRAPH_FIELDS = ('icon_id', 'name', 'family', 'profile', 'canvas_size', 'keyshape',
                'keyshape_bounds', 'style', 'primitives', 'contours', 'anchors',
                'relationships', 'human_figures', 'composition_class', 'children',
                'semantic_role', 'semantic_kind', 'category', 'free_keyshape')


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


def edited_graph(icon, offsets, scales=None):
    groups = {g['id']: g for g in stroke_groups(icon)}
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
    return normalized, graph


def load_edit(path, *, expected_svg_sha256=None):
    """Read a local or downloaded handoff, refusing a different source version."""
    document = json.loads(Path(path).read_text(encoding='utf-8'))
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
            isinstance(override.get('reason'), str) and override['reason'].strip()):
        return 'pass'
    report = document.get('validation') or {}
    return report.get('status', 'not-run') if report.get('graph_sha256') == digest else 'not-run'


class StrokeEditStore:
    def __init__(self, root, contracts_path=None):
        self.root = Path(root)
        self.contracts_path = Path(contracts_path) if contracts_path else None

    def graph_for(self, icon, data, old=None):
        if data.get('svg_sha256') != icon['svg_sha256']:
            raise EditConflict('The icon changed. Reload before checking or saving edits.')
        old = old or {}
        scales = normalized_scales(icon, data.get('scales', old.get('scales', {})))
        offsets, graph = edited_graph(icon, data.get('offsets'), scales)
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

    def folder(self, key):
        return self.root / hashlib.sha256(key.encode()).hexdigest()

    def path(self, key, sha):
        return self.folder(key) / (hashlib.sha256(sha.encode()).hexdigest() + '.json')

    @contextmanager
    def locked(self, key):
        folder = self.folder(key)
        folder.mkdir(parents=True, exist_ok=True)
        with (folder / '.lock').open('a') as lock:
            fcntl.flock(lock, fcntl.LOCK_EX)
            try:
                yield
            finally:
                fcntl.flock(lock, fcntl.LOCK_UN)

    def get(self, key, sha):
        path = self.path(key, sha)
        return load_edit(path) if path.is_file() else None

    def previous_versions(self, key, sha):
        rows = [load_edit(path) for path in self.folder(key).glob('*.json')]
        return [{'source_svg_sha256': row['source_svg_sha256'], 'updated_at': row['updated_at']}
                for row in rows if row['source_svg_sha256'] != sha]

    def save(self, icon, data, user):
        if data.get('svg_sha256') != icon['svg_sha256']:
            raise EditConflict('The icon changed. Reload before editing this version.')
        if type(data.get('revision')) is not int or data['revision'] < 0:
            raise ValueError('A saved edit revision is required.')
        key, sha = icon['key'], icon['svg_sha256']
        with self.locked(key):
            old = self.get(key, sha)
            if data['revision'] != (old['revision'] if old else 0):
                raise EditConflict('Someone saved newer edits. Download your draft, then reload saved edits.')
            # Older clients can still translate an edit without erasing its resize.
            offsets, scales, graph = self.graph_for(icon, data, old)
            override = (old or {}).get('validation_override')
            if override and (override.get('graph_sha256') != graph_sha256(graph) or
                             override.get('source_svg_sha256') != sha):
                override = None
            if 'validation_override' in data:
                requested = data['validation_override']
                override = None
                if requested is not None:
                    reason = requested.get('reason') if isinstance(requested, dict) else None
                    if not isinstance(reason, str) or not reason.strip() or len(reason) > 2000:
                        raise ValueError('Enter a human override reason (1–2000 characters).')
                    override = {'reason': reason.strip(), 'reviewed_by': user,
                                'reviewed_at': datetime.now(timezone.utc).isoformat(),
                                'source_svg_sha256': sha, 'graph_sha256': graph_sha256(graph)}
            validation = {'status': 'not-run', 'note': 'Run validation on these edits before publishing.'}
            if data.get('validate') is True or override:
                validation = self.validate(icon, dict(data, scales=scales, keyshape=graph.get('keyshape')))
            document = {
                'schema': 'pictographic.stroke-edit.v2', 'icon': key,
                'source_svg_sha256': sha, 'python_source': icon.get('python_source'),
                'revision': data['revision'] + 1,
                'updated_at': datetime.now(timezone.utc).isoformat(), 'updated_by': user,
                'status': 'pending', 'offsets': offsets, 'scales': scales,
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
            path = self.path(key, sha)
            temp = None
            try:
                with tempfile.NamedTemporaryFile(mode='w', dir=path.parent, suffix='.tmp',
                                                 encoding='utf-8', delete=False) as stream:
                    temp = Path(stream.name)
                    json.dump(document, stream, ensure_ascii=False, indent=2, allow_nan=False)
                    stream.write('\n')
                    stream.flush()
                    os.fsync(stream.fileno())
                os.replace(temp, path)
            finally:
                if temp and temp.exists():
                    temp.unlink()
        return document
