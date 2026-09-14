"""Down (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2fd40d0d-8574-4fc3-982c-2bfce5c820d1'
SOURCE_PATH = 'icons-json/arrows/down_2fd40d0d-8574-4fc3-982c-2bfce5c820d1.json'
AUTHOR = 'json_to_solo'

class Down(Solo48):
    icon_id = 'down'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('down', 'arrows')

    def build(self):
        self.add_line('sym-e0', (6, 6), (23, 24))
        self.add_arc('sym-e1', (23, 24), (24, 24), radius_x=1, sweep=False)
        self.add_arc('sym-e2', (24, 24), (25, 24), radius_x=1, sweep=False)
        self.add_line('sym-e3', (25, 24), (42, 6))
        self.add_line('sym-e4', (6, 24), (23, 42))
        self.add_arc('sym-e5', (23, 42), (24, 42), radius_x=27)
        self.add_arc('sym-e8', (24, 42), (25, 42), radius_x=29)
        self.add_line('sym-e9', (25, 42), (42, 24))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3')
        self.add_contour('sym-c1', 'sym-e4', 'sym-e5', 'sym-e8', 'sym-e9')
