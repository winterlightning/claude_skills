"""Remove the pinched inner leaf triangles and leave a generous open suspension above the bowl. Applied to the original icon identity."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '648d5f22-ccb1-4224-9894-c373442f1825'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-02/hanging plant 3_648d5f22-ccb1-4224-9894-c373442f1825.svg'
AUTHOR = 'gpt-6'

class TrailingHangingPlanter(Solo48):
    icon_id = 'trailing-hanging-planter'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/decoration'
    aliases = ()
    keywords = ('planter', 'hanging', 'trailing', 'vine', 'leaves', 'cord', 'plant')

    def build(self) -> None:
        """Symbol plan: Remove the pinched inner leaf triangles and leave a generous open suspension above the bowl. Reference: inspected current parent; no useful exact Lucide match selected."""
        self.add_polyline('cords', (8, 32), (24, 4), (40, 32), closed=False)
        self.add_line('rim-left', (17, 32), (31, 32))
        self.add_arc('bowl', (31, 32), (17, 32), radius_x=7, radius_y=12, sweep=True)
        self.add_line('left-support', (8, 32), (17, 32))
        self.add_line('right-support', (40, 32), (31, 32))
        self.relate('connect', 'cords', 'left-support')
        self.relate('connect', 'cords', 'right-support')
        self.add_polyline('left-trail', (8, 32), (8, 44), closed=False)
        self.add_polyline('right-trail', (40, 32), (40, 44), closed=False)
        self.relate('connect', 'left-trail', 'left-support')
        self.relate('connect', 'right-trail', 'right-support')
        self.relate('connect', 'left-trail', 'cords')
        self.relate('connect', 'right-trail', 'cords')
        self.add_contour('pot', 'rim-left', 'bowl', closed=True)
        self.relate('connect', 'pot', 'left-support')
        self.relate('connect', 'pot', 'right-support')
