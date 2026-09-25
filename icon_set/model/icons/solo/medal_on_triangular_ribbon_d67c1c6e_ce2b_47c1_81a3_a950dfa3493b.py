"""A plain circular medal hangs from an inverted triangular neck ribbon.

Live keyshape centerlines: VRECT_L (8,4)-(40,44); SQUARE (6,6)-(42,42);
HRECT_L (4,8)-(44,40). Shared dimensions preserve paired proportions.
Lucide medal: geometric construction; supplied reference: subject identity.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='d67c1c6e-ce2b-47c1-81a3-a950dfa3493b'
SOURCE_PATH='pictographic-primitives/rewards/medal_d67c1c6e-ce2b-47c1-81a3-a950dfa3493b.svg'
AUTHOR='gpt-6'

class MedalOnTriangularRibbon(Solo48):
    icon_id='medal-on-triangular-ribbon'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'rewards'
    categories = ('rewards', 'primitives')
    aliases=()
    keywords=('award', 'reward', 'medal-on-triangular-ribbon')
    def build(self) -> None:
        self.add_arc('disc-right',(24,18),(37,31),radius_x=13)
        self.add_arc('disc-bottom',(37,31),(11,31),radius_x=13)
        self.add_arc('disc-left',(11,31),(24,18),radius_x=13)
        self.add_contour('medal','disc-right','disc-bottom','disc-left',closed=True)
        self.add_polyline('ribbon',(24,18),(8,4),(40,4),(24,18))
        self.relate('connect','medal','ribbon')
