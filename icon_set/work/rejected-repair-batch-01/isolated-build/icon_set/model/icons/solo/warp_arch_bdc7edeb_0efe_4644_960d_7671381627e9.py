"""Warp arch (design), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'bdc7edeb-0efe-4644-960d-7671381627e9'
SOURCE_PATH = 'pictographic-primitives/design/warp arch_bdc7edeb-0efe-4644-960d-7671381627e9.svg'
AUTHOR = 'gpt-6'

class WarpArch(Solo48):
    icon_id = 'warp-arch'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('warp', 'arch', 'design')

    def build(self):
        self.add_arc('sym-e0', (4, 29), (12, 23), radius_x=34, radius_y=34, large_arc=False, sweep=True)
        self.add_arc('sym-e1', (12, 23), (24, 20), radius_x=26, radius_y=26, large_arc=False, sweep=True)
        self.add_arc('sym-e2', (24, 20), (36, 23), radius_x=26, radius_y=26, large_arc=False, sweep=True)
        self.add_arc('sym-e3', (36, 23), (44, 29), radius_x=34, radius_y=34, large_arc=False, sweep=True)
        self.add_line('sym-e4', (44, 29), (44, 40))
        self.add_arc('sym-e5', (44, 40), (35, 34), radius_x=38, radius_y=38, large_arc=False, sweep=False)
        self.add_arc('sym-e6', (35, 34), (24, 32), radius_x=27, radius_y=27, large_arc=False, sweep=False)
        self.add_arc('sym-e7', (24, 32), (13, 34), radius_x=27, radius_y=27, large_arc=False, sweep=False)
        self.add_arc('sym-e8', (13, 34), (4, 40), radius_x=38, radius_y=38, large_arc=False, sweep=False)
        self.add_line('sym-e9', (4, 40), (4, 16))
        self.add_line('sym-e12', (4, 16), (5, 15))
        self.add_arc('sym-e13', (5, 15), (23, 8), radius_x=29, radius_y=29, large_arc=False, sweep=True)
        self.add_line('sym-e14', (23, 8), (25, 8))
        self.add_arc('sym-e18', (25, 8), (43, 15), radius_x=29, radius_y=29, large_arc=False, sweep=True)
        self.add_arc('sym-e19', (43, 15), (44, 16), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('sym-e21', (44, 16), (44, 29))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e18', 'sym-e19', 'sym-e21', closed=False)
