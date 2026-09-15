"""Responsive design expand (websites), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '500a391a-b10e-4295-b94f-b4c317cce2c7'
SOURCE_PATH = 'pictographic-primitives/websites/responsive design expand_500a391a-b10e-4295-b94f-b4c317cce2c7.svg'
AUTHOR = 'gpt-6'

class ResponsiveDesignExpand(Solo48):
    icon_id = 'responsive-design-expand'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'websites'
    aliases = ()
    keywords = ('responsive', 'design', 'expand', 'websites')

    def build(self):
        self.add_line('e0', (4, 18), (4, 11))
        self.add_line('e1', (8, 8), (41, 8))
        self.add_line('e2', (44, 11), (44, 18))
        self.add_line('e3', (4, 18), (44, 18))
        self.add_line('e4', (4, 18), (4, 34))
        self.add_line('e5', (9, 40), (40, 40))
        self.add_line('e6', (44, 37), (44, 18))
        self.add_arc('e7', (4, 11), (8, 8), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('e8', (41, 8), (44, 11), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('e9-2', (4, 34), (5, 37), radius_x=7, radius_y=7, large_arc=False, sweep=False)
        self.add_arc('e9-3', (5, 37), (9, 40), radius_x=5, radius_y=5, large_arc=False, sweep=False)
        self.add_arc('e10', (40, 40), (44, 37), radius_x=5, radius_y=5, large_arc=False, sweep=False)
        self.add_contour('c0', 'e0', 'e7', 'e1', 'e8', 'e2', closed=False)
        self.add_contour('c1', 'e3', closed=False)
        self.add_contour('c2', 'e4', 'e9-2', 'e9-3', 'e5', 'e10', 'e6', closed=False)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
