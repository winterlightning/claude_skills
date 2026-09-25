'A wheelchair user faces right beside a triangular ramp rising toward the upper-right. The figure has a circular head, an extended arm and bent legs above a large curved wheel.\n\nConstruction: Wheelchair user faces a rising ramp; the open wheel rim distinguishes the chair. Bounds (4,8)-(44,40).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9dfb6289-487a-4bfa-95e5-fdc48e5dd47a'
SOURCE_PATH = 'pictographic-primitives/wayfinding/wheelchair way_9dfb6289-487a-4bfa-95e5-fdc48e5dd47a.svg'
AUTHOR = 'gpt-6'

class WheelchairUserAtRamp(Solo48):
    icon_id = 'wheelchair-user-at-ramp'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ()
    keywords = ('wheelchair', 'ramp', 'person', 'accessibility', 'mobility', 'slope')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_arc('head-top', (13, 11), (19, 11), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('head-bottom', (19, 11), (13, 11), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('rider-1', (16, 23), (16, 30))
        self.add_line('rider-2', (16, 30), (20, 30))
        self.add_line('rider-3', (20, 30), (24, 32))
        self.add_arc('wheel', (16, 23), (16, 39), radius_x=12, radius_y=8, large_arc=False, sweep=False)
        self.add_line('ramp-1', (28, 40), (44, 28))
        self.add_line('ramp-2', (44, 28), (44, 40))
        self.add_line('ramp-3', (44, 40), (28, 40))
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_contour('rider', 'rider-1', 'rider-2', 'rider-3', closed=False)
        self.add_contour('ramp', 'ramp-1', 'ramp-2', 'ramp-3', closed=False)
        self.relate('connect', 'wheel', 'rider')
