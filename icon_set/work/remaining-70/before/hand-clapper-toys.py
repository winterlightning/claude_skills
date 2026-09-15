"""Two hand-shaped clapper heads above crossed handles; reduce finger notches and omit motion ticks.
Live centerline extremes: SQUARE (6,6)-(42,42); HRECT_L (4,8)-(44,40);
VRECT_L (8,4)-(40,44). Lucide hand informs construction, source sets subject.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='d14f767a-d27e-45c9-837c-e0c5f4d0ad51'
SOURCE_PATH='pictographic-primitives/rewards/reward claps hand stick_d14f767a-d27e-45c9-837c-e0c5f4d0ad51.svg'
AUTHOR='gpt-6'
class HandClapperToys(Solo48):
    icon_id='hand-clapper-toys'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/award'
    aliases=()
    keywords=('reward','celebration','hand-clapper-toys')
    def build(self) -> None:
        for side,sign in [('left',-1),('right',1)]:
            def p(x,y): return (24+sign*x,y)
            self.add_polyline(side+'-palm',p(6,30),p(14,28),p(18,24),p(18,18),p(12,22),p(14,10))
            self.add_arc(side+'-finger',p(14,10),p(6,10),radius_x=4,sweep=sign==-1)
            self.add_polyline(side+'-inside',p(6,10),p(6,18),p(2,14),p(0,20),p(2,28),p(6,30))
            self.relate('connect',side+'-palm',side+'-finger')
            self.relate('connect',side+'-finger',side+'-inside')
            self.relate('connect',side+'-palm',side+'-inside')
        self.add_line('handle-right',(18,30),(32,42))
        self.add_line('handle-left',(30,30),(16,42))
        self.relate('connect','left-inside','right-inside')
        self.relate('connect','left-palm','handle-right')
        self.relate('connect','left-inside','handle-right')
        self.relate('connect','right-palm','handle-left')
        self.relate('connect','right-inside','handle-left')
        self.relate('connect','handle-right','handle-left')
