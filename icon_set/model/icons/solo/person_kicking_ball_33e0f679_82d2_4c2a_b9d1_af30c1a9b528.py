"""A player running right toward a ball. SQUARE extremes (6,6)-(42,42). Lucide person-standing informs the round head and connected stick limbs; preserve the source swung arms and backward leg. Widen clearance around the ball and head while retaining the kicking pose."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '33e0f679-82d2-4c2a-b9d1-af30c1a9b528'
SOURCE_PATH = 'pictographic-primitives/symbol/person playing ball_33e0f679-82d2-4c2a-b9d1-af30c1a9b528.svg'
AUTHOR = 'gpt-6'


class PersonKickingBall(Solo48):
    icon_id = 'person-kicking-ball'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('football', 'soccer', 'kick', 'ball', 'sport', 'player', 'person', 'game')

    def build(self) -> None:
        cx, cy, radius = 30, 10, 4
        self.add_arc('head-top', (cx-radius, cy), (cx+radius, cy), radius_x=radius)
        self.add_arc('head-bottom', (cx+radius, cy), (cx-radius, cy), radius_x=radius)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_line('body',(24,22),(20,30))
        self.add_polyline('arm-back',(24,22),(14,20),(8,26))
        self.add_polyline('arm-front',(24,22),(32,26),(42,20))
        self.add_polyline('leg-back',(20,30),(14,38),(6,38))
        self.add_polyline('leg-front',(20,30),(26,34),(22,42))
        for part in ['arm-back','arm-front','leg-back','leg-front']:
            self.relate('connect','body',part)
        cx, cy, radius = 38, 38, 4
        self.add_arc('ball-top', (cx-radius, cy), (cx+radius, cy), radius_x=radius)
        self.add_arc('ball-bottom', (cx+radius, cy), (cx-radius, cy), radius_x=radius)
        self.add_contour('ball', 'ball-top', 'ball-bottom', closed=True)
