"""Advertising technorati (_uncategorized_01), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5b7fd18e-1654-4680-87ab-99986f0f5a39'
SOURCE_PATH = 'icons-json/_uncategorized_01/advertising technorati_5b7fd18e-1654-4680-87ab-99986f0f5a39.json'
AUTHOR = 'json_to_solo'

class AdvertisingTechnoratiUncategorized01(Solo48):
    icon_id = 'advertising-technorati-uncategorized-01'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized_01'
    aliases = ()
    keywords = ('advertising', 'technorati', '_uncategorized_01')

    def build(self):
        self.add_line('e0', (8, 40), (16, 36))
        self.add_line('e1', (16, 36), (20, 37))
        self.add_line('e2', (10, 32), (8, 40))
        self.add_arc('e3-1', (20, 37), (33, 35), radius_x=27, sweep=False)
        self.add_arc('e3-2', (33, 35), (44, 22), radius_x=14, sweep=False)
        self.add_arc('e3-3', (44, 22), (38, 12), radius_x=12, sweep=False)
        self.add_line('e3-4', (38, 12), (32, 9))
        self.add_line('e3-5', (32, 9), (24, 8))
        self.add_line('e3-6', (24, 8), (14, 10))
        self.add_arc('e3-7', (14, 10), (10, 12), radius_x=22, sweep=False)
        self.add_arc('e3-8', (10, 12), (4, 22), radius_x=12, sweep=False)
        self.add_arc('e3-9', (4, 22), (10, 32), radius_x=12, sweep=False)
        self.add_contour('c0', 'e0', 'e1', 'e3-1', 'e3-2', 'e3-3', 'e3-4', 'e3-5', 'e3-6', 'e3-7', 'e3-8', 'e3-9', 'e2', closed=True)
