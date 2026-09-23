"""Two overlapping tied money bags, with a dollar on the front bag.

Symbol plan: separate gathered crowns meet the neck ties; broad lower
body curves distinguish a large foreground bag from a smaller back bag.
The dollar is a flowing S with attached short stems. No useful Lucide sack
construction was found; shopping-bag was inspected for closure logic only.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "facf19d7-e5b7-4559-806e-6d1d682ef4d0"
SOURCE_PATH = "pictographic-primitives/_uncategorized_27/money bags_facf19d7-e5b7-4559-806e-6d1d682ef4d0.svg"
AUTHOR = "gpt-6"


class TwoDollarMoneyBags(Solo48):
    icon_id = "two-dollar-money-bags"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "finance/money"
    aliases = ("money bags", "cash sacks")
    keywords = ("dollar", "wealth", "coins", "pair")

    def build(self) -> None:
        self.add_bezier(
            "small-bag-crown", (11, 21),
            ((9, 18), (10, 15), (13, 16)),
            ((15, 14), (16, 18), (17, 17)),
            ((20, 16), (22, 18), (19, 21)),
        )
        self.add_line("small-bag-tie", (11, 21), (19, 21))
        self.add_bezier(
            "small-bag-body", (11, 21),
            ((8, 25), (6, 28), (6, 31)),
            ((6, 35), (10, 37), (15, 37)),
        )
        self.relate("connect", "small-bag-crown", "small-bag-tie")
        self.relate("connect", "small-bag-body", "small-bag-tie")

        self.add_bezier(
            "front-bag-crown", (20, 18),
            ((18, 14), (17, 11), (19, 9)),
            ((21, 7), (22, 10), (24, 9)),
            ((25, 7), (25, 6), (27, 6)),
            ((29, 6), (30, 10), (32, 9)),
            ((35, 8), (36, 11), (34, 14)),
            ((33, 16), (32, 17), (32, 18)),
        )
        self.add_line("front-bag-tie", (20, 18), (32, 18))
        self.add_bezier(
            "front-bag-body", (20, 18),
            ((14, 23), (12, 28), (12, 32)),
            ((12, 38), (18, 42), (26, 42)),
            ((34, 42), (42, 38), (42, 32)),
            ((42, 27), (36, 22), (32, 18)),
        )
        self.relate("connect", "front-bag-crown", "front-bag-tie")
        self.relate("connect", "front-bag-body", "front-bag-tie")

        self.add_line("dollar-upper-stem", (27, 24), (27, 27))
        self.add_bezier(
            "dollar-s", (27, 27),
            ((23, 25), (22, 28), (24, 29)),
            ((26, 30), (31, 29), (31, 32)),
            ((31, 34), (28, 35), (26, 33)),
        )
        self.add_line("dollar-lower-stem", (26, 33), (26, 35))
        self.add_contour("dollar", "dollar-upper-stem", "dollar-s", "dollar-lower-stem")
