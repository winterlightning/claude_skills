from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "32057a32-76a0-4772-a719-f437eee961f4"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__pointed-shirt-collar-with-button/20260927T164345Z-thuan-mac-1/reference/collar_32057a32-76a0-4772-a719-f437eee961f4.svg"
AUTHOR = "claude-opus-5-5"


def _path(icon, name, start, steps, closed=False):
    """steps: ('L', end) | ('A', end, r[, ry], sweep[, large]) | ('C', c1, c2, end)"""
    here, members = start, []
    for i, st in enumerate(steps):
        m = f"{name}-{i + 1}"
        if st[0] == "L":
            icon.add_line(m, here, st[1]); here = st[1]
        elif st[0] == "A":
            end, r = st[1], st[2]
            rest = list(st[3:])
            ry = r
            if rest and not isinstance(rest[0], bool):
                ry = rest.pop(0)
            sweep = rest[0] if rest else True
            large = rest[1] if len(rest) > 1 else False
            icon.add_arc(m, here, end, radius_x=r, radius_y=ry, large_arc=large, sweep=sweep); here = end
        else:
            icon.add_bezier(m, here, (st[1], st[2], st[3])); here = st[3]
        members.append(m)
    icon.add_contour(name, *members, closed=closed)


def _circle(icon, name, cx, cy, r):
    _path(icon, name, (cx, cy - r), [("A", (cx + r, cy), r, True), ("A", (cx, cy + r), r, True),
                                      ("A", (cx - r, cy), r, True), ("A", (cx, cy - r), r, True)], True)


class PointedShirtCollarWithButton(Solo48):
    """Front view of a pointed shirt collar: two mirrored flaps meeting at the neck point,
    a short placket line below the gap and one round button at the bottom.

    Plan: axis x=24, SQUARE. Left flap quad T(10,6) -> C(24,15) -> tip(14,25) -> outer(6,14);
    right flap mirrored. The placket starts 8.5 below the flaps' 45-degree inner edges (y=27)
    and meets an r4 button whose bottom sets the keyshape bottom (y=42).
    """
    icon_id = "pointed-shirt-collar-with-button"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "clothing"
    categories = ("primitives", "clothing")
    aliases = ("collar", "shirt collar")
    keywords = ("pointed", "shirt", "collar", "button", "clothing", "formal")

    def build(self) -> None:
        ax = 24
        top, centre, tip, outer = (10, 6), (ax, 15), (14, 25), (6, 14)
        m = lambda p: (2 * ax - p[0], p[1])
        self.add_polyline("flap-left", top, centre, tip, outer, closed=True)
        self.add_polyline("flap-right", m(top), m(outer), m(tip), centre, closed=True)
        self.relate("connect", "flap-left", "flap-right")
        self.add_line("placket", (ax, 27), (ax, 34))
        _circle(self, "button", ax, 38, 4)
        self.relate("connect", "placket", "button")
