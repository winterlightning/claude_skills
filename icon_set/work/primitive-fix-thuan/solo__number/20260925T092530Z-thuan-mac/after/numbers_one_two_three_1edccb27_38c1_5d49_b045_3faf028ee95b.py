"""Number: the digits 1, 2 and 3 - a one on top, a two and a three below.

Symbol plan: hand-authored stroke digits. The 1 is a stem with a short
flag and a base serif centred on x = 24. The 2 is a hook bowl that sweeps
in one curve down to the baseline and a straight base. The 3 is two bowls
meeting at a waist node; each bowl's outer side and return is a single
cubic so the pinch at the waist is shared-endpoint geometry. Rows are 8
apart and the 2 and 3 are 8 apart. Keyshape SQUARE, centerline box
(6,6)-(42,42).
Lucide construction: list-ordered / hash digit strokes (open stroke
numerals with round caps).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "1edccb27-38c1-5d49-b045-3faf028ee95b"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__number/20260925T092530Z-thuan-mac/reference/number_1edccb27-38c1-5d49-b045-3faf028ee95b.svg"
AUTHOR = "claude-opus-5-5"


class NumberOneTwoThree(Solo48):
    icon_id = "number"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "text"
    aliases = ("numbers", "123", "numeric")
    keywords = ("number", "digits", "one", "two", "three", "count")

    def build(self) -> None:
        # 1
        self.add_polyline("one-stem", (20, 9), (24, 6), (24, 18))
        self.add_line("one-base-1", (20, 18), (24, 18))
        self.add_line("one-base-2", (24, 18), (28, 18))
        self.relate("connect", "one-stem", "one-base-1")
        self.relate("connect", "one-stem", "one-base-2")
        # 2
        self.add_bezier("two-curve", (6, 32),
                        ((6, 29), (9, 26), (13, 26)),
                        ((17, 26), (20, 29), (20, 32)),
                        ((20, 36), (12, 39), (6, 42)))
        self.add_line("two-base", (6, 42), (20, 42))
        self.add_contour("two", "two-curve", "two-base")
        # 3
        waist = (33, 34)
        self.add_bezier("three-upper", (29, 28),
                        ((30.5, 26.5), (32, 26), (35, 26)),
                        ((42, 26), (41, 34), waist))
        self.add_bezier("three-lower", waist,
                        ((38.5, 34), (42, 35), (42, 38)),
                        ((42, 41), (39, 42), (35, 42)),
                        ((32, 42), (29.5, 41.5), (28, 40)))
        self.add_contour("three", "three-upper", "three-lower")
