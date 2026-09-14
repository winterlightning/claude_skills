"""A seated wheelchair user holds a flag to the right; preserve intentional directional asymmetry.

Live keyshape centerlines: VRECT_L (8,4)-(40,44); SQUARE (6,6)-(42,42);
HRECT_L (4,8)-(44,40). Shared dimensions preserve paired proportions.
Lucide accessibility and flag: geometric construction; supplied reference: subject identity.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='8df4cee4-a586-5de1-9d67-5a1d7d4a0bfe'
SOURCE_PATH='pictographic-primitives/rewards/flag_8df4cee4-a586-5de1-9d67-5a1d7d4a0bfe.svg'
AUTHOR='gpt-6'

class WheelchairUserHoldingAFlag(Solo48):
    icon_id='wheelchair-user-holding-a-flag'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/award'
    aliases=()
    keywords=('award', 'reward', 'wheelchair-user-holding-a-flag')
    def build(self) -> None:
        self.add_arc('head-right',(14,6),(14,12),radius_x=3)
        self.add_arc('head-left',(14,12),(14,6),radius_x=3)
        self.add_contour('head','head-right','head-left',closed=True)
        self.add_arc('wheel-left',(16,22),(16,42),radius_x=10)
        self.add_arc('wheel-right',(16,42),(16,22),radius_x=10)
        self.add_contour('wheel','wheel-left','wheel-right',closed=True)
        self.add_polyline('person',(16,22),(16,30),(30,30),(36,40),(42,40))
        self.add_polyline('arm',(16,22),(30,22),(32,18))
        self.relate('connect','wheel','person')
        self.relate('connect','wheel','arm')
        self.relate('connect','person','arm')
        self.add_line('pole',(32,26),(32,18))
        self.add_polyline('flag',(32,18),(32,6),(42,6),(42,16),(32,16))
        self.relate('connect','pole','arm')
        self.relate('connect','pole','flag')
        self.relate('connect','arm','flag')
