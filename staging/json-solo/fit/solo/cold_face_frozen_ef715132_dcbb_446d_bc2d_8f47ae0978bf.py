"""Cold face frozen (smileys), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ef715132-dcbb-446d-bc2d-8f47ae0978bf'
SOURCE_PATH = 'icons-json/smileys/cold face frozen_ef715132-dcbb-446d-bc2d-8f47ae0978bf.json'
AUTHOR = 'json_to_solo'

class ColdFaceFrozenSmileys(Solo48):
    icon_id = 'cold-face-frozen-smileys'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('cold', 'face', 'frozen', 'smileys')

    def build(self):
        self.add_line('e0', (14, 38), (17, 41))
        self.add_line('e1', (17, 41), (19, 38))
        self.add_line('e2', (19, 38), (24, 42))
        self.add_line('e3', (24, 42), (28, 38))
        self.add_line('e4', (28, 38), (31, 41))
        self.add_line('e5', (31, 41), (35, 38))
        self.add_line('e6', (21, 24), (21, 30))
        self.add_line('e7', (27, 24), (27, 30))
        self.add_line('e8', (31, 24), (17, 24))
        self.add_line('e9', (17, 30), (31, 30))
        self.add_arc('e10-1', (11, 37), (6, 25), radius_x=18)
        self.add_line('e10-2', (6, 25), (8, 16))
        self.add_arc('e10-3', (8, 16), (9, 14), radius_x=19, sweep=False)
        self.add_arc('e10-4', (9, 14), (18, 7), radius_x=19)
        self.add_line('e10-5', (18, 7), (24, 6))
        self.add_arc('e10-6', (24, 6), (42, 24), radius_x=18)
        self.add_line('e10-7', (42, 24), (41, 31))
        self.add_arc('e10-8', (41, 31), (38, 36), radius_x=17)
        self.add_arc('e11', (13, 19), (13, 20), radius_x=20)
        self.add_arc('e12', (34, 19), (34, 20), radius_x=23, sweep=False)
        self.add_arc('e13', (17, 24), (17, 30), radius_x=3, sweep=False)
        self.add_arc('e14', (31, 30), (31, 24), radius_x=3, sweep=False)
        self.add_contour('c0', 'e10-1', 'e10-2', 'e10-3', 'e10-4', 'e10-5', 'e10-6', 'e10-7', 'e10-8')
        self.add_contour('c1', 'e0', 'e1', 'e2', 'e3', 'e4', 'e5')
        self.add_contour('c2', 'e11')
        self.add_contour('c3', 'e12')
        self.add_contour('c4', 'e6')
        self.add_contour('c5', 'e7')
        self.add_contour('c6', 'e8', 'e13', 'e9', 'e14', closed=True)
        self.relate('connect', 'c4', 'c6')
        self.relate('connect', 'c4', 'c6')
        self.relate('connect', 'c5', 'c6')
        self.relate('connect', 'c5', 'c6')
