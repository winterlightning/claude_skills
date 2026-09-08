"""Validate input structure before any renderer or geometry calculation runs.

Metadata constraints are read from the published record schema. Geometry grid
and style rules remain in their dedicated check so numeric drafts still receive
useful bounds diagnostics.
"""
from functools import lru_cache
import json
import math
from pathlib import Path
import re

from ..model.keyshapes import FreeKeyshapeSpec
from ..model.primitives import Arc, Line, Point, Contour, Relationship, ResolvedDrawing


@lru_cache(maxsize=1)
def _properties():
    path = Path(__file__).resolve().parents[1] / 'schemas/icon-record.schema.json'
    return json.loads(path.read_text(encoding='utf-8'))['properties']


def check_structure(icon, drawing) -> list[str]:
    errors = []
    properties = _properties()
    for field in ('icon_id', 'category', 'semantic_kind', 'composition_class'):
        value = getattr(icon, field)
        spec = properties[field]
        if not isinstance(value, str) or not value:
            errors.append(f'{field} must be a non-empty string')
        elif 'pattern' in spec and re.fullmatch(spec['pattern'], value) is None:
            errors.append(f'{field} must follow the naming pattern {spec["pattern"]!r}')
        elif 'enum' in spec and value not in spec['enum']:
            errors.append(f'{field} must be one of {spec["enum"]!r}')
    for field in ('aliases', 'keywords'):
        value = getattr(icon, field)
        if not isinstance(value, (list, tuple)) or any(not isinstance(v, str) for v in value):
            errors.append(f'{field} must be a sequence of strings')
    if icon.family is not None and not isinstance(icon.family, str):
        errors.append('family must be a string or None for a draft')
    if icon.semantic_role not in ('MAIN', 'SUB', None):
        errors.append('semantic_role must be MAIN, SUB or None')
    if icon.free_keyshape is not None and not isinstance(icon.free_keyshape, FreeKeyshapeSpec):
        errors.append('free_keyshape must be a FreeKeyshapeSpec')
    if not isinstance(drawing, ResolvedDrawing):
        return errors + ['draw() must return a ResolvedDrawing']

    def identifier(value, label):
        if not isinstance(value, str) or not value:
            errors.append(f'{label} must be a non-empty string')
            return False
        return True

    def point(value, label, *, integer=False):
        if not isinstance(value, Point):
            errors.append(f'{label} must be a Point')
            return
        for coordinate in value.as_tuple():
            if (isinstance(coordinate, bool) or not isinstance(coordinate, (int, float))
                    or not math.isfinite(coordinate)
                    or (integer and not isinstance(coordinate, int))):
                errors.append(f'{label} must contain finite {"integer" if integer else "numeric"} coordinates')
                break

    ids = set()
    for primitive in drawing.primitives:
        if not isinstance(primitive, (Line, Arc)):
            errors.append(f'unsupported primitive type {type(primitive).__name__}')
            continue
        if identifier(primitive.element_id, 'element_id'):
            ids.add(primitive.element_id)
        point(primitive.start, f'{primitive.element_id}.start')
        point(primitive.end, f'{primitive.element_id}.end')
        if isinstance(primitive, Arc):
            for field in ('radius_x', 'radius_y'):
                value = getattr(primitive, field)
                if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
                    errors.append(f'{primitive.element_id}.{field} must be finite and numeric')
            for field in ('large_arc', 'sweep'):
                if not isinstance(getattr(primitive, field), bool):
                    errors.append(f'{primitive.element_id}.{field} must be a boolean')
    for contour in drawing.contours:
        if not isinstance(contour, Contour):
            errors.append('contours must contain Contour objects')
            continue
        if identifier(contour.contour_id, 'contour_id'):
            ids.add(contour.contour_id)
        if not isinstance(contour.closed, bool):
            errors.append('contour.closed must be a boolean')
        if not isinstance(contour.members, (tuple, list)) or not contour.members:
            errors.append('contour.members must be a non-empty sequence')
        else:
            for member in contour.members:
                identifier(member, 'contour member')
    for name, anchor in drawing.anchors:
        identifier(name, 'anchor name')
        point(anchor, f'anchor {name}', integer=True)
    for relation in drawing.relationships:
        if not isinstance(relation, Relationship):
            errors.append('relationships must contain Relationship objects')
            continue
        if relation.kind not in ('connect', 'occlude', 'knockout'):
            errors.append(f'unknown relationship kind {relation.kind!r}')
        if not isinstance(relation.members, (tuple, list)) or not relation.members:
            errors.append('relationship.members must be a non-empty sequence')
        else:
            for member in relation.members:
                if identifier(member, 'relationship member') and member not in ids:
                    errors.append(f'relationship references unknown element {member!r}')
    return errors
