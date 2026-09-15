"""A person leaning forward with outstretched arms and one bent leg. SQUARE extremes (6,6)-(42,42). Lucide person-standing informs the head and connected limb framework; retain the source single visible arm silhouette and strongly leaning body. No wall is added."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e79b2a91-32af-425a-ad81-cd97e615caef'
SOURCE_PATH = 'pictographic-primitives/symbol/person running_e79b2a91-32af-425a-ad81-cd97e615caef.svg'
AUTHOR = 'gpt-6'


class PersonPushingForward(Solo48):
    icon_id = 'person-pushing-forward'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('push', 'person', 'effort', 'force', 'lean', 'move', 'exercise', 'strength')

    def build(self) -> None:
        cx, cy, radius = 30, 12, 6
        self.add_arc('head-top', (cx-radius, cy), (cx+radius, cy), radius_x=radius)
        self.add_arc('head-bottom', (cx+radius, cy), (cx-radius, cy), radius_x=radius)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_polyline('body-back-leg',(24,26),(16,34),(6,42))
        self.add_polyline('arms',(24,26),(28,28),(42,28))
        self.add_polyline('front-leg',(16,34),(28,36),(24,42))
        self.relate('connect','body-back-leg','arms')
        self.relate('connect','body-back-leg','front-leg')
