"""A leaning person pressing against a wall. SQUARE extremes (6,6)-(42,42). Lucide person-standing informs connected limb construction; no exact pushing match. Preserve the bent knee and right wall, and make the hand contact explicit."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fe641fda-6a23-4dc4-970c-90a6fe33f671'
SOURCE_PATH = 'pictographic-primitives/symbol/person pushing_fe641fda-6a23-4dc4-970c-90a6fe33f671.svg'
AUTHOR = 'gpt-6'


class PersonPushingWall(Solo48):
    icon_id = 'person-pushing-wall'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('push', 'wall', 'person', 'effort', 'force', 'exercise', 'strength', 'resistance')

    def build(self) -> None:
        cx, cy, radius = 26, 12, 6
        self.add_arc('head-top', (cx-radius, cy), (cx+radius, cy), radius_x=radius)
        self.add_arc('head-bottom', (cx+radius, cy), (cx-radius, cy), radius_x=radius)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_polyline('body-back-leg',(22,26),(16,34),(6,42))
        self.add_polyline('arm',(22,26),(30,28),(42,22))
        self.add_polyline('front-leg',(16,34),(28,34),(24,42))
        self.add_polyline('wall',(42,6),(42,22),(42,42))
        self.relate('connect','body-back-leg','arm')
        self.relate('connect','body-back-leg','front-leg')
        self.relate('connect','arm','wall')
