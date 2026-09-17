"""Semantic body measurement for text composition, separate from icon profiles.

Coordinates are stroke centerlines. A body is the outside span of the bowl,
not the empty counter. Geometry measures declared semantic regions; it cannot
reliably infer an arbitrary alphabet's baseline from its silhouette alone.
"""
from __future__ import annotations

import hashlib
import math
from ..validation.envelope import centerline_bounds
from ..renderers.svg import build_paths


def measure_glyph(icon) -> dict:
    spec = getattr(icon, 'typeface', None)
    if not spec or len(spec.get('character', '')) != 1:
        raise ValueError(f'{icon.icon_id}: missing typeface character')
    drawing = icon.draw()
    primitives = list(drawing.primitives)
    full = centerline_bounds(primitives)
    if 'body_band' in spec:
        top, baseline = spec['body_band']
        method = 'authored-body-band'
    else:
        closed = [c for c in drawing.contours if c.closed]
        if len(closed) == 1 and spec.get('kind', 'lowercase') == 'lowercase':
            members = set(closed[0].members)
            body = [p for p in primitives if p.element_id in members]
            method = 'closed-body-contour'
        else:
            # Detached zero-length primitives are dots, never the x-height.
            body = [p for p in primitives if p.start != p.end]
            method = 'main-stroke-bounds'
        _, top, _, baseline = centerline_bounds(body)
    if (not all(math.isfinite(v) for v in (top, baseline))
            or top >= baseline or top < full[1]-1e-8 or baseline > full[3]+1e-8):
        raise ValueError(f'{icon.icon_id}: invalid body band {top, baseline}')
    return {
        'icon_id': icon.icon_id, 'character': spec['character'],
        'kind': spec.get('kind', 'lowercase'), 'preferred': spec.get('preferred', True),
        'body_top': top, 'baseline': baseline, 'body_height': baseline-top,
        'bounds': list(full), 'measurement': method,
        'svg_sha256': hashlib.sha256(icon.to_svg().encode()).hexdigest(),
        'paths': [p['d'] for p in build_paths(drawing)],
    }
