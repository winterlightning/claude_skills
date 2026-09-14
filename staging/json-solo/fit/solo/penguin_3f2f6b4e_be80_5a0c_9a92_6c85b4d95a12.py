"""Penguin (animals), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3f2f6b4e-be80-5a0c-9a92-6c85b4d95a12'
SOURCE_PATH = 'icons-json/animals/penguin_3f2f6b4e-be80-5a0c-9a92-6c85b4d95a12.json'
AUTHOR = 'json_to_solo'

class Penguin(Solo48):
    icon_id = 'penguin'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ()
    keywords = ('penguin', 'animals')

    def build(self):
        self.add_line('e0', (19, 25), (19, 29))
        self.add_line('e1', (33, 14), (33, 37))
        self.add_line('e2', (37, 44), (11, 44))
        self.add_line('e3', (37, 44), (40, 44))
        self.add_arc('e4', (17, 20), (16, 44), radius_x=18, sweep=False)
        self.add_line('e5', (17, 20), (19, 25))
        self.add_arc('e6', (19, 29), (25, 39), radius_x=10, sweep=False)
        self.add_arc('e7', (17, 20), (8, 19), radius_x=11, sweep=False)
        self.add_arc('e8-1', (13, 14), (16, 7), radius_x=12)
        self.add_arc('e8-2', (16, 7), (19, 5), radius_x=11)
        self.add_line('e8-3', (19, 5), (24, 4))
        self.add_arc('e8-4', (24, 4), (33, 14), radius_x=10)
        self.add_arc('e9', (33, 37), (37, 44), radius_x=11, sweep=False)
        self.add_arc('e10', (13, 14), (8, 19), radius_x=9, sweep=False)
        self.add_contour('c0', 'e4')
        self.add_contour('c1', 'e5', 'e0', 'e6')
        self.add_contour('c2', 'e7')
        self.add_contour('c3', 'e8-1', 'e8-2', 'e8-3', 'e8-4', 'e1', 'e9', 'e2')
        self.add_contour('c4', 'e10')
        self.add_contour('c5', 'e3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c3')
