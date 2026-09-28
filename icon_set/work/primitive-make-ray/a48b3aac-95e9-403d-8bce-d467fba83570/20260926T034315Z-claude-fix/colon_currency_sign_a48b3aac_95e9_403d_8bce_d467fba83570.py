"""The colon currency sign (₡): a tall C crossed by a diagonal slash.

Symbol plan: the C is one open run, mirrored about y=24: a straight left side (x=12,
y 18..30) and smooth bezier bows to the top and bottom (extremes y=4/44 as integer knots)
that curl slightly back at their ends (x=40). The slash is a 45-degree line that crosses
the C's straight side at the exact node (12,24) (both split there, a provable
straight-straight crossing), running from outside at the lower left to a free end inside
the C, 8+ from the bowl.
Lucide construction: 'cent'/'euro' - currency letter with a crossing stroke.
Keyshape VRECT_L: centerline x 8..40 (slash foot, C ends), y 4..44 (C top, C bottom).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "a48b3aac-95e9-403d-8bce-d467fba83570"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__colon-currency-sign/20260926T034135Z-thuan-mac/reference/colon sign_a48b3aac-95e9-403d-8bce-d467fba83570.svg"
AUTHOR = "claude-opus-5-5"


class ColonCurrencySign(Solo48):
    icon_id = "colon-currency-sign"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbols/currency"
    aliases = ("colon sign", "costa rican colon", "salvadoran colon", "₡")
    keywords = ("colon", "currency", "money", "costa rica", "el salvador", "crc", "symbol")

    def build(self) -> None:
        side, mid, ax = 12, 24, 24

        def my(y):
            return 2 * mid - y

        self.add_bezier("bow-top", (40, 8), ((36, 4), (30, 4), (ax, 4)), ((16, 4), (side, 10), (side, 18)))
        cross = (side, 28)
        self.add_line("side-upper", (side, 18), cross)
        self.add_line("side-lower", cross, (side, my(18)))
        self.add_bezier("bow-bottom", (side, my(18)), ((side, my(10)), (16, my(4)), (ax, my(4))),
                        ((30, my(4)), (36, my(4)), (40, my(8))))
        self.add_contour("c", "bow-top", "side-upper", "side-lower", "bow-bottom")
        # slash: 45 degrees through the node on the straight side
        self.add_line("slash-out", (8, cross[1] + 4), cross)
        self.add_line("slash-in", cross, (26, 14))
        self.add_contour("slash", "slash-out", "slash-in")
        self.relate("connect", "c", "slash")
