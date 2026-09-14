"""Swift logo (logos), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '00fea778-55ec-442f-9e36-574d44a3c22a'
SOURCE_PATH = 'icons-json/logos/swift logo_00fea778-55ec-442f-9e36-574d44a3c22a.json'
AUTHOR = 'json_to_solo'

class SwiftLogo(Solo48):
    icon_id = 'swift-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('swift', 'logo', 'logos')

    def build(self):
        self.add_line('e0', (6, 33), (9, 34))
        self.add_line('e1', (21, 34), (24, 33))
        self.add_line('e2', (24, 33), (19, 31))
        self.add_line('e3', (9, 22), (4, 16))
        self.add_line('e4', (4, 16), (8, 19))
        self.add_line('e5', (27, 27), (15, 12))
        self.add_line('e6', (15, 12), (19, 14))
        self.add_line('e7', (19, 14), (31, 25))
        self.add_line('e8', (34, 14), (31, 8))
        self.add_line('e9', (31, 8), (35, 11))
        self.add_line('e10', (36, 37), (30, 38))
        self.add_line('e11', (10, 37), (6, 33))
        self.add_arc('e12', (9, 34), (21, 34), radius_x=17, sweep=False)
        self.add_arc('e13', (19, 31), (9, 22), radius_x=44)
        self.add_arc('e14', (8, 19), (27, 27), radius_x=36, sweep=False)
        self.add_arc('e15-1', (31, 25), (34, 20), radius_x=4, sweep=False)
        self.add_arc('e15-2', (34, 20), (34, 14), radius_x=11, sweep=False)
        self.add_arc('e16-1', (35, 11), (39, 31), radius_x=18)
        self.add_arc('e16-2', (39, 31), (44, 37), radius_x=7)
        self.add_arc('e16-3', (44, 37), (44, 40), radius_x=15, sweep=False)
        self.add_arc('e16-4', (44, 40), (36, 37), radius_x=8, sweep=False)
        self.add_arc('e17-1', (30, 38), (22, 40), radius_x=42)
        self.add_line('e17-2', (22, 40), (10, 37))
        self.add_contour('c0', 'e0', 'e12', 'e1', 'e2', 'e13', 'e3')
        self.add_contour('c1', 'e4', 'e14', 'e5', 'e6', 'e7', 'e15-1', 'e15-2', 'e8', 'e9', 'e16-1', 'e16-2', 'e16-3', 'e16-4', 'e10', 'e17-1', 'e17-2', 'e11')
