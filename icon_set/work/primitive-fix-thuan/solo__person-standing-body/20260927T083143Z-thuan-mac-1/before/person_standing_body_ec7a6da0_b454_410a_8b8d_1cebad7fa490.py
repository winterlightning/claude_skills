"""A front-facing person with bent lower arms and open torso. VRECT_L extremes (8,4)-(40,44). Lucide user-round informs the detached round head and paired shoulders. Preserve the source stepped arms, widening their spacing and the head gap."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ec7a6da0-b454-410a-8b8d-1cebad7fa490'
SOURCE_PATH = 'pictographic-primitives/symbol/person body 1_ec7a6da0-b454-410a-8b8d-1cebad7fa490.svg'
AUTHOR = 'gpt-6'


class PersonStandingBody(Solo48):
    icon_id = 'person-standing-body'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    categories = ("symbol",)
    aliases = ()
    keywords = ('person', 'body', 'standing', 'user', 'figure', 'human', 'member', 'people')

    def build(self) -> None:
        cx, cy, radius = 24, 11, 7
        self.add_arc('head-top', (cx-radius, cy), (cx+radius, cy), radius_x=radius)
        self.add_arc('head-bottom', (cx+radius, cy), (cx-radius, cy), radius_x=radius)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_line('left-inner',(16,44),(16,36))
        self.add_line('left-arm',(16,36),(8,36))
        self.add_arc('left-shoulder',(8,36),(16,28),radius_x=8)
        self.add_line('shoulder-top',(16,28),(32,28))
        self.add_arc('right-shoulder',(32,28),(40,36),radius_x=8)
        self.add_line('right-arm',(40,36),(32,36))
        self.add_line('right-inner',(32,36),(32,44))
        self.add_contour('body','left-inner','left-arm','left-shoulder','shoulder-top','right-shoulder','right-arm','right-inner')
