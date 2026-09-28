from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '516ab5ea-7a01-421d-ad0d-96fc5bb3ab45'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__central-hub-with-four-nodes-516ab5ea/20260927T144116Z-thuan-mac-1/reference/coding apps website big data complexity_516ab5ea-7a01-421d-ad0d-96fc5bb3ab45.svg'
AUTHOR = 'claude-opus-5-5'


def _path(icon, name, start, steps, closed=False):
    """steps: (x, y) line | ((x, y), rx, ry, sweep[, large]) arc | ('c', c1, c2, end) cubic."""
    members, point = [], start
    for i, step in enumerate(steps):
        member = f"{name}-{i + 1}"
        if step[0] == 'c':
            icon.add_bezier(member, point, (step[1], step[2], step[3])); point = step[3]
        elif isinstance(step[0], (int, float)):
            icon.add_line(member, point, step); point = step
        else:
            end, rx, ry, sweep = step[:4]
            large = step[4] if len(step) > 4 else False
            icon.add_arc(member, point, end, radius_x=rx, radius_y=ry, sweep=sweep, large_arc=large); point = end
        members.append(member)
    icon.add_contour(name, *members, closed=closed)
    return members


def _circle(icon, name, cx, cy, r):
    """Full circle from four cardinal quarter arcs (certifiable spacing)."""
    return _path(icon, name, (cx, cy - r), [((cx + r, cy), r, r, True), ((cx, cy + r), r, r, True),
                                            ((cx - r, cy), r, r, True), ((cx, cy - r), r, r, True)], True)


def _smooth(icon, name, pts, closed=True):
    """Catmull-Rom through integer knots, as cubics (closed loop or open run)."""
    n = len(pts)
    members = []
    rng = range(n) if closed else range(n - 1)
    for i in rng:
        p1, p2 = pts[i], pts[(i + 1) % n]
        p0 = pts[i - 1] if (closed or i > 0) else p1
        p3 = pts[(i + 2) % n] if (closed or i + 2 < n) else p2
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        m = f"{name}-{i + 1}"
        icon.add_bezier(m, p1, (c1, c2, p2)); members.append(m)
    icon.add_contour(name, *members, closed=closed)
    return members


class Drawing(Solo48):
    icon_id = 'central-hub-with-four-nodes-516ab5ea'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('hub', 'network', 'nodes', 'connections', 'spokes', 'diagram', 'central')

    def build(self) -> None:
        # Hub-and-spoke network: four r5 corner nodes (reaching the SQUARE
        # extremes 6/42) and an r5 hub, joined by 45-degree spokes that run
        # between 3-4-5 lattice points of the rings. Mirrored on both axes.
        hub = [(20, 21), (28, 21), (28, 27), (20, 27)]
        _path(self, 'hub', (20, 21), [((28, 21), 5, 5, True), ((28, 27), 5, 5, True), ((20, 27), 5, 5, True), ((20, 21), 5, 5, True)], closed=True)
        nodes = [((11, 11), (14, 15)), ((37, 11), (34, 15)), ((37, 37), (34, 33)), ((11, 37), (14, 33))]
        for i, ((cx, cy), p) in enumerate(nodes):
            name = f'node-{i + 1}'
            dx, dy = p[0] - cx, p[1] - cy
            q = (cx - dx, cy - dy)
            _path(self, name, p, [(q, 5, 5, True, True), (p, 5, 5, True)], closed=True)
            self.add_line(f'spoke-{i + 1}', p, hub[i])
            self.relate('connect', name, f'spoke-{i + 1}')
            self.relate('connect', 'hub', f'spoke-{i + 1}')
