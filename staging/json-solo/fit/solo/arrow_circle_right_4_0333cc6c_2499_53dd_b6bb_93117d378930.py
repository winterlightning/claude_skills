"""Arrow circle right 4 (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0333cc6c-2499-53dd-b6bb-93117d378930'
SOURCE_PATH = 'icons-json/arrows/arrow circle right 4_0333cc6c-2499-53dd-b6bb-93117d378930.json'
AUTHOR = 'json_to_solo'

class ArrowCircleRight4Arrows(Solo48):
    icon_id = 'arrow-circle-right-4-arrows'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'circle', 'right', 'arrows')

    def build(self):
        self.add_line('e0', (35, 24), (7, 24))
        self.add_line('e1', (35, 24), (26, 34))
        self.add_line('e2', (35, 24), (26, 15))
        self.add_arc('e3-1', (7, 24), (6, 25), radius_x=1, sweep=False)
        self.add_arc('e3-2', (6, 25), (23, 42), radius_x=18, sweep=False)
        self.add_arc('e3-3', (23, 42), (38, 35), radius_x=20, sweep=False)
        self.add_arc('e3-4', (38, 35), (41, 30), radius_x=17, sweep=False)
        self.add_line('e3-5', (41, 30), (42, 24))
        self.add_line('e3-6', (42, 24), (41, 18))
        self.add_arc('e3-7', (41, 18), (39, 14), radius_x=16, sweep=False)
        self.add_arc('e3-8', (39, 14), (23, 6), radius_x=20, sweep=False)
        self.add_line('e3-9', (23, 6), (15, 8))
        self.add_line('e3-10', (15, 8), (12, 10))
        self.add_arc('e3-11', (12, 10), (7, 20), radius_x=17, sweep=False)
        self.add_contour('c0', 'e0', 'e3-1', 'e3-2', 'e3-3', 'e3-4', 'e3-5', 'e3-6', 'e3-7', 'e3-8', 'e3-9', 'e3-10', 'e3-11')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
