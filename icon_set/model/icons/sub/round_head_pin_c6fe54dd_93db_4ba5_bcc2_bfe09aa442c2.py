"""Round-Head Pin: A long straight upright pin supports a large circular head at its upper end. The thin shaft attaches at the head's bottom centre and extends far downward.

Construction: An outlined circular head of radius 6 joins a 16-unit straight shaft, preserving the long pin proportions.
Keyshape: VRECT_S; authored to the SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'c6fe54dd-93db-4ba5-bcc2-bfe09aa442c2'
SOURCE_PATH = 'pictographic-primitives/state/pin task_c6fe54dd-93db-4ba5-bcc2-bfe09aa442c2.svg'
AUTHOR = 'gpt-6'


class RoundHeadPin(Sub32):
    icon_id = 'round-head-pin'
    keyshape = Keyshape.VRECT_S
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives/shape'
    aliases = ()
    keywords = ('round', 'head', 'pin', 'long', 'straight', 'upright', 'supports', 'large')

    def build(self):
        def circle(name,cx,cy,radius):
            self.add_arc(name+"-top",(cx-radius,cy),(cx+radius,cy),radius_x=radius)
            self.add_arc(name+"-bottom",(cx+radius,cy),(cx-radius,cy),radius_x=radius)
            self.add_contour(name,name+"-top",name+"-bottom",closed=True)
        circle('head',16,8,6)
        self.add_line('shaft',(16,14),(16,30))
        self.relate('connect','head','shaft')
