from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'a8e7d502-fe5d-4522-a86c-a96b575ac081'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__opened-spiky-durian/20260927T084830Z-thuan-mac-1/reference/durian peeled_a8e7d502-fe5d-4522-a86c-a96b575ac081.svg'
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


class Drawing(Solo48):
    icon_id = 'opened-spiky-durian'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('opened', 'spiky', 'durian')

    def build(self) -> None:
        # opened durian (reference): spiky husk split along the diagonal, the rounded oval flesh
        # pod lying in the split with its ends on the husk. Before drew a gear-like octagon with a
        # ring, which read as a cog.
        tips = [(44, 24), (40, 36), (24, 44), (4, 24), (12, 8), (24, 4)]
        valleys = [(38, 29), (31, 37), (16, 32), (11, 17), (19, 10), (32, 16)]
        pts = []
        for t, v in zip(tips, valleys):
            pts += [t, v]
        _path(self, "husk", pts[0], pts[1:] + [pts[0]], True)
        # pod: ellipse on the x+y=48 diagonal, ends on the husk valleys (16,32) and (32,16)
        k = 0.5523
        e1, s1, e2, s2, m = (16, 32), (21, 21), (32, 16), (27, 27), (24, 24)
        def q(p0, p1):
            c1 = (round(p0[0] + k * (p1[0] - m[0]), 3), round(p0[1] + k * (p1[1] - m[1]), 3))
            c2 = (round(p1[0] + k * (p0[0] - m[0]), 3), round(p1[1] + k * (p0[1] - m[1]), 3))
            return ('c', c1, c2, p1)
        _path(self, "pod", e1, [q(e1, s1), q(s1, e2), q(e2, s2), q(s2, e1)], True)
        self.relate("connect", "pod", "husk")
