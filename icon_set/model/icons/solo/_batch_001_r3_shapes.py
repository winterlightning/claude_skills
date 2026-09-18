"""Shared typed shapes for the batch-001 r3 solo icons (not scanned: leading underscore).

A rounded rectangle owns its edges, per-corner radii and the attachment nodes
that split an edge where another stroke joins it. Traversal is clockwise from
the top-left, so every corner arc uses ``sweep=True``.
"""
from __future__ import annotations


def rounded_rect(icon, name, left, top, right, bottom, radius=4, *,
                 corners=None, top_nodes=(), right_nodes=(), bottom_nodes=(), left_nodes=()):
    """Emit a closed rounded rectangle; return {node: [member ids touching it]}.

    ``corners`` overrides the radius as (top-left, top-right, bottom-right,
    bottom-left). A zero radius gives a square corner.
    """
    tl, tr, br, bl = corners if corners is not None else (radius,) * 4
    points = [(left + tl, top), *[(x, top) for x in sorted(top_nodes)], (right - tr, top)]
    if tr:
        points.append((right, top + tr))
    points += [*[(right, y) for y in sorted(right_nodes)], (right, bottom - br)]
    if br:
        points.append((right - br, bottom))
    points += [*[(x, bottom) for x in sorted(bottom_nodes, reverse=True)], (left + bl, bottom)]
    if bl:
        points.append((left, bottom - bl))
    points += [*[(left, y) for y in sorted(left_nodes, reverse=True)], (left, top + tl)]
    if tl:
        points.append((left + tl, top))
    # Drop duplicate consecutive points left by zero-radius corners.
    ring = [p for i, p in enumerate(points) if i == 0 or p != points[i - 1]]
    if ring[0] == ring[-1]:
        ring.pop()
    members, touching = [], {}
    for index, (start, end) in enumerate(zip(ring, ring[1:] + ring[:1])):
        member = f"{name}-{index + 1}"
        if start[0] != end[0] and start[1] != end[1]:
            radius_here = abs(end[0] - start[0])
            icon.add_arc(member, start, end, radius_x=radius_here)
        else:
            icon.add_line(member, start, end)
        members.append(member)
        touching.setdefault(start, []).append(member)
        touching.setdefault(end, []).append(member)
    icon.add_contour(name, *members, closed=True)
    return touching


def circle(icon, name, center, radius, *, split_at=None):
    """Emit a closed circle as two halves (or at a supplied pair of opposite nodes)."""
    cx, cy = center
    first, second = split_at or ((cx - radius, cy), (cx + radius, cy))
    icon.add_arc(f"{name}-a", first, second, radius_x=radius)
    icon.add_arc(f"{name}-b", second, first, radius_x=radius)
    icon.add_contour(name, f"{name}-a", f"{name}-b", closed=True)
    return (f"{name}-a", f"{name}-b")
