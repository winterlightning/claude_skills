"""A right-facing human head silhouette with an open neck."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "66eefdff-ac9b-4760-951f-816ff21b1e05"
SOURCE_PATH = "pictographic-primitives/other/head_66eefdff-ac9b-4760-951f-816ff21b1e05.svg"
AUTHOR = "gpt-6"


class HumanHeadSideProfile(Solo48):
    icon_id = "human-head-side-profile"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/anatomy"
    aliases = ("head profile", "side face")
    keywords = ("human", "face", "mind", "head")

    def build(self) -> None:
        # One continuous right-facing silhouette. The smooth skull and jaw
        # follow the human reference's simple anatomy; the projecting nose
        # remains intentionally asymmetric and angular as in the source.
        self.add_line("rear-neck", (12, 42), (12, 31))
        self.add_bezier("back-head", (12, 31), ((8, 27), (6, 23), (6, 18)))
        self.add_bezier("crown-left", (6, 18), ((6, 10), (14, 6), (24, 6)))
        self.add_bezier("crown-right", (24, 6), ((30, 6), (34, 10), (36, 15)))
        self.add_line("forehead", (36, 15), (42, 24))
        self.add_line("nose-return", (42, 24), (37, 25))
        self.add_line("face-front", (37, 25), (37, 31))
        self.add_bezier("jaw", (37, 31), ((37, 35), (33, 36), (29, 36)))
        self.add_line("front-neck", (29, 36), (29, 42))
        self.add_contour("head-profile", "rear-neck", "back-head",
                         "crown-left", "crown-right", "forehead",
                         "nose-return", "face-front", "jaw", "front-neck")
