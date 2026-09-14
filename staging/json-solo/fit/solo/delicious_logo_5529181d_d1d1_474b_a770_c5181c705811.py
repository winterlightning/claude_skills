"""Delicious logo (logos), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5529181d-d1d1-474b-a770-c5181c705811'
SOURCE_PATH = 'icons-json/logos/delicious logo_5529181d-d1d1-474b-a770-c5181c705811.json'
AUTHOR = 'json_to_solo'

class DeliciousLogoLogos(Solo48):
    icon_id = 'delicious-logo-logos'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('delicious', 'logo', 'logos')

    def build(self):
        self.add_line('e0', (23, 24), (6, 24))
        self.add_line('e1', (6, 24), (6, 42))
        self.add_line('e2', (6, 42), (23, 42))
        self.add_line('e3', (23, 42), (23, 24))
        self.add_line('e4', (23, 24), (42, 24))
        self.add_line('e5', (42, 24), (42, 6))
        self.add_line('e6', (42, 6), (23, 6))
        self.add_line('e7', (23, 6), (23, 24))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', closed=True)
        self.add_contour('c1', 'e4', 'e5', 'e6', 'e7', closed=True)
        self.relate('connect', 'c0', 'c1')
