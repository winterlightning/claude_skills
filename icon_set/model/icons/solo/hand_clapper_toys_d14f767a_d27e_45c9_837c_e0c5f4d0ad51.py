# Repair: Build two broad toy hands from the same rounded shape, with eight-unit spacing and crossed handles.
"""Two hand-shaped clapper heads above crossed handles; reduce finger notches and omit motion ticks.
Live centerline extremes: SQUARE (6,6)-(42,42); HRECT_L (4,8)-(44,40);
VRECT_L (8,4)-(40,44). Lucide hand informs construction, source sets subject.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='d14f767a-d27e-45c9-837c-e0c5f4d0ad51'
SOURCE_PATH='pictographic-primitives/rewards/reward claps hand stick_d14f767a-d27e-45c9-837c-e0c5f4d0ad51.svg'
AUTHOR = 'gpt-6'
class HandClapperToys(Solo48):
    icon_id='hand-clapper-toys'
    keyshape = Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'rewards'
    aliases=()
    keywords=('reward','celebration','hand-clapper-toys')
    def build(self):
        from ._symmetry_curves import path, ellipse, line, poly, contacts

        for j,cx in enumerate((12,36)):
            path(self,f'hand-{j}',(cx-8,12),('A',4,4,True,(cx,12)),('A',4,4,True,(cx+8,12)),('L',(cx+8,24)),('A',8,8,True,(cx,32)),('A',8,8,True,(cx-8,24)),('L',(cx-8,12)),closed=True)
            line(self,f'finger-{j}',(cx,12),(cx,20))
        line(self,'handle-left',(12,32),(32,40))
        line(self,'handle-right',(36,32),(16,40))
        contacts(self)
        self.relate('connect','handle-left','handle-right')
