"""Hanging pot with two upright leaves and two trailing stems; small side shoots omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '648d5f22-ccb1-4224-9894-c373442f1825'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-02/hanging plant 3_648d5f22-ccb1-4224-9894-c373442f1825.svg'
AUTHOR = 'gpt-6'

class TrailingHangingPlanter(Solo48):
    icon_id = 'trailing-hanging-planter'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/decoration"
    aliases = ()
    keywords = ('planter', 'hanging', 'trailing', 'vine', 'leaves', 'cord', 'plant')

    def build(self) -> None:
        # VRECT_XL: exact SOLO48 extremes; geometry authored on the integer grid.
        self.add_polyline('cords', (5, 26), (24, 2), (43, 26), closed=False)
        self.add_line('rim-left', (10, 26), (16, 26))
        self.add_line('leaf-a', (16, 26), (16, 18))
        self.add_line('leaf-b', (16, 18), (24, 24))
        self.add_line('leaf-c', (24, 24), (32, 18))
        self.add_line('leaf-d', (32, 18), (32, 26))
        self.add_line('rim-right', (32, 26), (38, 26))
        self.add_arc('bowl', (38, 26), (10, 26), radius_x=14, radius_y=12, sweep=True)
        self.add_contour('pot', 'rim-left', 'leaf-a', 'leaf-b', 'leaf-c', 'leaf-d', 'rim-right', 'bowl', closed=True)
        self.add_line('left-support', (5, 26), (10, 26))
        self.add_line('right-support', (43, 26), (38, 26))
        self.relate('connect', 'cords', 'left-support')
        self.relate('connect', 'cords', 'right-support')
        self.relate('connect', 'pot', 'left-support')
        self.relate('connect', 'pot', 'right-support')
        self.add_polyline('left-trail', (5, 26), (5, 36), (5, 46), closed=False)
        self.add_polyline('right-trail', (43, 26), (43, 36), (43, 46), closed=False)
        self.relate('connect', 'left-trail', 'left-support')
        self.relate('connect', 'right-trail', 'right-support')
        self.relate('connect', 'left-trail', 'cords')
        self.relate('connect', 'right-trail', 'cords')
