"""Lift hook box (construction), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c368d189-0003-5241-889d-bf5b16aa99f6'
SOURCE_PATH = 'icons-json/construction/lift hook box_c368d189-0003-5241-889d-bf5b16aa99f6.json'
AUTHOR = 'json_to_solo'

class LiftHookBoxConstruction(Solo48):
    icon_id = 'lift-hook-box-construction'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'construction'
    aliases = ()
    keywords = ('lift', 'hook', 'box', 'construction')

    def build(self):
        self.add_line('e0', (12, 23), (40, 23))
        self.add_line('e1', (40, 23), (40, 44))
        self.add_line('e2', (40, 44), (8, 44))
        self.add_line('e3', (8, 44), (8, 23))
        self.add_line('e4', (8, 23), (16, 23))
        self.add_line('e5', (35, 23), (24, 10))
        self.add_line('e6', (24, 10), (13, 23))
        self.add_line('e7', (24, 4), (24, 10))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', 'e4')
        self.add_contour('c1', 'e5', 'e6')
        self.add_contour('c2', 'e7')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c0')
