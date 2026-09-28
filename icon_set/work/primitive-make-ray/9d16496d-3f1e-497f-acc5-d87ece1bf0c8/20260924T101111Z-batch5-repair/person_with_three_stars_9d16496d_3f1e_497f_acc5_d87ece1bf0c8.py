"""male star: standalone repair of supplied reference.

Plan: Three-star row above centered person. Keyshape HRECT_L.
Reduction: Replaced closed five-point outlines with open five-ray stars; reduced head to radius 3.
Construction references: local Lucide originals and atomic-debug: star.
human_ref/user.svg: head center (24,27), radius 3; shoulder apex y=38 yields exactly 8 centerline / 4 ink gap. Symmetric about x=24.
All geometry is authored for SOLO48; earlier runs remain unchanged.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "9d16496d-3f1e-497f-acc5-d87ece1bf0c8"
SOURCE_PATH = "pictographic-primitives/_uncategorized_26/male star_9d16496d-3f1e-497f-acc5-d87ece1bf0c8.svg"
AUTHOR = "gpt-6"


class PersonWithThreeStars(Solo48):
    icon_id = "person-with-three-stars"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/recognition"
    aliases = ("rated-person",)
    keywords = ("person", "stars", "rating", "recognition")

    def build(self) -> None:
        # Three open five-ray stars preserve count without microscopic pockets.
        for index, cx in enumerate((8, 24, 40)):
            ends = ((cx, 8), (cx+4, 11), (cx+3, 16), (cx-3, 16), (cx-4, 11))
            names=[]
            for j, end in enumerate(ends):
                name=f"star-{index}-ray-{j}"
                self.add_line(name, (cx, 12), end)
                names.append(name)
            self.relate("connect", *names)
        self.add_arc("head-upper", (21, 27), (27, 27), radius_x=3, sweep=True)
        self.add_arc("head-lower", (27, 27), (21, 27), radius_x=3, sweep=True)
        self.add_contour("head", "head-upper", "head-lower", closed=True)
        self.add_arc("shoulders", (8, 40), (40, 40), radius_x=16, radius_y=2, sweep=True)
