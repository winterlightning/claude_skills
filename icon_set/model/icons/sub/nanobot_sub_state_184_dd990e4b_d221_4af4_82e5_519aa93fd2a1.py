"""Nanobot: A tall hexagonal body has gently rounded corners and a round central opening. Two curved claw-like appendages extend from the lower sides and bend outward before turning inward at their tips.

Construction: A hexagonal robot retains its outlined central opening and paired open claws.
Keyshape: SQUARE; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'dd990e4b-d221-4af4-82e5-519aa93fd2a1'
SOURCE_PATH = 'pictographic-primitives/state/nanobot_dd990e4b-d221-4af4-82e5-519aa93fd2a1.svg'
AUTHOR = 'gpt-6'


class NanobotSubState184(Sub32):
    icon_id = 'nanobot-sub-state-184'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives/shape'
    aliases = ()
    keywords = ('nanobot', 'tall', 'hexagonal', 'body', 'gently', 'rounded', 'corners', 'round')

    def build(self):
        def circle(name,cx,cy,radius):
            self.add_arc(name+"-top",(cx-radius,cy),(cx+radius,cy),radius_x=radius)
            self.add_arc(name+"-bottom",(cx+radius,cy),(cx-radius,cy),radius_x=radius)
            self.add_contour(name,name+"-top",name+"-bottom",closed=True)
        self.add_polyline('body',(16,2),(26,8),(26,20),(16,26),(6,20),(6,8),closed=True)
        circle('opening',16,13,3)
        self.add_arc('left-claw',(6,20),(6,30),radius_x=4,radius_y=5,sweep=False)
        self.add_arc('right-claw',(26,20),(26,30),radius_x=4,radius_y=5)
        self.relate('connect','body','left-claw')
        self.relate('connect','body','right-claw')
