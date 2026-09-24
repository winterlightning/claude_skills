"""A frontal person beneath three ranking stars.

Plan: a centered circular head sits exactly eight centerline units above a
mirrored shoulder arc. Three compact stars form a symmetric upper series.
Human user.svg owns the bust proportions; Lucide user-round and star informed
the circle/shoulder and five-tip constructions.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

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
        # Three open five-ray stars preserve count without microscopic pockets.
        for index, cx in enumerate((9, 24, 39)):
            ends = ((cx, 6), (cx+3, 9), (cx+2, 12), (cx-2, 12), (cx-3, 9))
            names=[]
            for j, end in enumerate(ends):
                name=f"star-{index}-ray-{j}"
                self.add_line(name, (cx, 10), end)
                names.append(name)
            self.relate("connect", *names)
        self.add_arc("head-upper", (19, 25), (29, 25), radius_x=5, sweep=True)
        self.add_arc("head-lower", (29, 25), (19, 25), radius_x=5, sweep=True)
        self.add_contour("head", "head-upper", "head-lower", closed=True)
        self.add_arc("shoulders", (8, 42), (40, 42), radius_x=16, radius_y=4, sweep=True)
