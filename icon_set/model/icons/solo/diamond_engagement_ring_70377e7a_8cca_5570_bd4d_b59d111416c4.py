"""A broad diamond sits on an arched ring band; minor triangular facets omitted.

Construction references: Lucide rose, heart, gem and hand as applicable.
SOLO48 live-contract centerline bounds: VRECT_L (8,4)-(40,44),
HRECT_L (4,8)-(44,40), SQUARE (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '70377e7a-8cca-5570-bd4d-b59d111416c4'
SOURCE_PATH = 'pictographic-primitives/romance/engagement ring_70377e7a-8cca-5570-bd4d-b59d111416c4.svg'
AUTHOR = 'gpt-6'


class DiamondEngagementRing(Solo48):
    icon_id = 'diamond-engagement-ring'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "romance"
    categories = ("primitives", "romance")
    aliases = ()
    keywords = ('diamond', 'ring', 'engagement', 'jewelry', 'gem', 'wedding')

    def build(self) -> None:
        self.add_polyline('gem',(14,8),(34,8),(40,18),(24,28),(8,18),closed=True)
        self.add_line('facet',(8,18),(40,18))
        self.relate('connect','gem','facet')
        self.add_arc('band-l',(4,40),(24,28),radius_x=20,radius_y=12)
        self.add_arc('band-r',(24,28),(44,40),radius_x=20,radius_y=12)
        self.add_contour('band','band-l','band-r')
        self.relate('connect','gem','band')
