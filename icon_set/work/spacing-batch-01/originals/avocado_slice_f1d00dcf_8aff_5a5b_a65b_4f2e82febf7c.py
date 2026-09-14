"""Avocado slice (food), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f1d00dcf-8aff-5a5b-a65b-4f2e82febf7c'
SOURCE_PATH = 'icons-json/food/avocado slice_f1d00dcf-8aff-5a5b-a65b-4f2e82febf7c.json'
AUTHOR = 'json_to_solo'

class AvocadoSlice(Solo48):
    icon_id = 'avocado-slice'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('avocado', 'slice', 'food')

    def build(self):
        self.add_arc('e0-1', (35, 39), (23, 44), radius_x=17)
        self.add_arc('e0-2', (23, 44), (8, 29), radius_x=15)
        self.add_line('e0-3', (8, 29), (9, 24))
        self.add_line('e0-4', (9, 24), (17, 7))
        self.add_arc('e0-5', (17, 7), (20, 5), radius_x=9)
        self.add_arc('e0-6', (20, 5), (24, 4), radius_x=9)
        self.add_arc('e0-7', (24, 4), (32, 9), radius_x=9)
        self.add_arc('e0-8', (32, 9), (39, 24), radius_x=48, sweep=False)
        self.add_arc('e0-9', (39, 24), (40, 29), radius_x=13)
        self.add_arc('e0-10', (40, 29), (35, 39), radius_x=13)
        self.add_arc('e1-1', (31, 27), (23, 20), radius_x=8, sweep=False)
        self.add_arc('e1-2', (23, 20), (17, 31), radius_x=10, sweep=False)
        self.add_arc('e1-3', (17, 31), (24, 36), radius_x=7, sweep=False)
        self.add_arc('e1-4', (24, 36), (31, 27), radius_x=7, sweep=False)
        self.add_contour('c0', 'e0-1', 'e0-2', 'e0-3', 'e0-4', 'e0-5', 'e0-6', 'e0-7', 'e0-8', 'e0-9', 'e0-10', closed=True)
        self.add_contour('c1', 'e1-1', 'e1-2', 'e1-3', 'e1-4', closed=True)
