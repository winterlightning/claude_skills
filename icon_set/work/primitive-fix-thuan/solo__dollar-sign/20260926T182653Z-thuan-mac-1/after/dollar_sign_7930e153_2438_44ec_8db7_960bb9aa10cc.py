"""Dollar sign: the currency symbol $ -- a tall S with round bowls, crossed by a
straight vertical stroke that runs out above and below it.

Revision (disapproved, reason not recorded): the rejected drawing stretched the S
to the full 32-unit width with flat, squashed bowls, so it read as a wide
squiggle rather than the original's tall, narrow S with rounded bowls. The S is
now 28 wide and 34 tall with full, round bowls.

Symbol plan: point symmetry about (24,24). The S is six cubics: top terminal
(37,12) over the crown (24,7) to the left extreme (10,15) (vertical tangent),
down through the spine's centre (24,24) to the right extreme (38,33) (vertical
tangent), round the foot (24,41) to the lower terminal (11,36). The stem is x=24
from (24,4) to (24,44), sharing the S's crown, centre and foot nodes.
Lucide construction: 'dollar-sign' stem through an S; classic typographic S.
Keyshape VRECT_M: centerline x 10..38 (bowls), y 4..44 (stem).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "7930e153-2438-44ec-8db7-960bb9aa10cc"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__dollar-sign/20260926T182653Z-thuan-mac-1/reference/dollar sign_7930e153-2438-44ec-8db7-960bb9aa10cc.svg"
AUTHOR = "claude-opus-5-5"

UPPER = [((37, 12), ((35, 8.5), (30, 7), (24, 7))),
         ((24, 7), ((16, 7), (10, 10.5), (10, 15))),
         ((10, 15), ((10, 20), (17, 22.5), (24, 24)))]


def turn(p):
    return (48 - p[0], 48 - p[1])


class DollarSign(Solo48):
    icon_id = "dollar-sign"
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    aliases = ("usd", "dollar-symbol")
    keywords = ("dollar", "sign", "currency", "money", "usd", "price")

    def build(self) -> None:
        names = []
        for i, (start, (c1, c2, end)) in enumerate(UPPER):
            self.add_bezier(f"s-{i}", start, (c1, c2, end))
            names.append(f"s-{i}")
        # Lower half: the upper half turned half a turn about (24,24), reversed.
        for i, (start, (c1, c2, end)) in enumerate(reversed(UPPER)):
            self.add_bezier(f"s-{3 + i}", turn(end), (turn(c2), turn(c1), turn(start)))
            names.append(f"s-{3 + i}")
        self.add_contour("s", *names)
        self.add_line("stem-top", (24, 4), (24, 7))
        self.add_line("stem-upper", (24, 7), (24, 24))
        self.add_line("stem-lower", (24, 24), (24, 41))
        self.add_line("stem-bottom", (24, 41), (24, 44))
        self.add_contour("stem", "stem-top", "stem-upper", "stem-lower", "stem-bottom")
        self.relate("connect", "stem", "s")
