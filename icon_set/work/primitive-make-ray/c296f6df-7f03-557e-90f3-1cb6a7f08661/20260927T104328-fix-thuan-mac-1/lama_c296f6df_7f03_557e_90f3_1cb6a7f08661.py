from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'c296f6df-7f03-557e-90f3-1cb6a7f08661'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__llama/20260927T104205Z-thuan-mac-1/reference/lama_c296f6df-7f03-557e-90f3-1cb6a7f08661.svg'
AUTHOR = "claude-opus-5-5"


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
    icon_id = 'llama'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'animals'
    categories = ('animals', 'primitives')
    aliases = ()
    keywords = ('llama', 'alpaca', 'standing', 'andes', 'animal', 'wool', 'farm', 'south america')

    def build(self) -> None:
        # Plan (reference): a llama in side view facing left. One closed
        # silhouette: a tall pointed ear on top (tip on y=6), a small head with a
        # long rounded muzzle reaching x=6, a long upright neck (walls x=12/20,
        # 8 apart), a level back, a rounded rump reaching x=42 and a flat belly;
        # a front and a back leg drop from the belly to the floor on y=42.
        _path(self, "body", (17, 6), [(20, 12), (20, 22), (37, 22),
                                      ('c', (40, 22), (42, 25), (42, 28)),
                                      ('c', (42, 32), (40, 34), (37, 34)),
                                      (15, 34),
                                      ('c', (13, 34), (12, 32), (12, 30)),
                                      (12, 20),
                                      ('c', (9, 20), (6, 19), (6, 16)),
                                      ('c', (6, 13), (9, 12), (13, 11)),
                                      (17, 6)], True)
        self.add_line("leg-front", (15, 34), (15, 42))
        self.add_line("leg-back", (37, 34), (37, 42))
        self.relate("connect", "leg-front", "body")
        self.relate("connect", "leg-back", "body")
