"""A broad three-lobed cloud canopy on a straight trunk. VRECT extremes (8,4)-(40,44); equal side lobes.
Reduction: Kept the complete simple silhouette.
Lucide: tree-deciduous, cloud
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7c2bb3d8-d265-584e-a679-91099162614b'
SOURCE_PATH = 'pictographic-primitives/nature/tree cloud_7c2bb3d8-d265-584e-a679-91099162614b.svg'
AUTHOR = 'gpt-6'

class CloudShapedTree(Solo48):
    icon_id = 'cloud-shaped-tree'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/batch-03"
    aliases = ()
    keywords = ('tree', 'canopy', 'cloud', 'park', 'nature', 'outdoors', 'forest', 'shade')

    def build(self) -> None:
        axis=24;r=8
        self.add_arc('top',(axis-r,12),(axis+r,12),radius_x=r)
        self.add_arc('right',(axis+r,12),(axis+r,28),radius_x=r)
        self.add_line('base-right',(axis+r,28),(axis,28));self.add_line('base-left',(axis,28),(axis-r,28))
        self.add_arc('left',(axis-r,28),(axis-r,12),radius_x=r)
        self.add_contour('canopy','top','right','base-right','base-left','left',closed=True)
        self.add_line('trunk',(axis,28),(axis,44))
        for p in ('base-right','base-left'): self.relate('connect','trunk',p)
