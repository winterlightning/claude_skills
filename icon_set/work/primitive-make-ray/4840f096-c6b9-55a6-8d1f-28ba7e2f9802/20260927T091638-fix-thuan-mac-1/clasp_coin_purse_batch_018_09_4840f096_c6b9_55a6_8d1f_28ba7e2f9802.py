from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '4840f096-c6b9-55a6-8d1f-28ba7e2f9802'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__clasp-coin-purse-batch-018-09/20260927T091421Z-thuan-mac-1/reference/coin purse_4840f096-c6b9-55a6-8d1f-28ba7e2f9802.svg'
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
    icon_id = 'clasp-coin-purse-batch-018-09'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'money'
    categories = ('primitives', 'money')
    aliases = ()
    keywords = ('purse', 'coin', 'clasp', 'wallet', 'pouch', 'money', 'accessory', 'bag')

    def build(self) -> None:
        # Kiss-lock coin purse, mirrored about x = 24: two r3 clasp balls touching at (24,9) and sitting
        # on the frame; a narrow frame band (x 12..36, y 12..20) with r4 top corners; a pouch that flares
        # out to the SQUARE sides and ends in r6 bottom corners on the SQUARE bottom.
        _circle(self, "ball-left", 21, 9, 3)
        _circle(self, "ball-right", 27, 9, 3)
        _path(self, "frame-left", (21, 12), [(16, 12), ((12, 16), 4, 4, False), (12, 20)])
        _path(self, "frame-right", (27, 12), [(32, 12), ((36, 16), 4, 4, True), (36, 20)])
        self.add_line("frame-bottom", (12, 20), (36, 20))
        _path(self, "pouch", (12, 20), [('c', (10, 23), (6, 26), (6, 30)), (6, 36), ((12, 42), 6, 6, False),
                                        (36, 42), ((42, 36), 6, 6, False), (42, 30), ('c', (42, 26), (38, 23), (36, 20))])
        for a, b in (("ball-left", "ball-right"), ("ball-left", "frame-left"), ("ball-right", "frame-right"),
                     ("frame-left", "frame-bottom"), ("frame-right", "frame-bottom"), ("frame-bottom", "pouch")):
            self.relate("connect", a, b)
