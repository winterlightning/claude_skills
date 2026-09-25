'An upright vacuum has a curved grip above a tall tapered body and a broad low floor head. A short slanted support joins the body to the flat-bottomed cleaning base.\n\nConstruction: Curved handle, upright dust bag, slanted neck and broad cleaning head. Bounds (8,4)-(40,44).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '79956b84-d271-5a2f-bc03-ba8c4043b2b7'
SOURCE_PATH = 'pictographic-primitives/wayfinding/cleaning vacuum_79956b84-d271-5a2f-bc03-ba8c4043b2b7.svg'
AUTHOR = 'gpt-6'

class UprightVacuumCleaner(Solo48):
    icon_id = 'upright-vacuum-cleaner'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    aliases = ()
    keywords = ('vacuum', 'cleaner', 'upright', 'cleaning', 'appliance', 'floor')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_line('floor-head-1', (8, 44), (12, 36))
        self.add_line('floor-head-2-joint-1', (12, 36), (28, 36))
        self.add_line('floor-head-2-joint-2', (28, 36), (36, 36))
        self.add_line('floor-head-3', (36, 36), (40, 44))
        self.add_line('floor-head-4', (40, 44), (8, 44))
        self.add_line('neck', (28, 36), (26, 28))
        self.add_line('bag-0-joint-1', (23, 14), (24, 14))
        self.add_line('bag-0-joint-2', (24, 14), (27, 14))
        self.add_arc('bag-1', (27, 14), (32, 19), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('bag-2', (32, 19), (32, 23))
        self.add_arc('bag-3', (32, 23), (27, 28), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('bag-4-joint-1', (27, 28), (26, 28))
        self.add_line('bag-4-joint-2', (26, 28), (23, 28))
        self.add_arc('bag-5', (23, 28), (18, 23), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('bag-6', (18, 23), (18, 19))
        self.add_arc('bag-7', (18, 19), (23, 14), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('handle-upright', (24, 14), (24, 10))
        self.add_arc('handle-bend', (24, 10), (30, 4), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('handle-top', (30, 4), (36, 4))
        self.add_contour('floor-head', 'floor-head-1', 'floor-head-2-joint-1', 'floor-head-2-joint-2', 'floor-head-3', 'floor-head-4', closed=True)
        self.add_contour('bag', 'bag-0-joint-1', 'bag-0-joint-2', 'bag-1', 'bag-2', 'bag-3', 'bag-4-joint-1', 'bag-4-joint-2', 'bag-5', 'bag-6', 'bag-7', closed=True)
        self.add_contour('handle', 'handle-upright', 'handle-bend', 'handle-top', closed=False)
        self.relate('connect', 'neck', 'bag')
        self.relate('connect', 'neck', 'floor-head')
        self.relate('connect', 'handle', 'bag')
