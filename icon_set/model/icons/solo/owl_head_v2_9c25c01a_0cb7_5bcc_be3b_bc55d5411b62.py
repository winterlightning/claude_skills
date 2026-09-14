# Variant of owl-head; parent file remains unchanged.
'Owl head: independent spacing revision.\n\nEnlarge diamond beak and rebalance the paired owl brows to current horizontal bounds.\nNative solo family, HRECT_XL keyshape. The original model is preserved.\nDirectional and natural asymmetry follows the supplied subject.\nFinal construction review: Original subject render; no exact Lucide match selected.\n'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9c25c01a-0cb7-5bcc-be3b-bc55d5411b62'
SOURCE_PATH = 'pictographic-primitives/animals/wild bird owl_9c25c01a-0cb7-5bcc-be3b-bc55d5411b62.svg'
AUTHOR = 'gpt-6'

class OwlHeadVariant2(Solo48):
    icon_id = 'owl-head-v2'
    variant_of = 'owl-head'
    variant_label = 'Roomier spacing — remaining review'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals/birds'
    aliases = ()
    keywords = ('owl', 'head', 'horned', 'ears', 'beak', 'night', 'bird', 'minimal')

    def build(self):
        self.add_polyline('left-ear',(4, 8),(14, 14),closed=False)
        self.add_arc('crown',(14, 14),(34, 14),radius_x=22,radius_y=12,sweep=True)
        self.add_line('right-ear',(34, 14),(44, 8))
        self.add_arc('brow-right',(44, 8),(34, 22),radius_x=24,radius_y=24,sweep=True)
        self.add_arc('cheek-right',(34, 22),(24, 28),radius_x=20,radius_y=20,sweep=False)
        self.add_arc('cheek-left',(24, 28),(14, 22),radius_x=20,radius_y=20,sweep=False)
        self.add_arc('brow-left',(14, 22),(4, 8),radius_x=24,radius_y=24,sweep=True)
        self.contours = [c for c in self.contours if c.contour_id != 'left-ear']
        self.add_contour('brows','left-ear-1','crown','right-ear','brow-right','cheek-right','cheek-left','brow-left',closed=True)
        self.add_arc('face-left',(14, 22),(8, 38),radius_x=14,radius_y=14,sweep=False)
        self.add_arc('face-right',(34, 22),(40, 38),radius_x=14,radius_y=14,sweep=True)
        self.add_polyline('beak',(24, 28),(30, 34),(24, 40),(18, 34),closed=True)
        self.relate('connect','brows','face-left')
        self.relate('connect','brows','face-right')
        self.relate('connect','brows','beak')
