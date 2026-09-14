"""Fall fast large head (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'aa929e50-8583-4e74-a3ad-c02b3ca337cf'
SOURCE_PATH = 'icons-json/arrows/fall fast large head_aa929e50-8583-4e74-a3ad-c02b3ca337cf.json'
AUTHOR = 'json_to_solo'

class FallFastLargeHeadArrows(Solo48):
    icon_id = 'fall-fast-large-head-arrows'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('fall', 'fast', 'large', 'head', 'arrows')

    def build(self):
        self.add_line('e0', (6, 6), (6, 14))
        self.add_line('e1', (13, 20), (26, 20))
        self.add_line('e2', (35, 27), (35, 42))
        self.add_line('e3', (26, 35), (35, 42))
        self.add_line('e4', (42, 35), (35, 42))
        self.add_bezier('e5', (6, 14), ((6, 16.757), (9.281, 19.124), (11.662, 19.688)), ((11.907, 19.745), (12.763, 20), (13, 20)))
        self.add_bezier('e6', (26, 20), ((26.245, 20), (27.076, 20.056), (27.33, 20.114)), ((30.284, 20.744), (33.221, 22.912), (34.276, 25.8)), ((34.44, 26.234), (35, 26.534), (35, 27)))
        self.add_contour('c0', 'e0', 'e5', 'e1', 'e6', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
