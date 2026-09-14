"""Dash wave down large head (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '811e8d54-369b-424d-a542-04d91cebc791'
SOURCE_PATH = 'icons-json/arrows/dash wave down large head_811e8d54-369b-424d-a542-04d91cebc791.json'
AUTHOR = 'json_to_solo'

class DashWaveDownLargeHead(Solo48):
    icon_id = 'dash-wave-down-large-head'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('dash', 'wave', 'down', 'large', 'head', 'arrows')

    def build(self):
        self.add_line('e0', (12, 11), (12, 35))
        self.add_line('e1', (27, 35), (27, 11))
        self.add_line('e2', (38, 11), (38, 26))
        self.add_line('e3', (33, 22), (38, 26))
        self.add_line('e4', (42, 22), (38, 26))
        self.add_arc('e5-1', (6, 6), (8, 6), radius_x=8, sweep=False)
        self.add_arc('e5-2', (8, 6), (11, 9), radius_x=6)
        self.add_arc('e5-3', (11, 9), (12, 11), radius_x=10, sweep=False)
        self.add_arc('e6-1', (12, 35), (19, 42), radius_x=7, sweep=False)
        self.add_arc('e6-2', (19, 42), (27, 35), radius_x=9, sweep=False)
        self.add_arc('e7-1', (27, 11), (33, 6), radius_x=7)
        self.add_arc('e7-2', (33, 6), (38, 11), radius_x=6)
        self.add_arc('e8', (42, 21), (42, 22), radius_x=26, sweep=False)
        self.add_contour('c0', 'e5-1', 'e5-2', 'e5-3', 'e0', 'e6-1', 'e6-2', 'e1', 'e7-1', 'e7-2', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e8', 'e4')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
