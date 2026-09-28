from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'c468c302-cf16-44e6-8780-b21dc169190b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__woman-above-two-men/20260927T083044Z-thuan-mac-1/reference/user multiple half female male_c468c302-cf16-44e6-8780-b21dc169190b.svg'
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
    icon_id = 'woman-above-two-men'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'users'
    categories = ('users', 'primitives')
    human_construction = "bust"
    aliases = ()
    keywords = ('group', 'team', 'woman', 'men', 'users', 'people', 'leader', 'mixed')

    def build(self) -> None:
        # Plan (human ref user.svg busts, bust construction): group of three as in the reference -
        # the woman's r5 head at top centre with straight hair locks hanging from its sides,
        # above two men whose r5 heads rest on rx7/ry6 shoulder arches (circular jaw touching the
        # shoulder top in ink: extrema exactly 4 apart on a shared axis, connected).
        _circle(self, "woman-head", 24, 11, 5)
        self.add_line("woman-hair-left", (19, 11), (19, 15))
        self.add_line("woman-hair-right", (29, 11), (29, 15))
        self.relate("connect", "woman-hair-left", "woman-head")
        self.relate("connect", "woman-hair-right", "woman-head")
        for side, cx in (("left", 13), ("right", 35)):
            _circle(self, f"man-{side}-head", cx, 27, 5)
            self.add_arc(f"man-{side}-shoulders", (cx - 7, 42), (cx + 7, 42), radius_x=7, radius_y=6, sweep=True)
            self.relate("connect", f"man-{side}-head-2", f"man-{side}-shoulders")
            self.relate("connect", f"man-{side}-head-3", f"man-{side}-shoulders")
            self.relate("connect", f"man-{side}-head", f"man-{side}-shoulders")
