"""Exact, user-requested native closures before existing region selection.

The execution policy separately authorizes exact reviewed recipes. A close command or a
straight connector derived from specified native vertices is permitted; no
coordinates, replacement contours, translations or drawing operators are input.
"""
import copy
import hashlib
import json
import xml.etree.ElementTree as ET
from pathlib import Path

from svgpathtools import parse_path
from . import geometry as g

STYLES = ('normal', 'round', 'sharp')


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False)


def checked_spec(spec):
    if isinstance(spec, dict) and spec.get('kind') == 'endpoint_chord':
        if set(spec) != {'kind', 'endpoints'} or not isinstance(spec['endpoints'], list) or len(spec['endpoints']) != 2:
            raise ValueError('Endpoint closure requires exactly two source endpoints')
        for endpoint in spec['endpoints']:
            if (not isinstance(endpoint, dict) or set(endpoint) != {'leaf', 'subpath', 'terminal'} or
                    any(type(endpoint[k]) is not int or endpoint[k] < 0 for k in ('leaf', 'subpath')) or
                    endpoint['terminal'] not in ('start', 'end')):
                raise ValueError('Endpoint closure accepts native subpath terminals only')
        return spec
    if not isinstance(spec, dict) or type(spec.get('leaf')) is not int or spec['leaf'] < 0:
        raise ValueError('Native closure needs an explicit nonnegative leaf index')
    if spec.get('kind') == 'close_subpath':
        if set(spec) != {'leaf', 'kind', 'subpath'} or type(spec['subpath']) is not int or spec['subpath'] != 0:
            raise ValueError('Native closure supports only the complete single subpath')
    elif spec.get('kind') == 'vertex_chord':
        if set(spec) != {'leaf', 'kind', 'vertices'} or not isinstance(spec['vertices'], list) or len(spec['vertices']) != 2:
            raise ValueError('Native connector needs exactly two bound vertices')
        for vertex in spec['vertices']:
            if (not isinstance(vertex, dict) or set(vertex) != {'segment', 'terminal'} or
                    type(vertex['segment']) is not int or vertex['segment'] < 0 or vertex['terminal'] not in ('start', 'end')):
                raise ValueError('Native connector accepts source segment terminals only')
    else:
        raise ValueError('Unsupported native closure kind')
    return spec


def native_record(root, spec):
    checked_spec(spec)
    if spec['kind'] == 'endpoint_chord':
        points, commands, contexts = [], [], []
        parents = g.fu._build_parent_map(root)
        for endpoint in spec['endpoints']:
            leaf = g.leaves(root)[endpoint['leaf']]
            if g.fu._local_tag(leaf.tag) != 'path':
                raise ValueError('Endpoint closure requires source paths')
            node = leaf; clips = []
            while node is not None:
                if node.get('transform'):
                    raise ValueError('Endpoint closure does not support transformed coordinates')
                if node.get('clip-path'): clips.append(node.get('clip-path'))
                node = parents.get(node)
            path = parse_path(g.fu._replace_zero_length_arcs(leaf.get('d', ''))).continuous_subpaths()[endpoint['subpath']]
            if not len(path) or path.isclosed():
                raise ValueError('Endpoint closure requires an open source subpath')
            contexts.append((clips, *[g.fu._resolve_attr(leaf, key, parents, default) for key, default in
                [('stroke','none'),('stroke-width','1'),('stroke-linejoin','miter'),('stroke-linecap','butt'),('stroke-miterlimit','4')]]))
            points.append(getattr(path, endpoint['terminal']))
            commands.append(hashlib.sha256(leaf.get('d').encode()).hexdigest())
        if contexts[0] != contexts[1] or contexts[0][1] == 'none':
            raise ValueError('Endpoint closure requires matching native paint and clip contexts')
        if abs(points[0]-points[1]) <= 1e-9:
            raise ValueError('Endpoint closure connector is empty')
        return dict(spec, native_d_sha256=commands, connector=[[p.real,p.imag] for p in points])
    leaf = g.leaves(root)[spec['leaf']]
    if g.fu._local_tag(leaf.tag) != 'path':
        raise ValueError('Native closure requires an original path')
    parents = g.fu._build_parent_map(root)
    node = leaf
    while node is not None:
        if node.get('transform'):
            raise ValueError('Native closure does not support transformed coordinates')
        node = parents.get(node)
    path = parse_path(g.fu._replace_zero_length_arcs(leaf.get('d', '')))
    if len(path.continuous_subpaths()) != 1 or not len(path) or path.isclosed():
        raise ValueError('Native closure requires the bound single open subpath')
    if spec['kind'] == 'close_subpath':
        a, b = path.end, path.start
    else:
        a, b = [getattr(path[v['segment']], v['terminal']) for v in spec['vertices']]
    if abs(a-b) <= 1e-9:
        raise ValueError('Native closure connector is empty')
    return dict(spec, native_d_sha256=hashlib.sha256(leaf.get('d').encode()).hexdigest(),
                connector=[[a.real, a.imag], [b.real, b.imag]])


def bind(recipe, source_dir, specs=None):
    """Recompute source coordinates from hash-bound selectors, never proposed points.

    ``specs`` is only a recipe-authoring convenience; execution extracts selectors
    from the saved binding and compares every field against this recomputation.
    Exact-icon/user authorization is enforced separately by execution policy.
    """
    name = recipe.get('name')
    supported = recipe.get('schema') == 'source-object-treatments/v1' or (recipe.get('schema') == 'normal-region-decisions/v1' and recipe.get('mode') == 'regions')
    if not supported or not isinstance(name, str) or '/' in name or '\\' in name:
        raise ValueError('Native closure requires a named object-treatment recipe')
    if set(recipe.get('sources', {})) != set(STYLES):
        raise ValueError('Native closure requires all three bound style sources')
    source_dir = Path(source_dir).resolve()
    schema = 'bound-native-closures/v2' if specs is not None and any(isinstance(v, list) for v in specs.values()) else 'bound-native-closures/v1'
    if specs is None:
        saved = recipe.get('native_closures')
        if not isinstance(saved, dict) or set(saved) != {'schema', 'styles'} or saved['schema'] not in ('bound-native-closures/v1','bound-native-closures/v2') or not isinstance(saved['styles'], dict) or set(saved['styles']) != set(STYLES):
            raise ValueError('Native closure requires a complete saved binding')
        schema = saved['schema']
        specs = {}
        for style, record in saved['styles'].items():
            if not isinstance(record, dict) or set(record) != {'source_sha256', 'closures'} or not isinstance(record['closures'], list) or not record['closures'] or (schema.endswith('/v1') and len(record['closures']) != 1):
                raise ValueError('Explicit native closure list is missing or invalid')
            specs[style] = []
            for closure in record['closures']:
                if not isinstance(closure, dict) or not {'native_d_sha256', 'connector'} <= set(closure):
                    raise ValueError('Native closure requires command and endpoint bindings')
                specs[style].append(checked_spec({k: v for k, v in closure.items() if k not in ('native_d_sha256', 'connector')}))
    if not isinstance(specs, dict) or set(specs) != set(STYLES):
        raise ValueError('Native closure specs need all three styles')
    records = {}
    for style in STYLES:
        expected = recipe['sources'][style]
        if not isinstance(expected, dict) or set(expected) != {'file', 'sha256'}:
            raise ValueError('Native closure requires an exact bound source record')
        if expected['file'] != f'{style}/{name}.svg':
            # Normal remains the original decision master. Styled inputs may
            # use an existing, separately accepted source derivation only when
            # the established manifest/hash/provenance guard validates it now.
            # Raw styled originals remain valid (e.g. the explicit knight case).
            if style == 'normal':
                raise ValueError('Native closure requires the original Normal source')
            from ..workflow import recipes as recipes_api
            approved = recipes_api.sources(source_dir, name).get(style)
            if canonical(expected) != canonical(approved):
                raise ValueError('Native closure styled derivation lacks accepted provenance')
            recipes_api.source(recipe, source_dir, style)
        path = source_dir/expected['file']
        if not path.resolve().is_relative_to(source_dir) or g.sha(path) != expected['sha256']:
            raise ValueError('Native closure source bytes changed')
        root = ET.parse(path).getroot()
        operations = specs[style] if isinstance(specs[style], list) else [specs[style]]
        if not operations: raise ValueError('Explicit native closure list cannot be empty')
        closures = [native_record(root, spec) for spec in operations]
        keys = [canonical(sorted(record['connector'])) for record in closures]
        if len(set(keys)) != len(keys): raise ValueError('Duplicate native closure connector')
        records[style] = {'source_sha256': expected['sha256'], 'closures': closures}
    return {'schema': schema, 'styles': records}


def validate(recipe, source_dir):
    actual = bind(recipe, source_dir)
    if canonical(recipe.get('native_closures')) != canonical(actual):
        raise ValueError('Native closure binding is missing, changed or contains extra fields')
    return actual


def apply(root, recipe, source_dir, style):
    binding = validate(recipe, source_dir)
    result = copy.deepcopy(root)
    # Keep original leaf references: inserting a connector inside one group must
    # not renumber a later source selector during this same replay.
    items = g.leaves(result)
    parents = g.fu._build_parent_map(result)
    for record in binding['styles'][style]['closures']:
        spec = {k: v for k, v in record.items() if k not in ('native_d_sha256', 'connector')}
        if canonical(native_record(root, spec)) != canonical(record):
            raise ValueError('Native closure working geometry no longer matches its binding')
        index = spec['endpoints'][0]['leaf'] if spec['kind'] == 'endpoint_chord' else spec['leaf']
        leaf = items[index]
        if spec['kind'] == 'close_subpath':
            leaf.set('d', leaf.get('d')+' Z')
        else:
            a, b = record['connector']
            connector = copy.deepcopy(leaf)
            connector.attrib.pop('id', None)
            connector.set('d', f'M{a[0]} {a[1]}L{b[0]} {b[1]}')
            if spec['kind'] == 'endpoint_chord': connector.set('fill', 'none')
            parents[leaf].append(connector)
    return result, binding['styles'][style]
