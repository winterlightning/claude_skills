# Variant of tropical-island-with-palm-tree; parent file remains unchanged.
"""Tropical island with a curved palm trunk and four arching fronds. SQUARE fits the canopy above a simple island mound. Lucide tree-palm informs the drooping canopy and leaning trunk; waves and the fifth frond were omitted. Trunk lean and island asymmetry are deliberate."""
from __future__ import annotations
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = None
SOURCE_PATH = '/Users/jakesdev/Downloads/feedback-briefs/solo/batch-05/49-tropical-island-with-palm-tree.md'
AUTHOR = 'gpt-6'

class TropicalIslandWithPalmTreeVariant2(Solo48):
    """A leaning palm with arching fronds above an island mound."""
    icon_id = 'tropical-island-with-palm-tree-v2'
    variant_of = 'tropical-island-with-palm-tree'
    variant_label = 'Clear palm and island'
    keyshape = Keyshape.SQUARE
    category = 'objects/nature'
    aliases = ('tropical-island', 'palm-tree-island', 'island-palm')
    keywords = ('island', 'palm', 'tree', 'beach', 'tropical', 'vacation', 'holiday', 'sea', 'sand', 'water')

    def build(self) -> None:
        # SQUARE centerline extremes (2,2)-(46,46).
        self.add_arc('upper-left', (24,14), (2,14), radius_x=11, radius_y=12, sweep=False)
        self.add_arc('upper-right', (24,14), (46,14), radius_x=11, radius_y=12)
        self.add_arc('lower-left', (24,14), (8,28), radius_x=16, radius_y=14, sweep=False)
        self.add_arc('lower-right', (24,14), (40,28), radius_x=16, radius_y=14)
        self.add_arc('trunk', (24,14), (28,34), radius_x=30, sweep=False)
        self.add_arc('island-left', (2,46), (28,34), radius_x=26, radius_y=12)
        self.add_arc('island-right', (28,34), (46,46), radius_x=18, radius_y=12)
        self.add_contour('island', 'island-left', 'island-right')
        fronds=['upper-left','upper-right','lower-left','lower-right']
        for i,a in enumerate(fronds):
            self.relate('connect', a, 'trunk')
            for b in fronds[i+1:]: self.relate('connect',a,b)
        self.relate('connect','trunk','island')
