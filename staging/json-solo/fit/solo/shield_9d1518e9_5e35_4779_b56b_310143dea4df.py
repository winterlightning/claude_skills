"""Shield (protection), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9d1518e9-5e35-4779-b56b-310143dea4df'
SOURCE_PATH = 'icons-json/protection/shield_9d1518e9-5e35-4779-b56b-310143dea4df.json'
AUTHOR = 'json_to_solo'

class Shield(Solo48):
    icon_id = 'shield'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'protection'
    aliases = ()
    keywords = ('shield', 'protection')

    def build(self):
        self.add_line('e0', (24, 4), (28, 7))
        self.add_arc('e1-1', (24, 44), (11, 28), radius_x=34)
        self.add_arc('e1-2', (11, 28), (9, 22), radius_x=37)
        self.add_line('e1-3', (9, 22), (8, 12))
        self.add_line('e1-4', (8, 12), (8, 11))
        self.add_arc('e1-5', (8, 11), (24, 4), radius_x=40, sweep=False)
        self.add_arc('e2-1', (28, 7), (38, 10), radius_x=31, sweep=False)
        self.add_arc('e2-2', (38, 10), (40, 12), radius_x=2)
        self.add_line('e2-3', (40, 12), (38, 25))
        self.add_arc('e2-4', (38, 25), (34, 34), radius_x=36)
        self.add_arc('e2-5', (34, 34), (24, 44), radius_x=35)
        self.add_contour('c0', 'e1-1', 'e1-2', 'e1-3', 'e1-4', 'e1-5', 'e0', 'e2-1', 'e2-2', 'e2-3', 'e2-4', 'e2-5')
