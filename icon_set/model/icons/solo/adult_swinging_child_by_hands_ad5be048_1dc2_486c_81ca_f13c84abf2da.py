"A standing adult bends slightly while holding both hands of a smaller child. The child's body stretches almost horizontally to the right, with the legs bent upward during the swing.\n\nConstruction: Standing adult grips a small child whose torso and legs swing horizontally. Bounds (4,8)-(44,40).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used."
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ad5be048-1dc2-486c-81ca-f13c84abf2da'
SOURCE_PATH = 'pictographic-primitives/wayfinding/family child play_ad5be048-1dc2-486c-81ca-f13c84abf2da.svg'
AUTHOR = 'gpt-6'

class AdultSwingingChildByHands(Solo48):
    icon_id = 'adult-swinging-child-by-hands'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    aliases = ()
    keywords = ('adult', 'child', 'play', 'swinging', 'hands', 'family')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_arc('adult-head-top', (9, 11), (15, 11), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('adult-head-bottom', (15, 11), (9, 11), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('adult-body-1', (10, 23), (8, 31))
        self.add_line('adult-body-2', (8, 31), (4, 40))
        self.add_line('adult-arm-1', (10, 23), (22, 27))
        self.add_line('adult-leg-1', (8, 31), (14, 40))
        self.add_arc('child-head-top', (30, 18), (34, 18), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('child-head-bottom', (34, 18), (30, 18), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('child-body-1', (22, 27), (30, 30))
        self.add_line('child-body-2', (30, 30), (38, 28))
        self.add_line('child-body-3', (38, 28), (44, 34))
        self.add_contour('adult-head', 'adult-head-top', 'adult-head-bottom', closed=True)
        self.add_contour('adult-body', 'adult-body-1', 'adult-body-2', closed=False)
        self.add_contour('adult-arm', 'adult-arm-1', closed=False)
        self.add_contour('adult-leg', 'adult-leg-1', closed=False)
        self.add_contour('child-head', 'child-head-top', 'child-head-bottom', closed=True)
        self.add_contour('child-body', 'child-body-1', 'child-body-2', 'child-body-3', closed=False)
        self.relate('connect', 'adult-body', 'adult-arm')
        self.relate('connect', 'adult-body', 'adult-leg')
        self.relate('connect', 'adult-arm', 'child-body')
