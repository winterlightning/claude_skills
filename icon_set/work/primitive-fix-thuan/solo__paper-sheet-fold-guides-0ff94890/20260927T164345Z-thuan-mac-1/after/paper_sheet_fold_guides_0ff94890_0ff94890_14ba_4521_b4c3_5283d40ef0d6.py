from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "0ff94890-14ba-4521-b4c3-5283d40ef0d6"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__paper-sheet-fold-guides-0ff94890/20260927T164345Z-thuan-mac-1/reference/paper sizes folding dash_0ff94890-14ba-4521-b4c3-5283d40ef0d6.svg"
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


class PaperSheetFoldGuides(Solo48):
    """A portrait paper sheet with a clipped top-right corner and dashed fold guides:
    a horizontal dashed fold across the middle and a vertical dashed fold above it.

    Plan (VRECT_L, x 8..40, y 4..44): the sheet's walls are standalone members joined by
    `connect` (rounded r4 corners, diagonal cut (32,4)-(40,12)) so every 8-unit dash gap
    certifies straight-vs-straight. Horizontal fold y=27: wall stubs 8..12 and 36..40 plus
    a centre dash 20..28. Vertical fold x=24: a stub hanging from the top edge (4..8) and a
    dash 16..19 that stops 8 above the horizontal fold.
    """
    icon_id = "paper-sheet-fold-guides-0ff94890"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "documents"
    categories = ("primitives", "documents")
    aliases = ("paper sizes", "paper folding")
    keywords = ("paper", "sheet", "fold", "guides", "dashed", "document", "size")

    def build(self) -> None:
        L, T, R, B, r, fy, ax = 8, 4, 40, 44, 4, 27, 24
        segs = [
            ("top-left", "L", (L + r, T), (ax, T)), ("top-right", "L", (ax, T), (32, T)),
            ("cut", "L", (32, T), (R, 12)),
            ("right-upper", "L", (R, 12), (R, fy)), ("right-lower", "L", (R, fy), (R, B - r)),
            ("corner-br", "A", (R, B - r), (R - r, B)), ("bottom", "L", (R - r, B), (L + r, B)),
            ("corner-bl", "A", (L + r, B), (L, B - r)),
            ("left-lower", "L", (L, B - r), (L, fy)), ("left-upper", "L", (L, fy), (L, T + r)),
            ("corner-tl", "A", (L, T + r), (L + r, T)),
        ]
        for name, kind, a, b in segs:
            if kind == "L":
                self.add_line(name, a, b)
            else:
                self.add_arc(name, a, b, radius_x=r, radius_y=r, sweep=True)
        for (n1, *_), (n2, *_) in zip(segs, segs[1:] + segs[:1]):
            self.relate("connect", n1, n2)
        self.add_line("fold-h-left", (L, fy), (12, fy))
        self.add_line("fold-h-mid", (20, fy), (28, fy))
        self.add_line("fold-h-right", (36, fy), (R, fy))
        self.add_line("fold-v-top", (ax, T), (ax, 8))
        self.add_line("fold-v-mid", (ax, 16), (ax, fy - 8))
        for stub, walls in (("fold-h-left", ("left-lower", "left-upper")),
                            ("fold-h-right", ("right-upper", "right-lower")),
                            ("fold-v-top", ("top-left", "top-right"))):
            for w in walls:
                self.relate("connect", stub, w)
