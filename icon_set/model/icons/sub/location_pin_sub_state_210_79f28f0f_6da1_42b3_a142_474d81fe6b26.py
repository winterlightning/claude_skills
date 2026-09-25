"""Location Pin: A rounded map pin tapers into a pointed lower tip. A circular opening is centred within its broad upper portion, following the same upright alignment as the outer shape.

Construction: A round upper pin narrows into its downward point; its centred outlined hole is retained.
Keyshape: CIRCLE; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '79f28f0f-6da1-42b3-a142-474d81fe6b26'
SOURCE_PATH = 'pictographic-primitives/state/pin wave_79f28f0f-6da1-42b3-a142-474d81fe6b26.svg'
AUTHOR = 'gpt-6'


class LocationPinSubState210(Sub32):
    icon_id = 'location-pin-sub-state-210'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('location', 'pin', 'rounded', 'map', 'tapers', 'pointed', 'lower', 'tip')

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
