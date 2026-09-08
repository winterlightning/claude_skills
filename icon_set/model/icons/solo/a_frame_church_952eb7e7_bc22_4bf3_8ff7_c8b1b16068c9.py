"""A-Frame Church. Rebuilt from the supplied silhouette."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '952eb7e7-bc22-4bf3-8ff7-c8b1b16068c9'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-01/church_952eb7e7-bc22-4bf3-8ff7-c8b1b16068c9.svg'
AUTHOR = 'gpt-6'


class Landmark(Solo48):
    icon_id = 'a-frame-church'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "places/landmarks"
    aliases = ()
    keywords = ('church', 'chapel', 'cross', 'religion', 'worship', 'a-frame', 'roof', 'christian')

    def build(self):
        self.add_polyline('roof', (2, 31), (24, 17), (46, 31), closed=False)
        self.add_polyline('outline', (8, 27), (8, 43), (24, 43), (40, 43), (40, 27), closed=False)
        self.relate("connect", "roof", "outline")
        self.add_polyline('cross-stem', (24, 5), (24, 9), (24, 17), closed=False)
        self.add_polyline('cross-bar', (20, 9), (24, 9), (28, 9), closed=False)
        self.relate("connect", "cross-stem", "cross-bar")
        self.relate("connect", "cross-stem", 'roof')
        self.add_polyline('door', (24, 43), (24, 35), closed=False)
        self.relate("connect", "door", "outline")
