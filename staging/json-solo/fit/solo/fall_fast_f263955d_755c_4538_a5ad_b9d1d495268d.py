"""Fall fast (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
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
        self.add_arc('e5', (4, 14), (10, 20), radius_x=7, sweep=False)
        self.add_arc('e6', (31, 20), (38, 26), radius_x=7)
        self.add_contour('c0', 'e0', 'e5', 'e1', 'e6', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
