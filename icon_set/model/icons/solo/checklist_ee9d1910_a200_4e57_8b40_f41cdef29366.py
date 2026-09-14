"""Checklist (work), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ee9d1910-a200-4e57-8b40-f41cdef29366'
SOURCE_PATH = 'icons-json/work/checklist_ee9d1910-a200-4e57-8b40-f41cdef29366.json'
AUTHOR = 'json_to_solo'

class Checklist(Solo48):
    icon_id = 'checklist'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'work'
    aliases = ()
    keywords = ('checklist', 'work')

    def build(self):
        self.add_line('e0', (22, 13), (16, 20))
        self.add_line('e1', (16, 20), (13, 17))
        self.add_line('e2', (26, 20), (35, 20))
        self.add_line('e3', (22, 26), (16, 32))
        self.add_line('e4', (16, 32), (13, 30))
        self.add_line('e5', (26, 33), (35, 33))
        self.add_line('e6', (40, 6), (8, 6))
        self.add_line('e7', (6, 8), (6, 40))
        self.add_line('e8', (8, 42), (40, 42))
        self.add_line('e9', (42, 40), (42, 8))
        self.add_line('e10', (8, 6), (6, 8))
        self.add_line('e11', (6, 40), (8, 42))
        self.add_line('e12', (40, 42), (42, 40))
        self.add_line('e13', (42, 8), (40, 6))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3', 'e4')
        self.add_contour('c3', 'e5')
        self.add_contour('c4', 'e6', 'e10', 'e7', 'e11', 'e8', 'e12', 'e9', 'e13', closed=True)
