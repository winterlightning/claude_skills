"""Imessage logo (logos), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '57877e05-412a-4ab7-81af-b1b8f5355989'
SOURCE_PATH = 'icons-json/logos/imessage logo_57877e05-412a-4ab7-81af-b1b8f5355989.json'
AUTHOR = 'json_to_solo'

class ImessageLogoLogos(Solo48):
    icon_id = 'imessage-logo-logos'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('imessage', 'logo', 'logos')

    def build(self):
        self.add_line('e0', (8, 40), (10, 37))
        self.add_line('e1', (9, 40), (8, 40))
        self.add_arc('e2-1', (10, 37), (11, 34), radius_x=2, sweep=False)
        self.add_arc('e2-2', (11, 34), (4, 23), radius_x=14)
        self.add_arc('e2-3', (4, 23), (9, 13), radius_x=13)
        self.add_arc('e2-4', (9, 13), (17, 9), radius_x=21)
        self.add_line('e2-5', (17, 9), (24, 8))
        self.add_line('e2-6', (24, 8), (32, 9))
        self.add_arc('e2-7', (32, 9), (39, 13), radius_x=20)
        self.add_arc('e2-8', (39, 13), (44, 22), radius_x=12)
        self.add_arc('e2-9', (44, 22), (28, 37), radius_x=16)
        self.add_arc('e2-10', (28, 37), (19, 37), radius_x=25)
        self.add_arc('e2-11', (19, 37), (16, 39), radius_x=11, sweep=False)
        self.add_line('e2-12', (16, 39), (11, 40))
        self.add_line('e2-13', (11, 40), (9, 40))
        self.add_contour('c0', 'e0', 'e2-1', 'e2-2', 'e2-3', 'e2-4', 'e2-5', 'e2-6', 'e2-7', 'e2-8', 'e2-9', 'e2-10', 'e2-11', 'e2-12', 'e2-13', 'e1', closed=True)
