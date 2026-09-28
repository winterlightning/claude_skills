"""Two cupped hands holding up a puzzle piece (module / integration).

Symbol plan: the puzzle piece is a 12x12 square (18..30, 10..22) with two round knobs (r4
semicircles) on its top and right sides. Below it the two hands are mirror images about
x=24: each is an open palm seen from the front - a finger block (r4 round top, crest y=27,
kept 9+ from the piece corner) over the wrist running to the bottom edge - with the thumb
angled up and in from the inner edge, its tip 10 clear of the piece.
Lucide construction: 'puzzle' (square piece with round knobs) and 'hand' (open palm with
angled thumb).
Keyshape SQUARE: centerline x 6..42 (finger edges), y 6..42 (top knob, wrists).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "cafe2d4d-7c9a-454e-8b86-9c5b5f0b2b05"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__hands-holding-puzzle-piece/20260926T035939Z-thuan-mac/reference/module hands puzzle_cafe2d4d-7c9a-454e-8b86-9c5b5f0b2b05.svg"
AUTHOR = "claude-opus-5-5"


class HandsHoldingPuzzlePiece(Solo48):
    icon_id = "hands-holding-puzzle-piece"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "business/concepts"
    aliases = ("module-hands-puzzle", "hands-puzzle", "integration-hands")
    keywords = ("puzzle", "piece", "hands", "module", "integration", "solution", "support", "teamwork", "fit")

    def build(self) -> None:
        # puzzle piece, clockwise from the top-left corner
        self.add_line("piece-top-left", (18, 10), (20, 10))
        self.add_arc("piece-knob-top", (20, 10), (28, 10), radius_x=4, sweep=True)
        self.add_line("piece-top-right", (28, 10), (30, 10))
        self.add_line("piece-right-upper", (30, 10), (30, 12))
        self.add_arc("piece-knob-right", (30, 12), (30, 20), radius_x=4, sweep=True)
        self.add_line("piece-right-lower", (30, 20), (30, 22))
        self.add_line("piece-bottom", (30, 22), (18, 22))
        self.add_line("piece-left", (18, 22), (18, 10))
        self.add_contour("piece", "piece-top-left", "piece-knob-top", "piece-top-right", "piece-right-upper",
                         "piece-knob-right", "piece-right-lower", "piece-bottom", "piece-left", closed=True)
        # open hands, palms toward the viewer: finger block over the wrist, thumb angled in
        for side, f in (("left", lambda p: p), ("right", lambda p: (48 - p[0], p[1]))):
            sw = side == "left"
            self.add_line(f"hand-{side}-outer", f((6, 42)), f((6, 31)))
            self.add_arc(f"hand-{side}-fingers", f((6, 31)), f((14, 31)), radius_x=4, sweep=sw)
            self.add_line(f"hand-{side}-inner-upper", f((14, 31)), f((14, 36)))
            self.add_line(f"hand-{side}-inner-lower", f((14, 36)), f((14, 42)))
            self.add_contour(f"hand-{side}", f"hand-{side}-outer", f"hand-{side}-fingers",
                             f"hand-{side}-inner-upper", f"hand-{side}-inner-lower")
            self.add_line(f"thumb-{side}", f((14, 36)), f((19, 32)))
            self.relate("connect", f"hand-{side}", f"thumb-{side}")
