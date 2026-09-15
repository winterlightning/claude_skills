"""Three pointed petals and a short stem. VRECT extremes (8,4)-(40,44); mirrored tips about x=24.
Reduction: Removed the overlapping inner petal seams.
Lucide: flower-2, leaf
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f054426c-e4b8-4451-ab96-7545c1e2315b'
SOURCE_PATH = 'pictographic-primitives/nature/plant_f054426c-e4b8-4451-ab96-7545c1e2315b.svg'
AUTHOR = 'gpt-6'

class ThreePetalBudUpright(Solo48):
    icon_id = 'three-petal-bud-upright'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/batch-03"
    aliases = ()
    keywords = ('bud', 'plant', 'petals', 'lotus', 'flower', 'growth', 'nature', 'botanical')

    def build(self) -> None:
        axis=24
        left,right=axis-16,axis+16
        self.add_line('left-tip',(left,12),(axis-6,18))
        self.add_arc('center-left',(axis-6,18),(axis,4),radius_x=20)
        self.add_arc('center-right',(axis,4),(axis+6,18),radius_x=20)
        self.add_line('right-tip',(axis+6,18),(right,12))
        self.add_arc('bowl-right',(right,12),(axis,36),radius_x=16,radius_y=24)
        self.add_arc('bowl-left',(axis,36),(left,12),radius_x=16,radius_y=24)
        self.add_contour('bud','left-tip','center-left','center-right','right-tip','bowl-right','bowl-left',closed=True)
        self.add_line('stem',(axis,36),(axis,44))
        for part in ('bowl-right','bowl-left'): self.relate('connect','stem',part)
