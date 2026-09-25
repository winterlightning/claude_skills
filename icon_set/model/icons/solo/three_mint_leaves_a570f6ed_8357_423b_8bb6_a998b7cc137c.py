"""Three pointed mint leaves fan from a shared stem. SQUARE extremes 6..42.
Symmetry x24, leaf perimeter owns shared attachment nodes. Omit tiny serrations and
branching veins; retain three pointed leaves and central tall leaf. Lucide leaf
teaches coherent tapered curves; source supplies three-leaf fan arrangement.
"""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID='a570f6ed-8357-423b-8bb6-a998b7cc137c'
SOURCE_PATH='pictographic-primitives/_uncategorized_27/mint_a570f6ed-8357-423b-8bb6-a998b7cc137c.svg'
AUTHOR='gpt-6-astra'
class Drawing(Solo48):
    icon_id='three-mint-leaves'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    aliases=('mint sprig',)
    keywords=('mint','leaves','herb','plant','botanical','foliage')
    def build(self):
        for side,sign in [('left',-1),('right',1)]:
            x=lambda n:24+sign*n
            self.add_bezier(f'upper-{side}',(24,6),((x(7),12),(x(9),18),(x(8),24)))
            self.add_bezier(f'lower-{side}',(x(8),24),((x(7),29),(x(4),33),(24,36)))
            self.add_bezier(f'outer-{side}',(x(8),24),((x(11),21),(x(15),21),(x(18),22)),((x(18),36),(x(9),42),(24,42)))
            self.relate('connect',f'upper-{side}',f'lower-{side}',f'outer-{side}')
        self.add_line('stem',(24,36),(24,42))
        self.relate('connect','upper-left','upper-right')
        self.relate('connect','lower-left','lower-right','stem')
        self.relate('connect','outer-left','outer-right','stem')
