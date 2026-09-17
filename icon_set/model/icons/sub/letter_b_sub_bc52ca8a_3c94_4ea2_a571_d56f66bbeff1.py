"""Letter B: An uppercase B has a straight upright stem and two rounded bowls, with the lower bowl slightly fuller. Generate this component alone; exclude Circle Frame.

Construction: Two equal elliptical bowls share the middle crossbar and left upright.
Keyshape: VRECT_L; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'bc52ca8a-3c94-4ea2-a571-d56f66bbeff1'
SOURCE_PATH = 'pictographic-primitives/state/b text in circle_bc52ca8a-3c94-4ea2-a571-d56f66bbeff1.svg'
AUTHOR = 'gpt-6'


class LetterBSub(Sub32):
    icon_id = 'letter-b-sub'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('letter', 'b', 'uppercase', 'straight', 'upright', 'stem', 'rounded', 'bowls')

    def build(self):
        self.add_line('stem',(6,2),(6,30))
        for name,y in (('upper',2),('lower',16)):
            self.add_line(name+'-top',(6,y),(16,y))
            self.add_arc(name+'-round',(16,y),(16,y+14),radius_x=10,radius_y=7)
            self.add_line(name+'-bottom',(16,y+14),(6,y+14))
            self.add_contour(name,name+'-top',name+'-round',name+'-bottom')
            self.relate('connect','stem',name)
        self.relate('connect','upper','lower')
