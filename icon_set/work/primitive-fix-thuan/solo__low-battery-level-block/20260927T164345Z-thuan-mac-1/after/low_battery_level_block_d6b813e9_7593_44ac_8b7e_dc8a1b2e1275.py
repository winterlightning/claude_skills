from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "d6b813e9-7593-44ac-8b7e-dc8a1b2e1275"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__low-battery-level-block/20260927T164345Z-thuan-mac-1/reference/charging battery low_d6b813e9-7593-44ac-8b7e-dc8a1b2e1275.svg"
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


class LowBatteryLevelBlock(Solo48):
    """Horizontal battery: rounded case, rounded terminal nub, one solid low-charge bar.

    Plan: case rounded rect (4,10)-(36,38) r4; terminal (36,18)-(44,30) r2 sharing the
    case's right wall; the level block is a single 4-wide stroke 8 inside the case's left
    and top/bottom walls (x=12, y 18..30) so it reads as a solid low-charge block.
    """
    icon_id = "low-battery-level-block"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "devices"
    categories = ("primitives", "devices")
    aliases = ("Low Battery Level", "battery low")
    keywords = ("low", "battery", "level", "charge", "power")

    def build(self) -> None:
        L, T, R, B, r = 4, 10, 36, 38, 4
        # Walls are standalone members joined by `connect`, so the exact 8-unit
        # clearance to the level bar certifies straight-vs-straight.
        segs = [
            ("case-top", "L", (L + r, T), (R - r, T)), ("case-tr", "A", (R - r, T), (R, T + r)),
            ("case-right", "L", (R, T + r), (R, B - r)), ("case-br", "A", (R, B - r), (R - r, B)),
            ("case-bottom", "L", (R - r, B), (L + r, B)), ("case-bl", "A", (L + r, B), (L, B - r)),
            ("case-left", "L", (L, B - r), (L, T + r)), ("case-tl", "A", (L, T + r), (L + r, T)),
        ]
        for name, kind, a, b in segs:
            if kind == "L":
                self.add_line(name, a, b)
            else:
                self.add_arc(name, a, b, radius_x=r, radius_y=r, sweep=True)
        for (n1, *_), (n2, *_) in zip(segs, segs[1:] + segs[:1]):
            self.relate("connect", n1, n2)
        _path(self, "terminal", (R, 18), [("L", (42, 18)), ("A", (44, 20), 2, True), ("L", (44, 28)),
                                          ("A", (42, 30), 2, True), ("L", (R, 30))])
        self.relate("connect", "case-right", "terminal")
        self.add_line("level", (12, 18), (12, 30))
