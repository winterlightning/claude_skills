"""Separate the two ribbon tails with a clear central notch and broaden their ends; remove the narrow diamond trapped under the flower.
Independent centerline revision; original snapshot preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '58f87e29-b0b5-42be-b412-f3b9d5882e0e'
SOURCE_PATH = 'pictographic-primitives/symbol/award flower shape_58f87e29-b0b5-42be-b412-f3b9d5882e0e.svg'
AUTHOR = 'gpt-6'

class AwardFlowerRosette(Solo48):
    icon_id = 'award-flower-rosette-centerline-v2'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbols/standalone'
    aliases = ()
    keywords = ('award', 'rosette', 'badge', 'prize', 'ribbon', 'medal', 'winner', 'achievement')

    def build(self) -> None:
        self.add_arc('top', (18, 10), (30, 10), radius_x=6, radius_y=6, sweep=True)
        self.add_arc('ne-outer', (30, 10), (40, 16), radius_x=10, radius_y=6, sweep=True)
        self.add_arc('ne-inner', (40, 16), (36, 20), radius_x=4, radius_y=4, sweep=True)
        self.add_arc('se-inner', (36, 20), (40, 24), radius_x=4, radius_y=4, sweep=True)
        self.add_arc('se-outer', (40, 24), (30, 30), radius_x=10, radius_y=6, sweep=True)
        self.add_arc('bottom', (30, 30), (18, 30), radius_x=6, radius_y=4, sweep=True)
        self.add_arc('sw-outer', (18, 30), (8, 24), radius_x=10, radius_y=6, sweep=True)
        self.add_arc('sw-inner', (8, 24), (12, 20), radius_x=4, radius_y=4, sweep=True)
        self.add_arc('nw-inner', (12, 20), (8, 16), radius_x=4, radius_y=4, sweep=True)
        self.add_arc('nw-outer', (8, 16), (18, 10), radius_x=10, radius_y=6, sweep=True)
        self.add_contour('rosette', 'top', 'ne-outer', 'ne-inner', 'se-inner', 'se-outer', 'bottom', 'sw-outer', 'sw-inner', 'nw-inner', 'nw-outer', closed=True)
        self.add_arc('center-ring-right', (24, 17), (24, 23), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('center-ring-left', (24, 23), (24, 17), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('center-ring', 'center-ring-right', 'center-ring-left', closed=True)
        self.add_polyline('ribbon-left', (18, 30), (10, 44), (19, 42))
        self.add_polyline('ribbon-right', (30, 30), (38, 44), (29, 42))
        self.relate('connect', 'rosette', 'ribbon-left')
        self.relate('connect', 'rosette', 'ribbon-right')
    variant_of = 'award-flower-rosette'
    variant_label = 'Batch 01 centerline repair'
