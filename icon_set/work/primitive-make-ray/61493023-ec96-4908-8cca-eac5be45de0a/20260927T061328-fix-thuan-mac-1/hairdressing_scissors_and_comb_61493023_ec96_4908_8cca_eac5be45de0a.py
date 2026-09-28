from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '61493023-ec96-4908-8cca-eac5be45de0a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hairdressing-scissors-and-comb/20260927T055730Z-thuan-mac-1/reference/hair dress cut_61493023-ec96-4908-8cca-eac5be45de0a.svg'
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


class Drawing(Solo48):
    icon_id = 'hairdressing-scissors-and-comb'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'beauty'
    categories = ('primitives', 'beauty')
    aliases = ()
    keywords = ('hairdressing', 'scissors', 'and', 'comb')

    def build(self) -> None:
        # closed scissors: two pieces share the tip; each runs down one blade edge and crosses the other
        # at the pivot to its finger loop (r3 rings)
        self.add_polyline("piece-a", (16, 6), (10, 24), (23, 36))
        self.add_polyline("piece-b", (16, 6), (22, 24), (9, 36))
        _circle(self, "loop-right", 23, 39, 3)
        _circle(self, "loop-left", 9, 39, 3)
        for a, b in (("piece-a", "piece-b"), ("piece-a", "loop-right"), ("piece-b", "loop-left")):
            self.relate("connect", a, b)
        # comb: outlined spine with teeth to the left
        _path(self, "comb", (34, 6), [(42, 6), (42, 38), ((34, 38), 4, 4, True), (34, 22), (34, 14), (34, 6)], closed=True)
        for j, y in enumerate((6, 14, 22)):
            self.add_line(f"tooth-{j}", (30, y), (34, y))
            self.relate("connect", f"tooth-{j}", "comb")
