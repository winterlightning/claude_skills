"""Play with slider (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b4c8a75d-f284-4a2b-9369-60ef9f7907dc'
SOURCE_PATH = 'icons-json/symbol/play with slider_b4c8a75d-f284-4a2b-9369-60ef9f7907dc.json'
AUTHOR = 'json_to_solo'

class PlayWithSliderSymbol(Solo48):
    icon_id = 'play-with-slider-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('play', 'with', 'slider', 'symbol')

    def build(self):
        self.add_line('e0', (30, 35), (30, 42))
        self.add_line('e1', (6, 39), (42, 39))
        self.add_line('e2', (36, 19), (15, 6))
        self.add_line('e3', (15, 6), (15, 31))
        self.add_line('e4', (15, 31), (36, 19))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e3', 'e4', closed=True)
