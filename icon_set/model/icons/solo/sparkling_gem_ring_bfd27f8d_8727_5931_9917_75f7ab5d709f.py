"""A round gem above a ring band with two glints; band thickness reduced to one stroke.

Construction references: Lucide rose, heart, gem and hand as applicable.
SOLO48 live-contract centerline bounds: VRECT_L (8,4)-(40,44),
HRECT_L (4,8)-(44,40), SQUARE (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bfd27f8d-8727-5931-9917-75f7ab5d709f'
SOURCE_PATH = 'pictographic-primitives/romance/diamond ring_bfd27f8d-8727-5931-9917-75f7ab5d709f.svg'
AUTHOR = 'gpt-6'


class SparklingGemRing(Solo48):
    icon_id = 'sparkling-gem-ring'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "romance"
    aliases = ()
    keywords = ('ring', 'gem', 'jewelry', 'sparkle', 'engagement', 'romance')

    def build(self) -> None:
        self.add_arc('gem-a',(24,6),(24,18),radius_x=6)
        self.add_arc('gem-b',(24,18),(24,6),radius_x=6)
        self.add_contour('gem','gem-a','gem-b',closed=True)
        self.add_arc('band-r',(24,18),(24,42),radius_x=12)
        self.add_arc('band-l',(24,42),(24,18),radius_x=12)
        self.add_contour('band','band-r','band-l',closed=True)
        self.relate('connect','gem','band')
        for n,x in [('left',8),('right',40)]:
            self.add_line(n+'-h',(x-2,10),(x+2,10))
            self.add_line(n+'-v',(x,8),(x,12))
            self.relate('connect',n+'-h',n+'-v')
