"""Recognize complete circular contours for the explicit small-circle exception."""
import math
import xml.etree.ElementTree as ET

from ..model.primitives import Arc
from .envelope import arc_geometry


def circle_candidates(document, drawing=None):
    circles = []
    if drawing is not None:
        by_id = drawing.by_id()
        for contour in drawing.contours:
            members = [by_id[m] for m in contour.members]
            if not contour.closed or not members or not all(isinstance(p, Arc) for p in members):
                continue
            geometry = [arc_geometry(p) for p in members]
            first = geometry[0]
            if any(abs(g.radius_x - g.radius_y) > 1e-9
                   or abs(g.radius_x - first.radius_x) > 1e-9
                   or math.hypot(g.center_x - first.center_x, g.center_y - first.center_y) > 1e-9
                   or g.delta_angle * first.delta_angle <= 0 for g in geometry):
                continue
            if abs(abs(sum(g.delta_angle for g in geometry)) - 2 * math.pi) > 1e-9:
                continue
            if any(a.end != b.start for a, b in zip(members, members[1:] + members[:1])):
                continue
            circles.append({'element_id': contour.contour_id, 'center': [first.center_x, first.center_y],
                            'centerline_diameter': 2 * first.radius_x})
    # Also support explicit circles passed directly to the SVG measurement API.
    root = ET.fromstring(document)
    def visit(element, transformed=False):
        transformed = transformed or bool(element.get('transform'))
        if element.tag.split('}')[-1] == 'circle' and not transformed:
            circles.append({'element_id': element.get('id', 'circle'),
                            'center': [float(element.get('cx', '0')), float(element.get('cy', '0'))],
                            'centerline_diameter': 2 * float(element.get('r', '0'))})
        for child in element:
            visit(child, transformed)
    visit(root)
    return circles


def apply_circle_exceptions(holes, labels, region_ids, candidates, *, rule, samples, measuring_stroke):
    """Exempt only a whole circular region, never a fragment inside a circle.

    A core/outer disk comparison allows only raster-edge uncertainty. An extra
    line crossing a circle splits or clips the disk and therefore cannot qualify.
    """
    import numpy as np
    allowed = rule['centerline_diameters']
    tolerance = 1.5 / samples
    for hole, region_id in zip(holes, region_ids):
        if hole['status'] != 'fail':
            continue
        ys, xs = np.where(labels == region_id)
        for circle in candidates:
            diameter = circle['centerline_diameter']
            if not any(abs(diameter - size) <= 1e-9 for size in allowed):
                continue
            cx, cy = circle['center']
            radius = (diameter - measuring_stroke) / 2
            x0, x1 = max(0, int((cx - radius - tolerance) * samples)), min(labels.shape[1], math.ceil((cx + radius + tolerance) * samples))
            y0, y1 = max(0, int((cy - radius - tolerance) * samples)), min(labels.shape[0], math.ceil((cy + radius + tolerance) * samples))
            if x1 <= x0 or y1 <= y0:
                continue
            # An approved circle must be completely inside the measurement canvas.
            if cx - radius < 0 or cy - radius < 0 or cx + radius > labels.shape[1] / samples or cy + radius > labels.shape[0] / samples:
                continue
            yy, xx = np.ogrid[y0:y1, x0:x1]
            distance = ((xx + .5) / samples - cx)**2 + ((yy + .5) / samples - cy)**2
            core = distance <= (radius - tolerance)**2
            actual_distance = ((xs + .5) / samples - cx)**2 + ((ys + .5) / samples - cy)**2
            if not core.any() or not np.all(labels[y0:y1, x0:x1][core] == region_id):
                continue
            if not np.all(actual_distance <= (radius + tolerance)**2):
                continue
            hole['measured_status'] = hole['status']
            hole['status'] = 'pass'
            hole['exception'] = {'rule': rule['id'], **circle,
                                 'reason': 'User-approved 4x4 or 6x6 circular contour'}
            break
