"""Flower (nature), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6a1ecbd5-e710-49ac-8aeb-04d4c78b521a'
SOURCE_PATH = 'icons-json/nature/flower_6a1ecbd5-e710-49ac-8aeb-04d4c78b521a.json'
AUTHOR = 'json_to_solo'

class Flower6a1ecbd5(Solo48):
    icon_id = 'flower-6a1ecbd5'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature'
    aliases = ()
    keywords = ('flower', 'nature')

    def build(self):
        self.add_arc('e0-1', (31, 14), (42, 22), radius_x=9)
        self.add_arc('e0-2', (42, 22), (37, 29), radius_x=8)
        self.add_arc('e0-3', (37, 29), (36, 30), radius_x=1, sweep=False)
        self.add_arc('e0-4', (36, 30), (37, 37), radius_x=8)
        self.add_arc('e0-5', (37, 37), (36, 39), radius_x=8)
        self.add_line('e0-6', (36, 39), (34, 41))
        self.add_line('e0-7', (34, 41), (30, 42))
        self.add_arc('e0-8', (30, 42), (24, 39), radius_x=8)
        self.add_arc('e0-9', (24, 39), (18, 42), radius_x=9)
        self.add_line('e0-10', (18, 42), (14, 41))
        self.add_arc('e0-11', (14, 41), (12, 39), radius_x=7)
        self.add_arc('e0-12', (12, 39), (12, 30), radius_x=7)
        self.add_arc('e0-13', (12, 30), (6, 22), radius_x=9)
        self.add_arc('e0-14', (6, 22), (17, 15), radius_x=8)
        self.add_arc('e1-1', (31, 14), (24, 6), radius_x=8, sweep=False)
        self.add_arc('e1-2', (24, 6), (17, 15), radius_x=8, sweep=False)
        self.add_contour('c0', 'e0-1', 'e0-2', 'e0-3', 'e0-4', 'e0-5', 'e0-6', 'e0-7', 'e0-8', 'e0-9', 'e0-10', 'e0-11', 'e0-12', 'e0-13', 'e0-14')
        self.add_contour('c1', 'e1-1', 'e1-2')
