"""A narrow pine and round deciduous tree stand together. HRECT extremes (4,8)-(44,40); unequal canopies keep the two species distinct.
Reduction: Removed overlapping outlines and internal branches.
Lucide: tree-pine, tree-deciduous
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0e3bb7df-114a-4b61-b796-cd96465aaa7b'
SOURCE_PATH = 'pictographic-primitives/nature/tree two_0e3bb7df-114a-4b61-b796-cd96465aaa7b.svg'
AUTHOR = 'gpt-6'

class PineAndRoundTree(Solo48):
    icon_id = 'pine-and-round-tree'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/batch-03"
    aliases = ()
    keywords = ('trees', 'pine', 'forest', 'park', 'woods', 'nature', 'outdoors', 'ecology')

    def build(self) -> None:
        self.add_polyline('pine',(4,32),(12,8),(20,32),(12,32),closed=True)
        self.add_line('pine-trunk',(12,32),(12,40))
        for p in ('pine-3','pine-4'):self.relate('connect','pine-trunk',p)
        x,y,r=36,22,8
        self.add_arc('round-right',(x,y-r),(x,y+r),radius_x=r)
        self.add_arc('round-left',(x,y+r),(x,y-r),radius_x=r)
        self.add_contour('round','round-right','round-left',closed=True)
        self.add_line('round-trunk',(x,y+r),(x,40))
        for p in ('round-right','round-left'):self.relate('connect','round-trunk',p)
