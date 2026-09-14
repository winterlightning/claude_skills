"""Dumbbell (sports), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c7617317-0663-433d-b73d-2bfd2f6407c8'
SOURCE_PATH = 'icons-json/sports/dumbbell_c7617317-0663-433d-b73d-2bfd2f6407c8.json'
AUTHOR = 'json_to_solo'

class DumbbellSports(Solo48):
    icon_id = 'dumbbell-sports'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'sports'
    aliases = ()
    keywords = ('dumbbell', 'sports')

    def build(self):
        self.add_line('e0', (35, 24), (13, 24))
        self.add_line('e1', (4, 38), (4, 10))
        self.add_line('e2', (5, 8), (12, 8))
        self.add_line('e3', (13, 10), (13, 38))
        self.add_line('e4', (12, 40), (5, 40))
        self.add_line('e5', (36, 8), (43, 8))
        self.add_line('e6', (44, 10), (44, 38))
        self.add_line('e7', (43, 40), (36, 40))
        self.add_line('e8', (35, 38), (35, 10))
        self.add_line('e9', (4, 10), (5, 8))
        self.add_arc('e10', (12, 8), (13, 10), radius_x=2)
        self.add_arc('e11', (13, 38), (12, 40), radius_x=2)
        self.add_line('e12', (5, 40), (4, 38))
        self.add_line('e13', (43, 8), (44, 10))
        self.add_line('e14', (44, 38), (43, 40))
        self.add_arc('e15', (36, 40), (35, 38), radius_x=2)
        self.add_arc('e16', (35, 10), (36, 8), radius_x=2)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e9', 'e2', 'e10', 'e3', 'e11', 'e4', 'e12', closed=True)
        self.add_contour('c2', 'e5', 'e13', 'e6', 'e14', 'e7', 'e15', 'e8', 'e16', closed=True)
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c1')
