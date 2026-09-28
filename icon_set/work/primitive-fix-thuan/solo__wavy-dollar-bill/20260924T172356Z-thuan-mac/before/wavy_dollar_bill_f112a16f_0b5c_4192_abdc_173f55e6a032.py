"""A wide dollar banknote with gently waved long edges.

Symbol plan: one closed paper outline shares straight vertical ends with
three-piece top and bottom waves; a compact central dollar remains detached.
Lucide banknote informed the balanced enclosure and centered currency mark.
The unequal wave heights are intentional to show flexible paper.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "f112a16f-0b5c-4192-abdc-173f55e6a032"
SOURCE_PATH = "pictographic-primitives/_uncategorized_27/money bill wave_f112a16f-0b5c-4192-abdc-173f55e6a032.svg"
AUTHOR = "gpt-6"


class WavyDollarBill(Solo48):
    icon_id = "wavy-dollar-bill"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "finance/money"
    aliases = ("waving dollar note", "money bill wave")
    keywords = ("cash", "banknote", "dollar", "paper")

    def build(self) -> None:
        self.add_bezier(
            "bill-top", (4, 10),
            ((7, 9), (10, 8), (14, 8)),
            ((19, 8), (22, 11), (28, 11)),
            ((35, 13), (40, 11), (44, 10)),
        )
        self.add_line("bill-right", (44, 10), (44, 38))
        self.add_bezier(
            "bill-bottom", (44, 38),
            ((40, 39), (36, 40), (32, 40)),
            ((27, 40), (23, 37), (18, 37)),
            ((12, 36), (8, 37), (4, 38)),
        )
        self.add_line("bill-left", (4, 38), (4, 10))
        self.add_contour("bill", "bill-top", "bill-right", "bill-bottom", "bill-left", closed=True)

        self.add_line("dollar-top-stem", (24, 19), (24, 21))
        self.add_bezier(
            "dollar-s", (24, 21),
            ((21, 20), (19, 21), (19, 23)),
            ((19, 25), (29, 24), (29, 27)),
            ((29, 29), (26, 30), (24, 27)),
        )
        self.add_line("dollar-bottom-stem", (24, 27), (24, 29))
        self.add_contour("dollar", "dollar-top-stem", "dollar-s", "dollar-bottom-stem")
