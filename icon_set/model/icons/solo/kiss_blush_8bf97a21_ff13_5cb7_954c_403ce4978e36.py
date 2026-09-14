"""Kiss blush (smileys), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8bf97a21-ff13-5cb7-954c-403ce4978e36'
SOURCE_PATH = 'icons-json/smileys/kiss blush_8bf97a21-ff13-5cb7-954c-403ce4978e36.json'
AUTHOR = 'json_to_solo'

class KissBlush(Solo48):
    icon_id = 'kiss-blush'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('kiss', 'blush', 'smileys')

    def build(self):
        self.add_arc('e0-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e0-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_arc('e1-1', (13, 20), (17, 17), radius_x=4)
        self.add_arc('e1-2', (17, 17), (20, 20), radius_x=3)
        self.add_arc('e2-1', (28, 21), (30, 18), radius_x=3)
        self.add_arc('e2-2', (30, 18), (35, 20), radius_x=3)
        self.add_arc('e3-1', (24, 27), (27, 28), radius_x=3)
        self.add_arc('e3-2', (27, 28), (26, 31), radius_x=2)
        self.add_line('e4', (24, 31), (26, 31))
        self.add_arc('e5-1', (24, 37), (27, 35), radius_x=4, sweep=False)
        self.add_arc('e5-2', (27, 35), (26, 31), radius_x=3, sweep=False)
        self.add_contour('c0', 'e1-1', 'e1-2')
        self.add_contour('c1', 'e2-1', 'e2-2')
        self.add_contour('c2', 'e3-1', 'e3-2')
        self.add_contour('c3', 'e4')
        self.add_contour('c4', 'e5-1', 'e5-2')
        self.add_contour('e0', 'e0-top', 'e0-bottom', closed=True)
