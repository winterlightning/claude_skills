"""Nauseous (smileys), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd8d61638-d143-5e45-ab87-0388fc66f071'
SOURCE_PATH = 'icons-json/smileys/nauseous_d8d61638-d143-5e45-ab87-0388fc66f071.json'
AUTHOR = 'json_to_solo'

class NauseousD8d61638(Solo48):
    icon_id = 'nauseous-d8d61638'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('nauseous', 'smileys')

    def build(self):
        self.add_line('e0', (35, 35), (33, 32))
        self.add_arc('e1-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e1-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_arc('e2', (13, 25), (19, 24), radius_x=4)
        self.add_arc('e3', (29, 24), (35, 24), radius_x=4)
        self.add_arc('e4-1', (33, 32), (29, 34), radius_x=3, sweep=False)
        self.add_arc('e4-2', (29, 34), (27, 34), radius_x=2)
        self.add_line('e4-3', (27, 34), (24, 32))
        self.add_arc('e4-4', (24, 32), (21, 34), radius_x=5, sweep=False)
        self.add_arc('e4-5', (21, 34), (16, 32), radius_x=4)
        self.add_arc('e4-6', (16, 32), (13, 34), radius_x=5, sweep=False)
        self.add_arc('e5', (29, 14), (36, 18), radius_x=6, sweep=False)
        self.add_arc('e6', (12, 18), (19, 16), radius_x=7, sweep=False)
        self.add_contour('c0', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e0', 'e4-1', 'e4-2', 'e4-3', 'e4-4', 'e4-5', 'e4-6')
        self.add_contour('c3', 'e5')
        self.add_contour('c4', 'e6')
        self.add_contour('e1', 'e1-top', 'e1-bottom', closed=True)
