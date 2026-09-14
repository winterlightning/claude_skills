"""Down large head (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2d9f7f27-8487-48e9-93e7-03bb61aa7349'
SOURCE_PATH = 'icons-json/arrows/down large head_2d9f7f27-8487-48e9-93e7-03bb61aa7349.json'
AUTHOR = 'json_to_solo'

class DownLargeHeadArrows(Solo48):
    icon_id = 'down-large-head-arrows'
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
        self.add_bezier('e3', (6, 6), ((6, 6.074), (6.008, 6.147), (6.008, 6.213)), ((6.008, 8.193), (6.524, 10.304), (6.982, 12.218)), ((9.256, 21.685), (15.965, 29.506), (25.301, 32.509)), ((27.764, 33.303), (30.398, 34), (33, 34)))
        self.add_contour('c0', 'e3', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
