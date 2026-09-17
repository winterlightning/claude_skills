"""Location Pin: A map pin has a rounded upper body tapering evenly into a sharp downward point. A small circular opening sits inside the upper half, centred beneath the crown.

Construction: A round upper pin narrows into its downward point; its centred outlined hole is retained.
Keyshape: CIRCLE; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '9e99a5ab-bfd4-40df-ab71-0932992ba881'
SOURCE_PATH = 'pictographic-primitives/state/location pin_9e99a5ab-bfd4-40df-ab71-0932992ba881.svg'
AUTHOR = 'gpt-6'


class LocationPinSubState150(Sub32):
    icon_id = 'location-pin-sub-state-150'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives/shape'
    aliases = ()
    keywords = ('location', 'pin', 'map', 'rounded', 'upper', 'body', 'tapering', 'evenly')

    def build(self):
        def circle(name,cx,cy,radius):
            self.add_arc(name+"-top",(cx-radius,cy),(cx+radius,cy),radius_x=radius)
            self.add_arc(name+"-bottom",(cx+radius,cy),(cx-radius,cy),radius_x=radius)
            self.add_contour(name,name+"-top",name+"-bottom",closed=True)
        self.add_arc('crown',(5,13),(27,13),radius_x=11)
        self.add_arc('right-taper',(27,13),(16,30),radius_x=24)
        self.add_arc('left-taper',(16,30),(5,13),radius_x=24)
        self.add_contour('outline','crown','right-taper','left-taper',closed=True)
        circle('hole',16,13,4)
