"""Curve up (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7d4b64cd-a567-41af-a620-5444017a5033'
SOURCE_PATH = 'icons-json/arrows/curve up_7d4b64cd-a567-41af-a620-5444017a5033.json'
AUTHOR = 'json_to_solo'

class CurveUp7d4b64cd(Solo48):
    icon_id = 'curve-up-7d4b64cd'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('curve', 'up', 'arrows')

    def build(self):
        self.add_line('e0', (38, 6), (42, 11))
        self.add_line('e1', (6, 6), (6, 33))
        self.add_line('e2', (25, 33), (25, 20))
        self.add_line('e3', (33, 11), (42, 11))
        self.add_line('e4', (38, 16), (42, 11))
        self.add_arc('e5-1', (6, 33), (15, 42), radius_x=9, sweep=False)
        self.add_line('e5-2', (15, 42), (21, 40))
        self.add_arc('e5-3', (21, 40), (25, 33), radius_x=11, sweep=False)
        self.add_arc('e6', (25, 20), (33, 11), radius_x=9)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e5-1', 'e5-2', 'e5-3', 'e2', 'e6', 'e3')
        self.add_contour('c2', 'e4')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
