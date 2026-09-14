"""Sad crying (smileys), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '785e1eca-19ef-5be9-9188-d492077d05a9'
SOURCE_PATH = 'icons-json/smileys/sad crying_785e1eca-19ef-5be9-9188-d492077d05a9.json'
AUTHOR = 'json_to_solo'

class SadCryingSmileys(Solo48):
    icon_id = 'sad-crying-smileys'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('sad', 'crying', 'smileys')

    def build(self):
        self.add_arc('e0-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e0-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_arc('e1', (29, 16), (36, 19), radius_x=8, sweep=False)
        self.add_arc('e2', (12, 19), (19, 16), radius_x=7, sweep=False)
        self.add_arc('e3', (13, 23), (19, 22), radius_x=6, sweep=False)
        self.add_arc('e4', (29, 22), (35, 23), radius_x=6, sweep=False)
        self.add_arc('e5-1', (32, 37), (18, 37), radius_x=15, sweep=False)
        self.add_arc('e5-2', (18, 37), (16, 34), radius_x=2)
        self.add_arc('e5-3', (16, 34), (19, 30), radius_x=9)
        self.add_arc('e5-4', (19, 30), (27, 29), radius_x=8)
        self.add_arc('e5-5', (27, 29), (32, 37), radius_x=6)
        self.add_contour('c0', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('c3', 'e4')
        self.add_contour('c4', 'e5-1', 'e5-2', 'e5-3', 'e5-4', 'e5-5', closed=True)
        self.add_contour('e0', 'e0-top', 'e0-bottom', closed=True)
