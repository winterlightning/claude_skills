"""Bounded path movement/resizing proposals for failed SOLO48 drafts.

No features, relationships, contours or validation rules are removed. Accepted
steps reduce measured failures. This is a numeric repair search, not approval.
"""
from copy import copy
from dataclasses import replace

from .primitives import Arc, Line, Point
from ..renderers.svg import build_paths
from ..validation.envelope import centerline_bounds
from ..validation.library_qa import inspect_icon, measure_spacing


def visible_hole_count(document, canvas=48):
    """Count visible openings at the authored stroke, independently of QA's
    measuring stroke. Reject repairs that turn existing rings into solid dots.
    Quarter-unit-area specks are excluded from this visual preservation guard.
    """
    import io
    import cairosvg
    import cv2
    import numpy as np
    from PIL import Image
    scale=8
    png=cairosvg.svg2png(bytestring=document.encode(),output_width=canvas*scale,output_height=canvas*scale)
    alpha=np.array(Image.open(io.BytesIO(png)).convert('RGBA'))[:,:,3]
    n,labels,stats,_=cv2.connectedComponentsWithStats((alpha<128).astype('uint8'),connectivity=8)
    outside=set(labels[0])|set(labels[-1])|set(labels[:,0])|set(labels[:,-1])
    return int(sum(i not in outside and stats[i,cv2.CC_STAT_AREA]>=scale*scale/4 for i in range(1,n)))


def preserves_visible_rings(original, candidate):
    """Preserve holes in existing circular features, independently of accidental
    ink contacts between separate paths that a spacing repair may resolve.
    """
    from ..validation.circle_exceptions import circle_candidates
    paths={p['id']:{s.element_id for s in p['primitives']} for p in build_paths(original.draw())}
    for circle in circle_candidates('<svg/>',original.draw()):
        if circle['centerline_diameter'] <= original.STROKE_WIDTH:
            continue
        members=paths[circle['element_id']]
        isolated=copy(candidate)
        isolated.primitives=[p for p in candidate.primitives if p.element_id in members]
        isolated.contours=[c for c in candidate.contours if set(c.members)<=members]
        if visible_hole_count(isolated.to_svg()) == 0:
            return False
    return True


def transform_paths(icon, members, *, sx=1, sy=1, dx=0, dy=0, radii=None):
    """Transform selected primitives; propagate shared vertices to every path."""
    selected = [p for p in icon.primitives if p.element_id in members]
    bounds = centerline_bounds(selected)
    cx, cy = (bounds[0] + bounds[2]) / 2, (bounds[1] + bounds[3]) / 2
    points = {point: Point(round(cx + (point.x-cx)*sx + dx), round(cy + (point.y-cy)*sy + dy))
              for p in selected for point in (p.start, p.end)}
    all_points = {point for p in icon.primitives for point in (p.start, p.end)}
    if len({points.get(point, point) for point in all_points}) != len(all_points):
        raise ValueError('movement would merge distinct vertices')
    result = copy(icon)
    result.primitives = []
    for p in icon.primitives:
        updates = {'start': points.get(p.start, p.start), 'end': points.get(p.end, p.end)}
        if isinstance(p, Arc) and p.element_id in members:
            rx, ry = radii if radii is not None else (round(p.radius_x*sx), round(p.radius_y*sy))
            if min(rx, ry) < 1:
                raise ValueError('arc radius would collapse')
            updates.update(radius_x=rx, radius_y=ry)
        result.primitives.append(replace(p, **updates))
    result.anchors = {name: points.get(point, point) if name != 'center' else point
                      for name, point in icon.anchors.items()}
    return result


def _score(report):
    score = 0.0
    for finding in report.findings:
        if finding.check not in ('mic', 'canvas/keyshape bounds'):
            return 1e6
        d = finding.detail
        if 'painted' in d and 'target' in d:
            score += 10 + 3*sum(abs(a-b) for a, b in zip(d['painted'], d['target']))
        elif finding.check == 'mic':
            distance = d.get('centerline_distance', d.get('lowerBound', 0))
            required = d.get('required_centerline_distance', d.get('requiredCenterline', 8))
            score += 10 + max(0, required-distance)*2
        else:
            score += 100
    return score


def _partition(qa):
    return sorted(tuple(sorted(c['elementIds'])) for c in qa.get('components', []))


def _displacement(original, candidate):
    values = []
    for a, b in zip(original.primitives, candidate.primitives):
        values.extend(abs(x-y) for p, q in ((a.start,b.start),(a.end,b.end))
                      for x,y in zip(p.as_tuple(), q.as_tuple()))
        if isinstance(a, Arc):
            values.extend((abs(a.radius_x-b.radius_x), abs(a.radius_y-b.radius_y)))
    return max(values, default=0), sum(values)


def _preserves_straight_edges(original, candidate):
    """Do not evade parallel clearance by introducing a tiny slant at a join."""
    old = {p.element_id:p for p in original.primitives}
    new = {p.element_id:p for p in candidate.primitives}
    for name, p in old.items():
        if isinstance(p, Line) and not p.is_dot:
            q = new[name]
            if p.start.x == p.end.x and q.start.x != q.end.x:
                return False
            if p.start.y == p.end.y and q.start.y != q.end.y:
                return False
    for contour in original.contours:
        lines = [old[name] for name in contour.members if isinstance(old[name],Line) and not old[name].is_dot]
        for i,p in enumerate(lines):
            for q in lines[i+1:]:
                ax,ay=p.end.x-p.start.x,p.end.y-p.start.y
                bx,by=q.end.x-q.start.x,q.end.y-q.start.y
                if ax*by != ay*bx:
                    continue
                a,b=new[p.element_id],new[q.element_id]
                if (a.end.x-a.start.x)*(b.end.y-b.start.y) != (a.end.y-a.start.y)*(b.end.x-b.start.x):
                    return False
    return True


def _proposals(icon, report):
    paths = {p['id']: {s.element_id for s in p['primitives']} for p in build_paths(icon.draw())}
    singles = {p.element_id: {p.element_id} for p in icon.primitives}
    def radius_proposals(p):
        for delta in (1,-1,2,-2):
            for rx,ry in ((p.radius_x+delta,p.radius_y+delta),
                          (p.radius_x+delta,p.radius_y), (p.radius_x,p.radius_y+delta)):
                if min(rx,ry)>0:
                    yield p.element_id, {p.element_id}, {'radii':(rx,ry)}
    boundary_arcs = set()
    if any(f.check == 'canvas/keyshape bounds' for f in report.findings):
        box = centerline_bounds(icon.primitives)
        for p in icon.primitives:
            if isinstance(p, Arc):
                bounds = centerline_bounds([p])
                if any(abs(a-b)<1e-7 for a,b in zip(box,bounds)):
                    boundary_arcs.add(p.element_id)
                    yield from radius_proposals(p)
    targets = []
    for f in report.findings:
        detail = f.detail
        targets.extend(detail.get('elements', []))
        targets.extend(str(s).split(':subpath-')[0] for s in detail.get('closestContours', []))
        if f.element_id:
            targets.append(f.element_id)
    # Also consider each existing path, so hole-only failures have repair options.
    targets.extend(paths)
    targets = list(dict.fromkeys(targets))
    for name in targets:
        members = paths.get(name, singles.get(name))
        if not members:
            continue
        selected = [p for p in icon.primitives if p.element_id in members]
        left, top, right, bottom = centerline_bounds(selected)
        w, h = right-left, bottom-top
        # Local shifts preserve shape. Resizing gives space to inner details or
        # enlarges narrow openings. Work on integer changes in bbox dimensions.
        for step in (1, 2, 3):
            for dx,dy in ((step,0),(-step,0),(0,step),(0,-step)):
                yield name, members, {'dx':dx,'dy':dy}
        for delta in (-2, 2, -4, 4):
            sx = (w+delta)/w if w else 1
            sy = (h+delta)/h if h else 1
            if sx > .4 and sy > .4:
                yield name, members, {'sx':sx,'sy':sy}
            if w and sx > .4:
                yield name, members, {'sx':sx}
            if h and sy > .4:
                yield name, members, {'sy':sy}
    # Arc snapping can move an extremum off the keyshape. Radius repairs are
    # evaluated using the exact SVG arc geometry, never by patching the SVG.
    for p in icon.primitives:
        if isinstance(p, Arc) and p.element_id not in boundary_arcs:
            yield from radius_proposals(p)


def repair_paths(icon, *, max_evaluations=600, max_steps=8, max_displacement=6):
    """Return the best locally repaired draft, full QA, and an audit trail.

    Shared endpoint topology, centerline component membership, and hole count
    are preserved. At most six units of coordinate/radius displacement from
    the starting draft are allowed. A bounded search may leave failures.
    """
    original = icon
    best = icon
    report = icon.validate_icon()
    qa = inspect_icon(icon, validation=report)
    baseline_partition = _partition(qa['spacing'])
    baseline_holes = qa.get('negative_space', {}).get('hole_count')
    best_score = _score(report)
    attempts, steps, rejected = 0, [], 0
    seen = {tuple(icon.primitives)}

    def hole_score(row):
        ns = row.get('negative_space', {})
        return 10*ns.get('failed_hole_count', 0) + 10*ns.get('pinch_count', 0) + sum(
            max(0,h.get('minimum_radius_design_u',0)-h.get('inscribed_radius_design_u',0))
            for h in ns.get('holes',[]) if h.get('status') == 'fail')

    for _ in range(max_steps):
        if qa['status'] == 'pass':
            break
        winning = None
        objective = best_score + hole_score(qa)
        round_limit = min(max_evaluations, attempts + 180)
        # Each round evaluates targeted moves from the same incumbent.
        for name, members, kwargs in _proposals(best, report):
            if attempts >= round_limit:
                break
            try:
                candidate = transform_paths(best, members, **kwargs)
                signature = tuple(candidate.primitives)
                if signature in seen:
                    continue
                seen.add(signature)
                displacement, total_move = _displacement(original, candidate)
                if displacement > max_displacement:
                    continue
                if not _preserves_straight_edges(original, candidate):
                    rejected += 1
                    continue
                attempts += 1
                candidate_report = candidate.validate_icon()
                vector_score = _score(candidate_report)
                # Preserve or improve vector checks before paying for raster QA.
                if vector_score > best_score + 1e-7:
                    continue
                if vector_score >= best_score - .05 and not hole_score(qa):
                    continue
                # Raster failures cannot have a negative cost. Skip candidates
                # that cannot beat the best already checked in this round.
                if winning is not None and vector_score >= winning[0][0] - .05:
                    continue
                spacing = measure_spacing(candidate, candidate.draw(), candidate_report)
                if _partition(spacing) != baseline_partition:
                    rejected += 1
                    continue
                candidate_qa = inspect_icon(candidate, validation=candidate_report)
                if candidate_qa['status'] == 'error':
                    continue
                if candidate_qa.get('negative_space',{}).get('hole_count') != baseline_holes:
                    rejected += 1
                    continue
                if not preserves_visible_rings(original,candidate):
                    rejected += 1
                    continue
                score = vector_score + hole_score(candidate_qa)
                rank = (score, total_move)
                if score < objective - .05 and (winning is None or rank < winning[0]):
                    winning = (rank, candidate, candidate_report, candidate_qa, vector_score,
                               {'path':name, 'operation':kwargs, 'before_score':objective, 'after_score':score})
                    if candidate_qa['status'] == 'pass':
                        break
            except (ValueError, ZeroDivisionError, OverflowError):
                continue
        if winning is None:
            break
        _, best, report, qa, best_score, change = winning
        steps.append(change)
    qa.pop('_svg', None)
    return best, qa, {'evaluations':attempts, 'changes':steps, 'topology_rejections':rejected,
                      'max_displacement':max_displacement,
                      'remaining_status':qa['status'], 'requires_visual_review':True}
