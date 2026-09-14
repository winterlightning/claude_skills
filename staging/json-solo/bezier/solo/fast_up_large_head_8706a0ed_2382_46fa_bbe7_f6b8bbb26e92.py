"""Fast up large head (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8706a0ed-2382-46fa-bbe7-f6b8bbb26e92'
SOURCE_PATH = 'icons-json/arrows/fast up large head_8706a0ed-2382-46fa-bbe7-f6b8bbb26e92.json'
AUTHOR = 'json_to_solo'

class FastUpLargeHeadArrows(Solo48):
    icon_id = 'fast-up-large-head-arrows'
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
        self.add_bezier('e3', (6, 42), ((6.033, 41.992), (6.074, 41.992), (6.106, 41.984)), ((6.769, 41.984), (7.481, 41.787), (8.127, 41.673)), ((10.238, 41.296), (12.308, 40.732), (14.313, 39.963)), ((23.288, 36.51), (29.834, 29.539), (32.615, 20.335)), ((33.262, 18.207), (34, 15.225), (34, 13)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e3', 'e1')
        self.add_contour('c2', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
