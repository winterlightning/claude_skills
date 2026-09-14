"""Pile poo (smileys), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c335382e-9874-5d16-95d4-344cff747084'
SOURCE_PATH = 'icons-json/smileys/pile poo_c335382e-9874-5d16-95d4-344cff747084.json'
AUTHOR = 'json_to_solo'

class PilePooSmileys(Solo48):
    icon_id = 'pile-poo-smileys'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('pile', 'poo', 'smileys')

    def build(self):
        self.add_line('e0', (35, 42), (13, 42))
        self.add_line('e1', (13, 29), (31, 29))
        self.add_line('e2', (26, 19), (16, 19))
        self.add_line('e3-1', (13, 42), (9, 41))
        self.add_arc('e3-2', (9, 41), (6, 36), radius_x=6)
        self.add_arc('e3-3', (6, 36), (13, 29), radius_x=7)
        self.add_arc('e4-1', (31, 29), (36, 27), radius_x=7, sweep=False)
        self.add_arc('e4-2', (36, 27), (39, 29), radius_x=12, sweep=False)
        self.add_arc('e4-3', (39, 29), (42, 35), radius_x=8)
        self.add_arc('e4-4', (42, 35), (36, 42), radius_x=8)
        self.add_line('e4-5', (36, 42), (35, 42))
        self.add_arc('e5', (35, 27), (31, 17), radius_x=6, sweep=False)
        self.add_line('e6-1', (13, 29), (11, 26))
        self.add_arc('e6-2', (11, 26), (16, 19), radius_x=6)
        self.add_arc('e6-3', (16, 19), (15, 15), radius_x=5)
        self.add_arc('e6-4', (15, 15), (18, 12), radius_x=4)
        self.add_arc('e6-5', (18, 12), (23, 6), radius_x=5, sweep=False)
        self.add_arc('e6-6', (23, 6), (31, 17), radius_x=9)
        self.add_arc('e7', (30, 17), (26, 19), radius_x=6)
        self.add_contour('c0', 'e0', 'e3-1', 'e3-2', 'e3-3', 'e1', 'e4-1', 'e4-2', 'e4-3', 'e4-4', 'e4-5', closed=True)
        self.add_contour('c1', 'e5')
        self.add_contour('c2', 'e6-1', 'e6-2', 'e6-3', 'e6-4', 'e6-5', 'e6-6')
        self.add_contour('c3', 'e7', 'e2')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c2', 'c0')
        self.relate('connect', 'c3', 'c2')
