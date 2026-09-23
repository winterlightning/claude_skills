"""A personal identification card with a small bust and two text rules."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "42934536-bcce-5901-84a4-d7a7a1f46294"
SOURCE_PATH = "pictographic-primitives/office/business card_42934536-bcce-5901-84a4-d7a7a1f46294.svg"
AUTHOR = "gpt-6"


class PersonalIdentificationCard(Solo48):
    icon_id = "personal-identification-card"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    human_construction = "bust"
    category = "objects/office"
    aliases = ("business card", "contact card")
    keywords = ("identification", "profile", "person", "contact")

    def build(self) -> None:
        # A horizontal card, with consistently rounded exterior corners.
        self.add_line("card-top", (7, 8), (41, 8))
        self.add_arc("card-ne", (41, 8), (44, 11), radius_x=3)
        self.add_line("card-right", (44, 11), (44, 37))
        self.add_arc("card-se", (44, 37), (41, 40), radius_x=3)
        self.add_line("card-bottom", (41, 40), (7, 40))
        self.add_arc("card-sw", (7, 40), (4, 37), radius_x=3)
        self.add_line("card-left", (4, 37), (4, 11))
        self.add_arc("card-nw", (4, 11), (7, 8), radius_x=3)
        self.add_contour("card", "card-top", "card-ne", "card-right",
                         "card-se", "card-bottom", "card-sw", "card-left",
                         "card-nw", closed=True)

        # Shared human_ref/user.svg informs the circular head and open shoulders.
        # Their axial extrema are 4 centerline units apart, so the ink touches.
        self.add_arc("head-right", (17, 17), (17, 23), radius_x=3)
        self.add_arc("head-left", (17, 23), (17, 17), radius_x=3)
        self.add_contour("head", "head-right", "head-left", closed=True)
        self.add_arc("shoulder-left", (13, 31), (17, 27), radius_x=4)
        self.add_arc("shoulder-right", (17, 27), (21, 31), radius_x=4)
        self.add_contour("shoulders", "shoulder-left", "shoulder-right")
        self.relate("connect", "head", "shoulders")

        # Two independent rules represent the card's identifying text.
        self.add_line("text-top", (29, 19), (35, 19))
        self.add_line("text-bottom", (29, 29), (35, 29))
