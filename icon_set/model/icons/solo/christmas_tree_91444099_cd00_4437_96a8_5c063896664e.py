"""Tiered fir silhouette and a short trunk. VRECT extremes (8,4)-(40,44); mirrored side steps about x=24.
Reduction: Reduced three tiers to two broad tiers.
Lucide: tree-pine
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '91444099-cd00-4437-96a8-5c063896664e'
SOURCE_PATH = 'pictographic-primitives/nature/tree christmas_91444099-cd00-4437-96a8-5c063896664e.svg'
AUTHOR = 'gpt-6'

class ChristmasTree(Solo48):
    icon_id = 'christmas-tree'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature"
    categories = ("nature", "primitives")
    aliases = ()
    keywords = ('christmas', 'tree', 'fir', 'pine', 'holiday', 'evergreen', 'winter', 'festive')

    def build(self) -> None:
        axis=24
        left=[(axis,4),(axis-16,20),(axis-4,20),(axis-16,36),(axis,36)]
        right=[(2*axis-x,y) for x,y in reversed(left[:-1])]
        self.add_polyline('canopy',*(left+right),closed=True)
        self.add_line('trunk',(axis,36),(axis,44))
        for p in ('canopy-4','canopy-5'):self.relate('connect','trunk',p)
