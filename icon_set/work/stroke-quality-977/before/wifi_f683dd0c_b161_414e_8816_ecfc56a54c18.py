"""Wifi (networks), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f683dd0c-b161-414e-8816-ecfc56a54c18'
SOURCE_PATH = 'pictographic-primitives/networks/wifi_f683dd0c-b161-414e-8816-ecfc56a54c18.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class WifiF683dd0c(Solo48):
    icon_id = 'wifi-f683dd0c'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'networks'
    aliases = ()
    keywords = ('wifi', 'networks')

    def build(self):
        self.add_line('sym-e0', (24, 40), (24, 40))
        self.add_arc('sym-e2', (4, 17), (5, 16), radius_x=3)
        self.add_arc('sym-e3', (5, 16), (10, 12), radius_x=44)
        self.add_arc('sym-e4', (10, 12), (23, 8), radius_x=25)
        self.add_arc('sym-e6', (23, 8), (24, 8), radius_x=39, sweep=False)
        self.add_line('sym-e9', (24, 8), (25, 8))
        self.add_arc('sym-e11', (25, 8), (38, 12), radius_x=24)
        self.add_arc('sym-e12', (38, 12), (43, 16), radius_x=44)
        self.add_line('sym-e13', (43, 16), (44, 17))
        self.add_arc('sym-e15', (14, 27), (19, 24), radius_x=15)
        self.add_arc('sym-e16', (19, 24), (24, 23), radius_x=15)
        self.add_arc('sym-e17', (24, 23), (29, 24), radius_x=15)
        self.add_arc('sym-e18', (29, 24), (34, 27), radius_x=15)
        self.add_contour('sym-c0', 'sym-e0', closed=True)
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e6', 'sym-e9', 'sym-e11', 'sym-e12', 'sym-e13')
        self.add_contour('sym-c2', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18')
