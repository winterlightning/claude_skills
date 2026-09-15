"""Wifi (networks), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b7c0d52e-b021-59e3-b8ec-b0ebdccb7598'
SOURCE_PATH = 'pictographic-primitives/networks/wifi_b7c0d52e-b021-59e3-b8ec-b0ebdccb7598.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class WifiNetworks(Solo48):
    icon_id = 'wifi-networks'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'networks'
    aliases = ()
    keywords = ('wifi', 'networks')

    def build(self):
        self.add_line('sym-e0', (24, 40), (24, 40))
        self.add_arc('sym-e2', (4, 16), (10, 12), radius_x=44)
        self.add_arc('sym-e3', (10, 12), (23, 8), radius_x=29)
        self.add_arc('sym-e4', (23, 8), (24, 8), radius_x=39, sweep=False)
        self.add_line('sym-e5', (24, 8), (25, 8))
        self.add_arc('sym-e6', (25, 8), (38, 12), radius_x=28)
        self.add_line('sym-e7', (38, 12), (44, 16))
        self.add_arc('sym-e9', (10, 23), (24, 17), radius_x=21)
        self.add_arc('sym-e10', (24, 17), (38, 23), radius_x=21)
        self.add_arc('sym-e11', (17, 30), (24, 27), radius_x=13)
        self.add_arc('sym-e12', (24, 27), (31, 30), radius_x=13)
        self.add_contour('sym-c0', 'sym-e0', closed=True)
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7')
        self.add_contour('sym-c2', 'sym-e9', 'sym-e10')
        self.add_contour('sym-c3', 'sym-e11', 'sym-e12')
