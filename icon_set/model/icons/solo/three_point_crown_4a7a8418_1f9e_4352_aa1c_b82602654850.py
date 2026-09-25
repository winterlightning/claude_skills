"""A three-point crown with tall center and a detached lower band.
Live centerline extremes: SQUARE (6,6)-(42,42); HRECT_L (4,8)-(44,40);
VRECT_L (8,4)-(40,44). Lucide crown informs construction, source sets subject.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='4a7a8418-1f9e-4352-aa1c-b82602654850'
SOURCE_PATH='pictographic-primitives/rewards/vip crown king_4a7a8418-1f9e-4352-aa1c-b82602654850.svg'
AUTHOR='gpt-6'
class ThreePointCrown(Solo48):
    icon_id='three-point-crown'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'rewards'
    categories = ('rewards', 'primitives')
    aliases=()
    keywords=('reward','celebration','three-point-crown')
    def build(self) -> None:
        self.add_polyline('crown',(4,16),(14,24),(24,8),(34,24),(44,16),(38,32),(10,32),closed=True)
        self.add_line('band',(10,40),(38,40))
