"""Chick (animals), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4cda3eae-34c4-5ab8-a48f-adebd3cb4042'
SOURCE_PATH = 'icons-json/animals/chick_4cda3eae-34c4-5ab8-a48f-adebd3cb4042.json'
AUTHOR = 'json_to_solo'

class Chick(Solo48):
    icon_id = 'chick'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ()
    keywords = ('chick', 'animals')

    def build(self):
        self.add_line('e0', (23, 25), (14, 25))
        self.add_line('e1', (41, 16), (44, 19))
        self.add_line('e2', (44, 14), (41, 16))
        self.add_arc('e3-1', (41, 16), (38, 10), radius_x=8, sweep=False)
        self.add_arc('e3-2', (38, 10), (32, 8), radius_x=10, sweep=False)
        self.add_arc('e3-3', (32, 8), (24, 13), radius_x=9, sweep=False)
        self.add_arc('e3-4', (24, 13), (26, 22), radius_x=8, sweep=False)
        self.add_arc('e3-5', (26, 22), (23, 25), radius_x=4)
        self.add_arc('e4-1', (14, 25), (9, 20), radius_x=5)
        self.add_arc('e4-2', (9, 20), (5, 23), radius_x=5, sweep=False)
        self.add_arc('e4-3', (5, 23), (4, 26), radius_x=5, sweep=False)
        self.add_line('e4-4', (4, 26), (4, 28))
        self.add_arc('e4-5', (4, 28), (9, 36), radius_x=11, sweep=False)
        self.add_arc('e4-6', (9, 36), (21, 40), radius_x=20, sweep=False)
        self.add_line('e4-7', (21, 40), (27, 39))
        self.add_arc('e4-8', (27, 39), (34, 35), radius_x=19, sweep=False)
        self.add_arc('e4-9', (34, 35), (38, 28), radius_x=16, sweep=False)
        self.add_line('e4-10', (38, 28), (38, 22))
        self.add_arc('e4-11', (38, 22), (41, 16), radius_x=9, sweep=False)
        self.add_contour('c0', 'e3-1', 'e3-2', 'e3-3', 'e3-4', 'e3-5', 'e0', 'e4-1', 'e4-2', 'e4-3', 'e4-4', 'e4-5', 'e4-6', 'e4-7', 'e4-8', 'e4-9', 'e4-10', 'e4-11', 'e1')
        self.add_contour('c1', 'e2')
