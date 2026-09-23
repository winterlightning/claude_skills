"""A frontal person beneath three ranking stars.

Plan: a centered circular head sits exactly eight centerline units above a
mirrored shoulder arc. Three compact stars form a symmetric upper series.
Human user.svg owns the bust proportions; Lucide user-round and star informed
the circle/shoulder and five-tip constructions.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "9d16496d-3f1e-497f-acc5-d87ece1bf0c8"
SOURCE_PATH = "pictographic-primitives/_uncategorized_26/male star_9d16496d-3f1e-497f-acc5-d87ece1bf0c8.svg"
AUTHOR = "gpt-6"


class PersonWithThreeStars(Solo48):
    icon_id = "person-with-three-stars"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/recognition"
    aliases = ("rated-person",)
    keywords = ("person", "stars", "rating", "recognition")

    def build(self) -> None:
        for index, cx in enumerate((9, 24, 39)):
            self.add_polyline(f"star-{index}", (cx, 6), (cx+1, 8),
                              (cx+3, 8), (cx+1, 10), (cx+2, 12),
                              (cx, 11), (cx-2, 12), (cx-1, 10),
                              (cx-3, 8), (cx-1, 8), closed=True)
        self.add_arc("head-upper", (19, 25), (29, 25), radius_x=5, sweep=True)
        self.add_arc("head-lower", (29, 25), (19, 25), radius_x=5, sweep=True)
        self.add_contour("head", "head-upper", "head-lower", closed=True)
        self.add_arc("shoulders", (8, 42), (40, 42), radius_x=16, radius_y=4, sweep=True)
