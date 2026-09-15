"""Warp arc upper (design), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '41afe867-f59f-5952-985b-78e3355127ff'
SOURCE_PATH = 'icons-json/design/warp arc upper_41afe867-f59f-5952-985b-78e3355127ff.json'
AUTHOR = 'gpt-6'

class WarpArcUpper(Solo48):
    icon_id = 'warp-arc-upper'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('warp', 'arc', 'upper', 'design')

    def build(self):
        self.add_arc('sym-e1', (24, 4), (23, 4), radius_x=1, radius_y=1, large_arc=False, sweep=True)
        self.add_arc('sym-e2', (23, 4), (8, 21), radius_x=18, radius_y=18, large_arc=False, sweep=False)
        self.add_line('sym-e3', (8, 21), (8, 44))
        self.add_line('sym-e6', (8, 44), (40, 44))
        self.add_line('sym-e8', (40, 44), (40, 21))
        self.add_arc('sym-e11', (40, 21), (25, 4), radius_x=18, radius_y=18, large_arc=False, sweep=False)
        self.add_arc('sym-e12', (25, 4), (24, 4), radius_x=1, radius_y=1, large_arc=False, sweep=True)
        self.add_contour('sym-c0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e6', 'sym-e8', 'sym-e11', 'sym-e12', closed=True)
