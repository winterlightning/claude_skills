"""Open eyes (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '47a44264-9c90-4733-bd24-6bfdf39290df'
SOURCE_PATH = 'icons-json/interface-essential/open eyes_47a44264-9c90-4733-bd24-6bfdf39290df.json'
AUTHOR = 'gpt-6'

class OpenEyes(Solo48):
    icon_id = 'open-eyes'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('open', 'eyes', 'interface-essential')

    def build(self):
        self.add_arc('sym-e0', (19, 24), (29, 24), radius_x=5, radius_y=7, large_arc=False, sweep=True)
        self.add_arc('sym-e1', (29, 24), (19, 24), radius_x=5, radius_y=7, large_arc=False, sweep=True)
        self.add_arc('sym-e2', (4, 24), (8, 19), radius_x=33, radius_y=33, large_arc=False, sweep=True)
        self.add_arc('sym-e3', (8, 19), (23, 8), radius_x=24, radius_y=24, large_arc=False, sweep=True)
        self.add_line('sym-e4', (23, 8), (25, 8))
        self.add_arc('sym-e8', (25, 8), (40, 19), radius_x=24, radius_y=24, large_arc=False, sweep=True)
        self.add_arc('sym-e9', (40, 19), (44, 24), radius_x=33, radius_y=33, large_arc=False, sweep=True)
        self.add_arc('sym-e10', (44, 24), (40, 29), radius_x=32, radius_y=32, large_arc=False, sweep=True)
        self.add_arc('sym-e11', (40, 29), (25, 40), radius_x=25, radius_y=25, large_arc=False, sweep=True)
        self.add_line('sym-e12', (25, 40), (23, 40))
        self.add_arc('sym-e16', (23, 40), (8, 29), radius_x=25, radius_y=25, large_arc=False, sweep=True)
        self.add_arc('sym-e17', (8, 29), (4, 24), radius_x=33, radius_y=33, large_arc=False, sweep=True)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e16', 'sym-e17', closed=True)
