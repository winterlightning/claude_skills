"""Warp shell upper (design), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '318570bf-d868-5293-9426-d9a1090f3879'
SOURCE_PATH = 'icons-json/design/warp shell upper_318570bf-d868-5293-9426-d9a1090f3879.json'
AUTHOR = 'json_to_solo'

class WarpShellUpperDesign(Solo48):
    icon_id = 'warp-shell-upper-design'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('warp', 'shell', 'upper', 'design')

    def build(self):
        self.add_line('e0', (31, 42), (31, 35))
        self.add_line('e1', (38, 26), (42, 26))
        self.add_line('e2', (17, 34), (17, 42))
        self.add_line('e3', (17, 42), (31, 42))
        self.add_arc('e4', (31, 35), (38, 26), radius_x=10)
        self.add_line('e5-1', (42, 26), (41, 18))
        self.add_arc('e5-2', (41, 18), (39, 14), radius_x=18, sweep=False)
        self.add_arc('e5-3', (39, 14), (30, 7), radius_x=18, sweep=False)
        self.add_line('e5-4', (30, 7), (24, 6))
        self.add_arc('e5-5', (24, 6), (6, 24), radius_x=18, sweep=False)
        self.add_line('e5-6', (6, 24), (6, 25))
        self.add_arc('e5-7', (6, 25), (14, 29), radius_x=11)
        self.add_line('e5-8', (14, 29), (17, 34))
        self.add_contour('c0', 'e0', 'e4', 'e1', 'e5-1', 'e5-2', 'e5-3', 'e5-4', 'e5-5', 'e5-6', 'e5-7', 'e5-8', 'e2', 'e3', closed=True)
