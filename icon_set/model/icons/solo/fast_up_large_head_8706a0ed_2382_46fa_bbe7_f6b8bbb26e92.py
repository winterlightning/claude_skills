"""Fast up large head (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8706a0ed-2382-46fa-bbe7-f6b8bbb26e92'
SOURCE_PATH = 'icons-json/arrows/fast up large head_8706a0ed-2382-46fa-bbe7-f6b8bbb26e92.json'
AUTHOR = 'json_to_solo'

class FastUpLargeHead(Solo48):
    icon_id = 'fast-up-large-head'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('fast', 'up', 'large', 'head', 'arrows')

    def build(self):
        self.add_line('e0', (26, 13), (34, 6))
        self.add_line('e1', (34, 13), (34, 6))
        self.add_line('e2', (42, 14), (34, 6))
        self.add_arc('e3', (6, 42), (34, 13), radius_x=31, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e3', 'e1')
        self.add_contour('c2', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
