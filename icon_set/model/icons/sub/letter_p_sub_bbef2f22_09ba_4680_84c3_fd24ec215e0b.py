"""Letter P: An uppercase P has a straight upright stem with one rounded bowl attached to its upper half. Generate this component alone; exclude Circle Frame.

Construction: An upright joins a half-elliptical upper bowl at its top and midpoint.
Keyshape: VRECT_L; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'bbef2f22-09ba-4680-84c3-fd24ec215e0b'
SOURCE_PATH = 'pictographic-primitives/state/circle p_bbef2f22-09ba-4680-84c3-fd24ec215e0b.svg'
AUTHOR = 'gpt-6'


class LetterPSub(Sub32):
    icon_id = 'letter-p-sub'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('letter', 'p', 'uppercase', 'straight', 'upright', 'stem', 'rounded', 'bowl')

    def build(self):
        self.add_line('stem',(6,2),(6,30))
        self.add_line('top',(6,2),(16,2))
        self.add_arc('round',(16,2),(16,18),radius_x=10,radius_y=8)
        self.add_line('middle',(16,18),(6,18))
        self.add_contour('bowl','top','round','middle')
        self.relate('connect','stem','bowl')
