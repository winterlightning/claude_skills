"""A looped awareness ribbon forms the body of a butterfly with paired scalloped wings.

Live keyshape centerlines: VRECT_L (8,4)-(40,44); SQUARE (6,6)-(42,42);
HRECT_L (4,8)-(44,40). Shared dimensions preserve paired proportions.
Lucide ribbon (loop and crossing); source supplies butterfly wings: geometric construction; supplied reference: subject identity.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='a0d5db3d-81f0-4556-bcaf-7ec67b1e7ff1'
SOURCE_PATH='pictographic-primitives/rewards/down syndrome butterfly ribbin_a0d5db3d-81f0-4556-bcaf-7ec67b1e7ff1.svg'
AUTHOR='gpt-6'

class ButterflyAwarenessRibbon(Solo48):
    icon_id='butterfly-awareness-ribbon'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'rewards'
    categories = ('rewards', 'primitives')
    aliases=()
    keywords=('award', 'reward', 'butterfly-awareness-ribbon')
    def build(self) -> None:
        self.add_arc('ribbon-loop',(18,14),(30,14),radius_x=6,radius_y=8)
        self.add_line('tail-right-1',(30,14),(18,42))
        self.add_polyline('tail-left',(18,14),(30,42))
        self.add_contour('ribbon','ribbon-loop','tail-right-1')
        self.relate('connect','ribbon','tail-left')
        for side,sign in [('left',-1),('right',1)]:
            def p(x,y): return (24+sign*x,y)
            self.add_arc(side+'-upper',p(6,14),p(18,14),radius_x=6,radius_y=8,sweep=sign==1)
            self.add_arc(side+'-shoulder',p(18,14),p(12,26),radius_x=6,radius_y=12,sweep=sign==1)
            self.add_arc(side+'-lower',p(12,26),p(6,36),radius_x=6,radius_y=7,sweep=sign==1)
            self.add_contour(side+'-wing',side+'-upper',side+'-shoulder',side+'-lower')
            self.relate('connect',side+'-wing','ribbon')
            if side=='left': self.relate('connect',side+'-wing','tail-left')
