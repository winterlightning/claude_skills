"""Vimeo logo (logos), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0368b9b2-c06f-47a3-9fa0-ea39f0be0ef8'
SOURCE_PATH = 'icons-json/logos/vimeo logo_0368b9b2-c06f-47a3-9fa0-ea39f0be0ef8.json'
AUTHOR = 'json_to_solo'

class VimeoLogoLogos(Solo48):
    icon_id = 'vimeo-logo-logos'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('vimeo', 'logo', 'logos')

    def build(self):
        self.add_line('e0', (29, 16), (31, 16))
        self.add_line('e1', (22, 25), (21, 17))
        self.add_line('e2', (6, 17), (8, 17))
        self.add_line('e3', (10, 19), (14, 34))
        self.add_arc('e4-1', (31, 16), (33, 19), radius_x=2)
        self.add_arc('e4-2', (33, 19), (28, 28), radius_x=21)
        self.add_arc('e4-3', (28, 28), (24, 29), radius_x=3)
        self.add_line('e4-4', (24, 29), (22, 25))
        self.add_arc('e5-1', (21, 17), (17, 9), radius_x=8, sweep=False)
        self.add_arc('e5-2', (17, 9), (4, 16), radius_x=18, sweep=False)
        self.add_arc('e5-3', (4, 16), (6, 17), radius_x=2, sweep=False)
        self.add_arc('e6', (8, 17), (10, 19), radius_x=2)
        self.add_arc('e7-1', (14, 34), (21, 40), radius_x=8, sweep=False)
        self.add_arc('e7-2', (21, 40), (31, 35), radius_x=14, sweep=False)
        self.add_arc('e7-3', (31, 35), (44, 14), radius_x=34, sweep=False)
        self.add_arc('e7-4', (44, 14), (38, 8), radius_x=6, sweep=False)
        self.add_line('e7-5', (38, 8), (34, 9))
        self.add_arc('e7-6', (34, 9), (29, 16), radius_x=8, sweep=False)
        self.add_contour('c0', 'e0', 'e4-1', 'e4-2', 'e4-3', 'e4-4', 'e1', 'e5-1', 'e5-2', 'e5-3', 'e2', 'e6', 'e3', 'e7-1', 'e7-2', 'e7-3', 'e7-4', 'e7-5', 'e7-6', closed=True)
