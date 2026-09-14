"""Astrology lilith (religion), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8fe41c51-86b1-5293-9e23-cf23e45a15fc'
SOURCE_PATH = 'icons-json/religion/astrology lilith_8fe41c51-86b1-5293-9e23-cf23e45a15fc.json'
AUTHOR = 'json_to_solo'

class AstrologyLilithReligion(Solo48):
    icon_id = 'astrology-lilith-religion'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'religion'
    aliases = ()
    keywords = ('astrology', 'lilith', 'religion')

    def build(self):
        self.add_line('e0', (25, 28), (25, 44))
        self.add_line('e1', (15, 36), (35, 36))
        self.add_arc('e2-1', (33, 6), (24, 4), radius_x=22, sweep=False)
        self.add_arc('e2-2', (24, 4), (14, 7), radius_x=19, sweep=False)
        self.add_arc('e2-3', (14, 7), (8, 16), radius_x=11, sweep=False)
        self.add_arc('e2-4', (8, 16), (19, 27), radius_x=12, sweep=False)
        self.add_arc('e2-5', (19, 27), (40, 22), radius_x=22, sweep=False)
        self.add_contour('c0', 'e2-1', 'e2-2', 'e2-3', 'e2-4', 'e2-5')
        self.add_contour('c1', 'e0')
        self.add_contour('c2', 'e1')
        self.relate('connect', 'c1', 'c0')
