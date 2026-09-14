"""Christianity (religion), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '07ae975c-acdb-4a08-93fc-2f176ffca091'
SOURCE_PATH = 'icons-json/religion/christianity_07ae975c-acdb-4a08-93fc-2f176ffca091.json'
AUTHOR = 'json_to_solo'

class ChristianityReligion(Solo48):
    icon_id = 'christianity-religion'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'religion'
    aliases = ()
    keywords = ('christianity', 'religion')

    def build(self):
        self.add_line('e0', (41, 19), (38, 24))
        self.add_arc('e1', (44, 8), (41, 19), radius_x=35)
        self.add_arc('e2', (44, 40), (38, 24), radius_x=42, sweep=False)
        self.add_arc('e3-1', (38, 24), (24, 12), radius_x=26, sweep=False)
        self.add_arc('e3-2', (24, 12), (4, 24), radius_x=22, sweep=False)
        self.add_arc('e3-3', (4, 24), (25, 36), radius_x=20, sweep=False)
        self.add_arc('e3-4', (25, 36), (38, 24), radius_x=27, sweep=False)
        self.add_contour('c0', 'e1', 'e0')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3-1', 'e3-2', 'e3-3', 'e3-4', closed=True)
        self.relate('connect', 'c1', 'c2')
