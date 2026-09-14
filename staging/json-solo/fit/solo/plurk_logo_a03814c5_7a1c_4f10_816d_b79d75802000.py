"""Plurk logo (logos), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a03814c5-7a1c-4f10-816d-b79d75802000'
SOURCE_PATH = 'icons-json/logos/plurk logo_a03814c5-7a1c-4f10-816d-b79d75802000.json'
AUTHOR = 'json_to_solo'

class PlurkLogoA03814c5(Solo48):
    icon_id = 'plurk-logo-a03814c5'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('plurk', 'logo', 'logos')

    def build(self):
        self.add_line('e0', (6, 6), (34, 6))
        self.add_line('e1', (42, 13), (42, 24))
        self.add_line('e2', (34, 32), (15, 32))
        self.add_line('e3', (15, 32), (15, 42))
        self.add_line('e4', (15, 42), (6, 42))
        self.add_line('e5', (6, 42), (6, 6))
        self.add_line('e6', (15, 23), (15, 14))
        self.add_line('e7', (15, 14), (32, 14))
        self.add_line('e8', (32, 14), (32, 23))
        self.add_line('e9', (32, 23), (15, 23))
        self.add_arc('e10', (34, 6), (42, 13), radius_x=10)
        self.add_arc('e11', (42, 24), (34, 32), radius_x=9)
        self.add_contour('c0', 'e0', 'e10', 'e1', 'e11', 'e2', 'e3', 'e4', 'e5', closed=True)
        self.add_contour('c1', 'e6', 'e7', 'e8', 'e9', closed=True)
