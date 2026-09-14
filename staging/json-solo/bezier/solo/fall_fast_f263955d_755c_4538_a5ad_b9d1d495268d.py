"""Fall fast (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f263955d-755c-4538-a5ad-b9d1d495268d'
SOURCE_PATH = 'icons-json/arrows/fall fast_f263955d-755c-4538-a5ad-b9d1d495268d.json'
AUTHOR = 'json_to_solo'

class FallFastArrows(Solo48):
    icon_id = 'fall-fast-arrows'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('fall', 'fast', 'arrows')

    def build(self):
        self.add_line('e0', (4, 8), (4, 14))
        self.add_line('e1', (10, 20), (31, 20))
        self.add_line('e2', (38, 26), (38, 40))
        self.add_line('e3', (32, 35), (38, 40))
        self.add_line('e4', (44, 35), (38, 40))
        self.add_bezier('e5', (4, 14), ((4, 16.762), (6.664, 18.888), (9.355, 19.562)), ((9.627, 19.629), (9.727, 20), (10, 20)))
        self.add_bezier('e6', (31, 20), ((31.209, 20), (31.845, 19.924), (32.064, 19.975)), ((34.6, 20.531), (36.782, 22.442), (37.409, 24.808)), ((37.482, 25.061), (38, 25.747), (38, 26)))
        self.add_contour('c0', 'e0', 'e5', 'e1', 'e6', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
