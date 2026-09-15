"""Wireless access (networks), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f57e425b-c626-50a8-8206-2b98c4e3dc56'
SOURCE_PATH = 'pictographic-primitives/networks/wireless access_f57e425b-c626-50a8-8206-2b98c4e3dc56.svg'
AUTHOR = 'gpt-6'

class WirelessAccess(Solo48):
    icon_id = 'wireless-access'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'networks'
    aliases = ()
    keywords = ('wireless', 'access', 'networks')

    def build(self):
        self.add_arc('sym-e0', (8, 24), (20, 24), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('sym-e1', (20, 24), (8, 24), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('sym-e2', (32, 4), (34, 7), radius_x=31, radius_y=31, large_arc=False, sweep=False)
        self.add_arc('sym-e3', (34, 7), (40, 23), radius_x=28, radius_y=28, large_arc=False, sweep=True)
        self.add_line('sym-e5', (40, 23), (40, 25))
        self.add_arc('sym-e8', (40, 25), (34, 41), radius_x=27, radius_y=27, large_arc=False, sweep=True)
        self.add_arc('sym-e9', (34, 41), (32, 44), radius_x=31, radius_y=31, large_arc=False, sweep=False)
        self.add_arc('sym-e10', (25, 11), (28, 15), radius_x=20, radius_y=20, large_arc=False, sweep=False)
        self.add_arc('sym-e11', (28, 15), (30, 24), radius_x=17, radius_y=17, large_arc=False, sweep=True)
        self.add_arc('sym-e12', (30, 24), (28, 33), radius_x=17, radius_y=17, large_arc=False, sweep=True)
        self.add_arc('sym-e13', (28, 33), (25, 37), radius_x=20, radius_y=20, large_arc=False, sweep=False)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e5', 'sym-e8', 'sym-e9', closed=False)
        self.add_contour('sym-c2', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', closed=False)
