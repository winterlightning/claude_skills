from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'bf631264-7a4c-4e1d-a29d-1e9aa325795f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__aerial-yoga-standing-stretch/20260927T141159Z-thuan-mac-1/reference/aerial yoga basic pose_bf631264-7a4c-4e1d-a29d-1e9aa325795f.svg'
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
    icon_id = 'aerial-yoga-standing-stretch'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('aerial', 'yoga', 'standing', 'stretch')

    def build(self) -> None:
        # Aerial yoga standing stretch (reference: one long straight line from the stretched back
        # foot at the lower left up through the hip to the shoulder, the other leg standing under the
        # hip, and the arm reaching up to grip the aerial silk hanging from the ceiling at the right).
        # Shared stick-figure construction (human_ref/full_body_ref.png): r4 ring head exactly 8
        # above a short vertical neck stub; the body line (6,42)-(16,33)-(26,24) is straight.
        _circle(self, "head", 26, 10, 4)
        self.add_line("torso", (26, 22), (26, 24))
        self.add_line("torso-lean", (26, 24), (16, 33))
        self.add_line("leg-back", (16, 33), (6, 42))
        self.add_line("leg-stand", (16, 33), (22, 42))
        self.add_line("arm", (26, 24), (42, 16))
        self.add_line("silk-top", (42, 6), (42, 16))
        self.add_line("silk-tail", (42, 16), (42, 30))
        for a, b in (("torso", "torso-lean"), ("torso", "arm"), ("torso-lean", "arm"), ("torso-lean", "leg-back"),
                     ("torso-lean", "leg-stand"), ("leg-back", "leg-stand"), ("arm", "silk-top"),
                     ("arm", "silk-tail"), ("silk-top", "silk-tail")):
            self.relate("connect", a, b)
        self.mark_human_figure("person", head="head", torso="torso", torso_junction="start")
