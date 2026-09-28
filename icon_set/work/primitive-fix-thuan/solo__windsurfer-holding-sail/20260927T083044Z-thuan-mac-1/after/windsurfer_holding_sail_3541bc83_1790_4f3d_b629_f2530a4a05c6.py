from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '3541bc83-1790-4f3d-b629-f2530a4a05c6'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__windsurfer-holding-sail/20260927T083044Z-thuan-mac-1/reference/nautic sports sailing person_3541bc83-1790-4f3d-b629-f2530a4a05c6.svg'
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
    icon_id = 'windsurfer-holding-sail'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'recreation'
    categories = ('primitives', 'recreation')
    aliases = ()
    keywords = ('windsurfer', 'holding', 'sail')

    def build(self) -> None:
        # Plan (human ref full_body_ref.png; reference layout): windsurfer on the left leaning back,
        # r4 head 8 above a vertical neck stub, arms reaching to the boom grip on the slanted mast;
        # tall sail = mast (22,6)->(28,40) + foot to the clew + a cubic leech bulging right back to
        # the head of the sail; feet and mast foot stand in a cubic wave line (y38..42).
        _circle(self, "head", 10, 14, 4)
        self.add_line("torso", (10, 26), (10, 28))
        self.add_line("torso-lean", (10, 28), (13, 33))
        self.mark_human_figure("sailor", head="head", torso="torso", torso_junction="start")
        self.add_line("arms", (10, 28), (25, 23))
        self.add_line("legs", (13, 33), (18, 40))
        _path(self, "sail", (22, 6), [(25, 23), (28, 40), (40, 32), ('c', (43, 22), (36, 10), (22, 6))], closed=True)
        a = 8 / 3
        knots = [(6, 40), (18, 40), (28, 40), (42, 40)]
        steps, up = [], False
        for (x0, _), (x1, _) in zip(knots, knots[1:]):
            d = (x1 - x0) / 3
            cy = 40 - a if up else 40 + a
            steps.append(('c', (x0 + d, cy), (x1 - d, cy), (x1, 40)))
            up = not up
        _path(self, "water", (6, 40), steps)
        for p, q in (("torso", "torso-lean"), ("torso", "arms"), ("torso-lean", "arms"), ("torso-lean", "legs")):
            self.relate("connect", p, q)
        self.relate("connect", "arms", "sail-1", "sail-2")
        self.relate("connect", "legs", "water-1", "water-2")
        self.relate("connect", "sail", "water-2", "water-3")
