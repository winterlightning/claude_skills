"""Arrow circle left 4 (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '71c91594-3568-5185-a426-59b87ba667ee'
SOURCE_PATH = 'icons-json/arrows/arrow circle left 4_71c91594-3568-5185-a426-59b87ba667ee.json'
AUTHOR = 'json_to_solo'

class ArrowCircleLeft4Arrows(Solo48):
    icon_id = 'arrow-circle-left-4-arrows'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'circle', 'left', 'arrows')

    def build(self):
        self.add_line('e0', (13, 24), (41, 24))
        self.add_line('e1', (13, 24), (22, 14))
        self.add_line('e2', (13, 24), (22, 34))
        self.add_arc('e3-1', (41, 24), (42, 23), radius_x=1, sweep=False)
        self.add_arc('e3-2', (42, 23), (25, 6), radius_x=18, sweep=False)
        self.add_arc('e3-3', (25, 6), (10, 13), radius_x=20, sweep=False)
        self.add_arc('e3-4', (10, 13), (7, 18), radius_x=17, sweep=False)
        self.add_line('e3-5', (7, 18), (6, 24))
        self.add_line('e3-6', (6, 24), (7, 30))
        self.add_arc('e3-7', (7, 30), (9, 34), radius_x=16, sweep=False)
        self.add_arc('e3-8', (9, 34), (25, 42), radius_x=20, sweep=False)
        self.add_line('e3-9', (25, 42), (33, 40))
        self.add_line('e3-10', (33, 40), (36, 38))
        self.add_arc('e3-11', (36, 38), (41, 28), radius_x=17, sweep=False)
        self.add_contour('c0', 'e0', 'e3-1', 'e3-2', 'e3-3', 'e3-4', 'e3-5', 'e3-6', 'e3-7', 'e3-8', 'e3-9', 'e3-10', 'e3-11')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
