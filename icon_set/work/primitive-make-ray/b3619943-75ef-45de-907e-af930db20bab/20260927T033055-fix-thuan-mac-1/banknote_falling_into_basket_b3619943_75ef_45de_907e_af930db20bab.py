from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'b3619943-75ef-45de-907e-af930db20bab'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__banknote-falling-into-basket/20260927T032145Z-thuan-mac-1/reference/money basket_b3619943-75ef-45de-907e-af930db20bab.svg'
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
    icon_id = 'banknote-falling-into-basket'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'business'
    categories = ('primitives', 'business')
    aliases = ()
    keywords = ('banknote', 'basket', 'money', 'payment', 'cash', 'collection', 'deposit', 'finance')

    def build(self) -> None:
        # basket: rim with a short lip, sides tapering to the base, two ribs
        self.add_line("rim", (6, 27), (42, 27))
        _path(self, "basket", (10, 27), [(13, 42), (37, 42), (40, 27)])
        self.add_line("rib-left", (21, 27), (21, 42))
        self.add_line("rib-right", (29, 27), (29, 42))
        for part in ("basket", "rib-left", "rib-right"):
            self.relate("connect", "rim", part)
        self.relate("connect", "basket", "rib-left")
        self.relate("connect", "basket", "rib-right")
        # banknote tilted 1:3 as it drops in: its lower half is hidden behind the rim
        _path(self, "note", (10, 27), [(6, 15), (33, 6), (40, 27)])
        self.relate("connect", "note", "rim")
        self.relate("connect", "note", "basket")
        self.add_dot("note-centre", (21, 19))
