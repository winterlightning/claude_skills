# Variant of trailing-hanging-planter; parent file remains unchanged.
"""Hanging planter with leaves lowered to enlarge the triangular openings inside the hanger. VRECT_XL preserves hanging proportions. Lucide sprout informed simple leaf construction; paired geometry stays mirrored."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '648d5f22-ccb1-4224-9894-c373442f1825'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-02/hanging plant 3_648d5f22-ccb1-4224-9894-c373442f1825.svg'
AUTHOR = 'gpt-6'

class TrailingHangingPlanterVariant2(Solo48):
    icon_id = 'trailing-hanging-planter-v2'
    variant_of = 'trailing-hanging-planter'
    variant_label = 'Open hanger gaps'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/decoration'
    aliases = ()
    keywords = ('planter', 'hanging', 'trailing', 'vine', 'leaves', 'cord', 'plant')

    def build(self) -> None:
        self.add_polyline('cords', (5, 32), (24, 2), (43, 32), closed=False)
        self.add_line('rim-left', (10, 32), (16, 32))
        self.add_line('leaf-a', (16, 32), (16, 24))
        self.add_line('leaf-b', (16, 24), (24, 30))
        self.add_line('leaf-c', (24, 30), (32, 24))
        self.add_line('leaf-d', (32, 24), (32, 32))
        self.add_line('rim-right', (32, 32), (38, 32))
        self.add_arc('bowl', (38, 32), (10, 32), radius_x=14, radius_y=12, sweep=True)
        self.add_contour('pot', 'rim-left', 'leaf-a', 'leaf-b', 'leaf-c', 'leaf-d', 'rim-right', 'bowl', closed=True)
        self.add_line('left-support', (5, 32), (10, 32))
        self.add_line('right-support', (43, 32), (38, 32))
        self.relate('connect', 'cords', 'left-support')
        self.relate('connect', 'cords', 'right-support')
        self.relate('connect', 'pot', 'left-support')
        self.relate('connect', 'pot', 'right-support')
        self.add_polyline('left-trail', (5, 32), (5, 36), (5, 46), closed=False)
        self.add_polyline('right-trail', (43, 32), (43, 36), (43, 46), closed=False)
        self.relate('connect', 'left-trail', 'left-support')
        self.relate('connect', 'right-trail', 'right-support')
        self.relate('connect', 'left-trail', 'cords')
        self.relate('connect', 'right-trail', 'cords')
