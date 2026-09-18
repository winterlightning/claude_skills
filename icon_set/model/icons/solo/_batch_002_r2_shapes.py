"""Shared typed shapes for the batch-002 r2 SOLO48 icons.

Each helper emits one logical shape as a single contour so its joins paint as
round joins. Straight edges can be split at named attachment nodes, which
lets a divider or handle share an exact endpoint with the receiving edge.
"""
SOURCE_ICON_ID = None
SOURCE_PATH = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-002'
AUTHOR = 'claude-opus-5'


def path(icon, name, start, *steps, closed=False):
    """Emit a run of steps as one contour.

    Steps are ``('L', end)``, ``('A', end, rx, ry, sweep[, large])`` or
    ``('C', c1, c2, end)``. Members are named ``<name>-<index>``.
    """
    point, members = start, []
    for index, step in enumerate(steps):
        ident = f'{name}-{index}'
        kind, end = step[0], step[-1] if step[0] == 'C' else step[1]
        if kind == 'L':
            icon.add_line(ident, point, end)
        elif kind == 'A':
            _, end, rx, ry, sweep, *large = step
            icon.add_arc(ident, point, end, radius_x=rx, radius_y=ry,
                         sweep=sweep, large_arc=bool(large and large[0]))
        elif kind == 'C':
            _, c1, c2, end = step
            icon.add_bezier(ident, point, (c1, c2, end))
        else:
            raise ValueError(f'{name}: unknown step {kind!r}')
        members.append(ident)
        point = end
    icon.add_contour(name, *members, closed=closed)
    return members


def _split(a, b, nodes):
    """Straight run a->b cut at every node lying strictly inside it, in order."""
    dx, dy = b[0] - a[0], b[1] - a[1]
    length = dx * dx + dy * dy
    inside = [p for p in nodes
              if (p[0] - a[0]) * dy == (p[1] - a[1]) * dx
              and 0 < (p[0] - a[0]) * dx + (p[1] - a[1]) * dy < length]
    inside.sort(key=lambda p: (p[0] - a[0]) * dx + (p[1] - a[1]) * dy)
    return [('L', p) for p in inside] + [('L', b)]


def rounded_rect(icon, name, left, top, right, bottom, radius, nodes=()):
    """Closed rounded rectangle, clockwise from the top-left tangent point.

    ``radius`` 0 gives square corners (round stroke joins). ``nodes`` are
    attachment points on the straight edges; each splits its edge. An edge
    whose length the corners use up (a capsule side) is omitted.
    """
    r = radius
    steps = []
    corners = [
        ((left + r, top), (right - r, top), (right, top + r)),
        ((right, top + r), (right, bottom - r), (right - r, bottom)),
        ((right - r, bottom), (left + r, bottom), (left, bottom - r)),
        ((left, bottom - r), (left, top + r), (left + r, top)),
    ]
    for start, edge_end, corner_end in corners:
        if start != edge_end:
            steps += _split(start, edge_end, nodes)
        if r:
            steps.append(('A', corner_end, r, r, True))
    return path(icon, name, (left + r, top), *steps, closed=True)


def polyline(icon, name, *points, nodes=(), closed=False):
    """Open or closed straight run, split at ``nodes`` lying on its edges."""
    seq = list(points) + ([points[0]] if closed else [])
    steps = []
    for a, b in zip(seq, seq[1:]):
        steps += _split(a, b, nodes)
    return path(icon, name, seq[0], *steps, closed=closed)


def circle(icon, name, cx, cy, r):
    """Circle as two semicircles; the top and bottom are drawn endpoints."""
    icon.add_arc(f'{name}-right', (cx, cy - r), (cx, cy + r), radius_x=r)
    icon.add_arc(f'{name}-left', (cx, cy + r), (cx, cy - r), radius_x=r)
    icon.add_contour(name, f'{name}-right', f'{name}-left', closed=True)
