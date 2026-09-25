"""A two-tier pine stands on a short trunk. VRECT extremes (8,4)-(40,44); mirrored tier geometry.
Reduction: Kept the two tiers and omitted no identifying feature.
Lucide: tree-pine
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '66e32e15-544c-4dc8-bd51-99f96d8c78b2'
SOURCE_PATH = 'pictographic-primitives/nature/tree_66e32e15-544c-4dc8-bd51-99f96d8c78b2.svg'
AUTHOR = 'gpt-6'

class PineTreeUpright(Solo48):
    icon_id = 'pine-tree-upright'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature"
    categories = ("nature", "primitives")
    aliases = ()
    keywords = ('pine', 'tree', 'fir', 'evergreen', 'forest', 'conifer', 'nature', 'woods')

    def build(self) -> None:
        axis=24
        left=[(axis,4),(axis-16,20),(axis-4,20),(axis-16,36),(axis,36)]
        right=[(2*axis-x,y) for x,y in reversed(left[:-1])]
        self.add_polyline('canopy',*(left+right),closed=True)
        self.add_line('trunk',(axis,36),(axis,44))
        for p in ('canopy-4','canopy-5'):self.relate('connect','trunk',p)
