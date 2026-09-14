"""Focus close (photography), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7619190d-943a-49eb-bd67-270ef4c1b668'
SOURCE_PATH = 'icons-json/photography/focus close_7619190d-943a-49eb-bd67-270ef4c1b668.json'
AUTHOR = 'json_to_solo'

class FocusClosePhotography(Solo48):
    icon_id = 'focus-close-photography'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'photography'
    aliases = ()
    keywords = ('focus', 'close', 'photography')

    def build(self):
        self.add_line('e0', (6, 13), (6, 8))
        self.add_line('e1', (8, 6), (13, 6))
        self.add_line('e2', (35, 6), (40, 6))
        self.add_line('e3', (42, 8), (42, 13))
        self.add_line('e4', (35, 42), (40, 42))
        self.add_line('e5', (42, 40), (42, 35))
        self.add_line('e6', (6, 35), (6, 40))
        self.add_line('e7', (8, 42), (13, 42))
        self.add_arc('e8-top', (13, 24), (35, 24), radius_x=11)
        self.add_arc('e8-bottom', (35, 24), (13, 24), radius_x=11)
        self.add_arc('e9', (6, 8), (8, 6), radius_x=2)
        self.add_arc('e10', (40, 6), (42, 8), radius_x=2)
        self.add_arc('e11', (40, 42), (42, 40), radius_x=2, sweep=False)
        self.add_arc('e12', (6, 40), (8, 42), radius_x=2, sweep=False)
        self.add_contour('c0', 'e0', 'e9', 'e1')
        self.add_contour('c1', 'e2', 'e10', 'e3')
        self.add_contour('c2', 'e4', 'e11', 'e5')
        self.add_contour('c3', 'e6', 'e12', 'e7')
        self.add_contour('e8', 'e8-top', 'e8-bottom', closed=True)
