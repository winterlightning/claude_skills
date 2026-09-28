from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'e142d409-a523-4dfc-95b4-a48bd6dd01f3'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__woman-and-man-busts/20260927T083044Z-thuan-mac-1/reference/multiple man woman 2_e142d409-a523-4dfc-95b4-a48bd6dd01f3.svg'
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
    icon_id = 'woman-and-man-busts'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'users'
    categories = ('users', 'primitives')
    human_construction = "bust"
    aliases = ()
    keywords = ('woman', 'man', 'couple', 'busts', 'users', 'people', 'pair', 'profile')

    def build(self) -> None:
        # Plan (Lucide users at 2x, human ref user.svg): woman in front at left, man behind her at
        # right, as in the reference. Woman: r7 head exactly 8 above a standalone flat shoulder
        # line, r7 rounded shoulders to the bottom edge, straight hair locks hanging from the
        # head's sides. Man: only his visible right half - a semicircle head (r7) and the right
        # shoulder curving down to the bottom edge.
        _circle(self, "woman-head", 17, 15, 7)
        self.add_line("woman-hair-left", (10, 15), (10, 21))
        self.add_line("woman-hair-right", (24, 15), (24, 21))
        self.relate("connect", "woman-hair-left", "woman-head")
        self.relate("connect", "woman-hair-right", "woman-head")
        self.add_line("woman-shoulder-top", (11, 30), (23, 30))
        _path(self, "woman-shoulder-left", (4, 40), [(4, 37), ((11, 30), 7, 7, True)])
        _path(self, "woman-shoulder-right", (23, 30), [((30, 37), 7, 7, True), (30, 40)])
        self.relate("connect", "woman-shoulder-top", "woman-shoulder-left", "woman-shoulder-right")
        self.mark_human_figure("woman", head="woman-head", torso="woman-shoulder-top", torso_junction="start")
        self.add_arc("man-head", (33, 8), (33, 22), radius_x=7, radius_y=7, sweep=True)
        _path(self, "man-shoulder", (37, 30), [((44, 37), 7, 7, True), (44, 40)])
