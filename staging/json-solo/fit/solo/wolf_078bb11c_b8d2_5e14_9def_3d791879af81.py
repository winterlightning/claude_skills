"""Wolf (animals), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '078bb11c-b8d2-5e14-9def-3d791879af81'
SOURCE_PATH = 'icons-json/animals/wolf_078bb11c-b8d2-5e14-9def-3d791879af81.json'
AUTHOR = 'json_to_solo'

class Wolf(Solo48):
    icon_id = 'wolf'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ()
    keywords = ('wolf', 'animals')

    def build(self):
        self.add_line('e0', (26, 6), (26, 13))
        self.add_line('e1', (35, 22), (42, 25))
        self.add_line('e2', (35, 31), (30, 30))
        self.add_arc('e3-1', (6, 26), (18, 14), radius_x=30)
        self.add_line('e3-2', (18, 14), (19, 11))
        self.add_arc('e3-3', (19, 11), (26, 6), radius_x=9)
        self.add_line('e4-1', (26, 13), (30, 15))
        self.add_line('e4-2', (30, 15), (35, 22))
        self.add_arc('e5', (42, 25), (35, 31), radius_x=7)
        self.add_arc('e6', (30, 30), (25, 42), radius_x=8, sweep=False)
        self.add_contour('c0', 'e3-1', 'e3-2', 'e3-3', 'e0', 'e4-1', 'e4-2', 'e1', 'e5', 'e2', 'e6')
