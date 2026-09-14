'Two children sit at opposite ends of a seesaw with circular heads and bent legs. The long plank tilts upward to the right above a central upright support and short foot.\n\nConstruction: Two seated children balance a diagonal seesaw on a central pivot. Bounds (4,8)-(44,40).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e5a65a59-3ada-4acf-99fb-4a0e4440ea37'
SOURCE_PATH = 'pictographic-primitives/wayfinding/family child teeter_e5a65a59-3ada-4acf-99fb-4a0e4440ea37.svg'
AUTHOR = 'gpt-6'

class ChildrenOnSeesaw(Solo48):
    icon_id = 'children-on-seesaw'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/wayfinding'
    aliases = ()
    keywords = ('children', 'seesaw', 'play', 'playground', 'balance', 'seat')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_arc('left-child-head-top', (7, 17), (13, 17), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('left-child-head-bottom', (13, 17), (7, 17), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('left-child-seat-1', (8, 29), (16, 29))
        self.add_line('left-child-seat-2', (16, 29), (18, 34))
        self.add_arc('right-child-head-top', (33, 11), (39, 11), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('right-child-head-bottom', (39, 11), (33, 11), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('right-child-seat-1', (36, 23), (30, 23))
        self.add_line('right-child-seat-2', (30, 23), (34, 27))
        self.add_line('beam-1', (4, 36), (24, 30))
        self.add_line('beam-2', (24, 30), (34, 27))
        self.add_line('beam-3', (34, 27), (44, 24))
        self.add_line('pivot-1', (24, 30), (24, 40))
        self.add_line('pivot-2', (24, 40), (18, 40))
        self.add_line('pivot-3-joint-1', (18, 40), (24, 40))
        self.add_line('pivot-3-joint-2', (24, 40), (30, 40))
        self.add_contour('left-child-head', 'left-child-head-top', 'left-child-head-bottom', closed=True)
        self.add_contour('left-child-seat', 'left-child-seat-1', 'left-child-seat-2', closed=False)
        self.add_contour('right-child-head', 'right-child-head-top', 'right-child-head-bottom', closed=True)
        self.add_contour('right-child-seat', 'right-child-seat-1', 'right-child-seat-2', closed=False)
        self.add_contour('beam', 'beam-1', 'beam-2', 'beam-3', closed=False)
        self.add_contour('pivot', 'pivot-1', 'pivot-2', 'pivot-3-joint-1', 'pivot-3-joint-2', closed=False)
        self.relate('connect', 'beam', 'pivot')
        self.relate('connect', 'beam', 'right-child-seat')
