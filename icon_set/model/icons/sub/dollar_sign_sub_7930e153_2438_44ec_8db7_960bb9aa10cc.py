"""Dollar Sign: A large S-shaped curve is crossed by one continuous vertical line extending beyond its top and bottom. The upper and lower bowls turn in opposite directions around the stem.

Construction: An S contour uses tangent elliptical arcs; a vertical currency stem crosses it intentionally.
Keyshape: VRECT_L; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '7930e153-2438-44ec-8db7-960bb9aa10cc'
SOURCE_PATH = 'pictographic-primitives/state/dollar sign_7930e153-2438-44ec-8db7-960bb9aa10cc.svg'
AUTHOR = 'gpt-6'


class DollarSignSub(Sub32):
    icon_id = 'dollar-sign-sub'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives-generate'
    categories = ('primitives-generate', 'state')
    aliases = ()
    keywords = ('dollar', 'sign', 'large', 's', 'shaped', 'curve', 'crossed', 'continuous')

    def build(self):
        self.add_arc("top",(26,10),(6,10),radius_x=10,radius_y=6,sweep=False)
        self.add_arc("upper-return",(6,10),(16,16),radius_x=10,radius_y=6,sweep=False)
        self.add_arc("lower-start",(16,16),(26,22),radius_x=10,radius_y=6)
        self.add_arc("bottom",(26,22),(6,22),radius_x=10,radius_y=6)
        self.add_contour("s","top","upper-return","lower-start","bottom")
        self.add_line("stem",(16,2),(16,30))
        self.relate("connect","s","stem")
