"""Down large head (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2d9f7f27-8487-48e9-93e7-03bb61aa7349'
SOURCE_PATH = 'icons-json/arrows/down large head_2d9f7f27-8487-48e9-93e7-03bb61aa7349.json'
AUTHOR = 'json_to_solo'

class DownLargeHead(Solo48):
    icon_id = 'down-large-head'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('down', 'large', 'head', 'arrows')

    def build(self):
        self.add_line('e0', (33, 34), (42, 34))
        self.add_line('e1', (34, 42), (42, 34))
        self.add_line('e2', (34, 25), (42, 34))
        self.add_arc('e3', (6, 6), (33, 34), radius_x=29, sweep=False)
        self.add_contour('c0', 'e3', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
