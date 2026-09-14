"""Lower steady (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '64a3ba6a-5e3e-4e12-a04c-b8e6de012c65'
SOURCE_PATH = 'icons-json/arrows/lower steady_64a3ba6a-5e3e-4e12-a04c-b8e6de012c65.json'
AUTHOR = 'json_to_solo'

class LowerSteady(Solo48):
    icon_id = 'lower-steady'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('lower', 'steady', 'arrows')

    def build(self):
        self.add_line('e0', (6, 6), (6, 36))
        self.add_line('e1', (20, 36), (20, 26))
        self.add_line('e2', (25, 21), (42, 21))
        self.add_line('e3', (37, 26), (42, 21))
        self.add_line('e4', (37, 17), (42, 21))
        self.add_arc('e5-1', (6, 36), (13, 42), radius_x=8, sweep=False)
        self.add_arc('e5-2', (13, 42), (20, 36), radius_x=8, sweep=False)
        self.add_arc('e6', (20, 26), (25, 21), radius_x=5)
        self.add_contour('c0', 'e0', 'e5-1', 'e5-2', 'e1', 'e6', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
