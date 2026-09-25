"""A round canopy encloses a forked trunk. VRECT extremes (8,4)-(40,44); paired branches share a central junction.
Reduction: Smoothed the three-lobed canopy to a broad oval to make room for branches.
Lucide: tree-deciduous
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '40067bd5-d36d-55f3-85e2-1e023ada9bcd'
SOURCE_PATH = 'pictographic-primitives/nature/tree_40067bd5-d36d-55f3-85e2-1e023ada9bcd.svg'
AUTHOR = 'gpt-6'

class DeciduousTreeWithBranches(Solo48):
    icon_id = 'deciduous-tree-with-branches'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature"
    aliases = ()
    keywords = ('tree', 'deciduous', 'oak', 'canopy', 'forest', 'park', 'nature', 'branches')

    def build(self) -> None:
        a=24
        self.add_arc('canopy-right',(a,4),(a,36),radius_x=16)
        self.add_arc('canopy-left',(a,36),(a,4),radius_x=16)
        self.add_contour('canopy','canopy-right','canopy-left',closed=True)
        self.add_line('trunk-upper',(a,16),(a,26));self.add_line('trunk-middle',(a,26),(a,36));self.add_line('trunk-bottom',(a,36),(a,44))
        self.add_polyline('branches',(18,20),(a,26),(30,20))
        for j in (1,2):
         for p in ('trunk-upper','trunk-middle'):self.relate('connect',f'branches-{j}',p)
        for p in ('canopy-right','canopy-left'):
         for s in ('trunk-middle','trunk-bottom'):self.relate('connect',s,p)
