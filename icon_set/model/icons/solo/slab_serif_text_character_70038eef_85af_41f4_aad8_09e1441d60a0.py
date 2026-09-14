"""Slab serif text character (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '70038eef-85af-41f4-aad8-09e1441d60a0'
SOURCE_PATH = 'icons-json/interface-essential/slab serif text character_70038eef-85af-41f4-aad8-09e1441d60a0.json'
AUTHOR = 'json_to_solo'

class SlabSerifTextCharacter(Solo48):
    icon_id = 'slab-serif-text-character'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('slab', 'serif', 'text', 'character', 'interface-essential')

    def build(self):
        self.add_line('e0', (8, 4), (11, 4))
        self.add_line('e1', (8, 44), (11, 44))
        self.add_line('e2', (13, 44), (11, 44))
        self.add_line('e3', (35, 44), (37, 44))
        self.add_line('e4', (40, 44), (37, 44))
        self.add_line('e5', (40, 4), (37, 4))
        self.add_line('e6', (11, 44), (11, 4))
        self.add_line('e7', (11, 4), (14, 4))
        self.add_line('e8', (14, 4), (24, 30))
        self.add_line('e9', (24, 30), (34, 5))
        self.add_line('e10', (35, 4), (37, 4))
        self.add_line('e11', (37, 44), (37, 4))
        self.add_arc('e12', (34, 5), (35, 4), radius_x=2)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.add_contour('c5', 'e5')
        self.add_contour('c6', 'e6')
        self.add_contour('c7', 'e7', 'e8', 'e9', 'e12', 'e10')
        self.add_contour('c8', 'e11')
        self.relate('connect', 'c0', 'c6')
        self.relate('connect', 'c0', 'c7')
        self.relate('connect', 'c6', 'c7')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c6')
        self.relate('connect', 'c2', 'c6')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c8')
        self.relate('connect', 'c4', 'c8')
        self.relate('connect', 'c5', 'c7')
        self.relate('connect', 'c5', 'c8')
        self.relate('connect', 'c7', 'c8')
