from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'cac28c98-7a13-413c-8246-fe935c1db139'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hanging-bassinet/20260927T061820Z-thuan-mac-1/reference/rocking crib basket swing bed_cac28c98-7a13-413c-8246-fe935c1db139.svg'
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
    icon_id = 'hanging-bassinet'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'babies'
    categories = ('babies', 'primitives')
    aliases = ()
    keywords = ('hanging', 'bassinet', 'baby', 'nursery', 'toy')

    def build(self) -> None:
        # hanging bassinet: a rounded canopy whose lower edge is a valance of three shallow r10
        # scallops (chord 12), the basket (flat rim, deep half-ellipse body rx18/ry16) hanging from
        # the outer scallops on two straps. Mirrored about x=24.
        _path(self, "canopy", (6, 15), [(6, 14), ((14, 6), 8, 8, True), (34, 6), ((42, 14), 8, 8, True), (42, 15),
                                        ((36, 17), 10, 10, True), ((30, 15), 10, 10, True),
                                        ((18, 15), 10, 10, True),
                                        ((12, 17), 10, 10, True), ((6, 15), 10, 10, True)], closed=True)
        _path(self, "basket", (6, 26), [(12, 26), (36, 26), (42, 26), ((6, 26), 18, 16, True)], closed=True)
        self.add_line("strap-left", (12, 17), (12, 26))
        self.add_line("strap-right", (36, 17), (36, 26))
        for s in ("strap-left", "strap-right"):
            self.relate("connect", s, "canopy"); self.relate("connect", s, "basket")
