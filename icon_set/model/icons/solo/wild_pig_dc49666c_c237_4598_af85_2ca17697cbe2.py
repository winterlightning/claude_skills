"""Front-facing boar with pointed ears, eyes and broad nostril-bearing snout. Revised for recognition using Lucide dog cheek construction."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dc49666c-c237-4598-af85-2ca17697cbe2'
SOURCE_PATH = 'pictographic-primitives/animals/wild pig_dc49666c-c237-4598-af85-2ca17697cbe2.svg'
AUTHOR = 'gpt-6'


class BoarHead(Solo48):
    icon_id = 'boar-head'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/animals"
    aliases = ()
    keywords = ('boar', 'pig', 'head', 'ears', 'silhouette', 'face', 'wild', 'animal')

    def build(self) -> None:
        # SQUARE centerline extremes (2,2)-(46,46).
        self.add_polyline('ears-and-crown', (10,18), (2,2), (16,10), (32,10), (46,2), (38,18))
        self.add_arc('right-cheek-top', (38,18), (46,26), radius_x=8)
        self.add_arc('right-cheek-bottom', (46,26), (36,36), radius_x=10)
        self.add_contour('right-cheek', 'right-cheek-top', 'right-cheek-bottom')
        self.add_arc('left-cheek-bottom', (12,36), (2,26), radius_x=10)
        self.add_arc('left-cheek-top', (2,26), (10,18), radius_x=8)
        self.add_contour('left-cheek', 'left-cheek-bottom', 'left-cheek-top')
        self.add_arc('snout-top', (12,36), (36,36), radius_x=12, radius_y=10)
        self.add_arc('snout-bottom', (36,36), (12,36), radius_x=12, radius_y=10)
        self.add_contour('snout', 'snout-top', 'snout-bottom', closed=True)
        self.add_dot('eye-left', (17,18))
        self.add_dot('eye-right', (31,18))
        self.add_dot('nostril-left', (21,36))
        self.add_dot('nostril-right', (27,36))
        self.relate('connect', 'ears-and-crown', 'left-cheek')
        self.relate('connect', 'ears-and-crown', 'right-cheek')
        self.relate('connect', 'snout', 'left-cheek')
        self.relate('connect', 'snout', 'right-cheek')
