"""Dressing hanger (furnitures), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3bd96682-b5d1-5b3b-b906-7bd98211e403'
SOURCE_PATH = 'icons-json/furnitures/dressing hanger_3bd96682-b5d1-5b3b-b906-7bd98211e403.json'
AUTHOR = 'json_to_solo'

class DressingHanger(Solo48):
    icon_id = 'dressing-hanger'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'furnitures'
    aliases = ()
    keywords = ('dressing', 'hanger', 'furnitures')

    def build(self):
        self.add_line('e0', (24, 18), (24, 22))
        self.add_line('e1', (24, 22), (6, 34))
        self.add_line('e2', (7, 40), (40, 40))
        self.add_line('e3', (42, 34), (24, 22))
        self.add_arc('e4-1', (19, 13), (24, 8), radius_x=5)
        self.add_arc('e4-2', (24, 8), (28, 13), radius_x=5)
        self.add_arc('e4-3', (28, 13), (24, 18), radius_x=6)
        self.add_arc('e5-1', (6, 34), (4, 37), radius_x=4, sweep=False)
        self.add_arc('e5-2', (4, 37), (7, 40), radius_x=3, sweep=False)
        self.add_line('e6-1', (40, 40), (43, 39))
        self.add_arc('e6-2', (43, 39), (44, 37), radius_x=3, sweep=False)
        self.add_arc('e6-3', (44, 37), (42, 34), radius_x=4, sweep=False)
        self.add_contour('c0', 'e4-1', 'e4-2', 'e4-3', 'e0')
        self.add_contour('c1', 'e1', 'e5-1', 'e5-2', 'e2', 'e6-1', 'e6-2', 'e6-3', 'e3')
