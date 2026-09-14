"""Calendly logo (_uncategorized), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bacfa429-a6b0-4633-9b16-4de2c0ffebf1'
SOURCE_PATH = 'icons-json/_uncategorized_09/calendly logo_bacfa429-a6b0-4633-9b16-4de2c0ffebf1.json'
AUTHOR = 'json_to_solo'

class CalendlyLogoUncategorized(Solo48):
    icon_id = 'calendly-logo-uncategorized'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized'
    aliases = ()
    keywords = ('calendly', 'logo', '_uncategorized')

    def build(self):
        self.add_arc('e0-1', (42, 17), (25, 6), radius_x=19, sweep=False)
        self.add_line('e0-2', (25, 6), (16, 8))
        self.add_arc('e0-3', (16, 8), (6, 24), radius_x=18, sweep=False)
        self.add_arc('e0-4', (6, 24), (24, 42), radius_x=18, sweep=False)
        self.add_line('e0-5', (24, 42), (31, 41))
        self.add_line('e0-6', (31, 41), (35, 39))
        self.add_arc('e0-7', (35, 39), (42, 30), radius_x=19, sweep=False)
        self.add_arc('e0-8', (42, 30), (35, 29), radius_x=5, sweep=False)
        self.add_arc('e0-9', (35, 29), (26, 35), radius_x=13)
        self.add_arc('e0-10', (26, 35), (14, 28), radius_x=11)
        self.add_arc('e0-11', (14, 28), (25, 13), radius_x=11)
        self.add_arc('e0-12', (25, 13), (36, 19), radius_x=14)
        self.add_arc('e0-13', (36, 19), (42, 18), radius_x=5, sweep=False)
        self.add_arc('e0-14', (42, 18), (42, 17), radius_x=24)
        self.add_contour('c0', 'e0-1', 'e0-2', 'e0-3', 'e0-4', 'e0-5', 'e0-6', 'e0-7', 'e0-8', 'e0-9', 'e0-10', 'e0-11', 'e0-12', 'e0-13', 'e0-14', closed=True)
