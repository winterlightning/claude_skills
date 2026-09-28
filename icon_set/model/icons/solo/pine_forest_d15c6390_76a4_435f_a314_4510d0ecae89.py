"""Three pines form one forest canopy with a taller central peak and three trunks. HRECT centerline extremes (4,8)-(44,40); side trees mirror about x=24.
Reduction: Merged overlapping canopy outlines and removed small notched tiers while retaining all three trees.
Lucide: tree-pine
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd15c6390-76a4-435f-a314-4510d0ecae89'
SOURCE_PATH = 'pictographic-primitives/nature/wild harvested_d15c6390-76a4-435f-a314-4510d0ecae89.svg'
AUTHOR = 'gpt-6'

class PineForest(Solo48):
    icon_id = 'pine-forest'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature"
    categories = ("nature", "primitives")
    aliases = ()
    keywords = ('pine', 'forest', 'trees', 'woods', 'evergreen', 'wild', 'nature', 'outdoors')

    def build(self) -> None:
        a=24
        left=[(4,34),(10,16),(16,26),(a,8)]
        right=[(2*a-x,y) for x,y in reversed(left[:-1])]
        base=[(38,34),(24,34),(10,34)]
        self.add_polyline('canopy',*(left+right+base),closed=True)
        for n,x in enumerate((10,24,38)):
         self.add_line(f'trunk-{n}',(x,34),(x,40))
         for j in ({10:(9,10),24:(8,9),38:(7,8)}[x]):self.relate('connect',f'trunk-{n}',f'canopy-{j}')
