"""Redo (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bdd5c523-073c-40e4-bb23-2bca55ba830d'
SOURCE_PATH = 'icons-json/interface-essential/redo_bdd5c523-073c-40e4-bb23-2bca55ba830d.json'
AUTHOR = 'json_to_solo'

class Redo(Solo48):
    icon_id = 'redo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('redo', 'interface-essential')

    def build(self):
        self.add_line('e0', (40, 4), (40, 12))
        self.add_line('e1', (32, 14), (40, 14))
        self.add_line('e2', (40, 12), (40, 14))
        self.add_arc('e3-1', (25, 44), (12, 37), radius_x=17)
        self.add_arc('e3-2', (12, 37), (9, 32), radius_x=20)
        self.add_line('e3-3', (9, 32), (8, 25))
        self.add_arc('e3-4', (8, 25), (9, 19), radius_x=19)
        self.add_arc('e3-5', (9, 19), (11, 14), radius_x=19)
        self.add_arc('e3-6', (11, 14), (23, 6), radius_x=18)
        self.add_arc('e3-7', (23, 6), (40, 14), radius_x=18)
        self.add_contour('c0', 'e0', 'e2')
        self.add_contour('c1', 'e3-1', 'e3-2', 'e3-3', 'e3-4', 'e3-5', 'e3-6', 'e3-7')
        self.add_contour('c2', 'e1')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
