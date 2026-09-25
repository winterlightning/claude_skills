"""A two-tier pine stands on a short trunk. VRECT extremes (8,4)-(40,44); mirrored tier geometry.
Reduction: Kept the two tiers and omitted no identifying feature.
Lucide: tree-pine
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3f0937d0-e60c-4dfb-805d-b75941386342'
SOURCE_PATH = 'pictographic-primitives/nature/tree_3f0937d0-e60c-4dfb-805d-b75941386342.svg'
AUTHOR = 'gpt-6'

class PineTree(Solo48):
    icon_id = 'pine-tree'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature"
    aliases = ()
    keywords = ('pine', 'tree', 'fir', 'evergreen', 'forest', 'conifer', 'nature', 'woods')

    def build(self) -> None:
        axis=24
        left=[(axis,4),(axis-16,20),(axis-4,20),(axis-16,36),(axis,36)]
        right=[(2*axis-x,y) for x,y in reversed(left[:-1])]
        self.add_polyline('canopy',*(left+right),closed=True)
        self.add_line('trunk',(axis,36),(axis,44))
        for p in ('canopy-4','canopy-5'):self.relate('connect','trunk',p)
