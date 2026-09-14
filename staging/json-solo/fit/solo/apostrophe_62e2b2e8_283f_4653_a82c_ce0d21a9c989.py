"""Apostrophe (_uncategorized_03), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '62e2b2e8-283f-4653-a82c-ce0d21a9c989'
SOURCE_PATH = 'icons-json/_uncategorized_03/apostrophe_62e2b2e8-283f-4653-a82c-ce0d21a9c989.json'
AUTHOR = 'json_to_solo'

class ApostropheUncategorized03(Solo48):
    icon_id = 'apostrophe-uncategorized-03'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized_03'
    aliases = ()
    keywords = ('apostrophe', '_uncategorized_03')

    def build(self):
        self.add_line('e0', (15, 38), (10, 40))
        self.add_line('e1', (18, 23), (23, 24))
        self.add_line('e2-1', (10, 40), (10, 43))
        self.add_line('e2-2', (10, 43), (13, 44))
        self.add_arc('e2-3', (13, 44), (40, 18), radius_x=29, sweep=False)
        self.add_line('e2-4', (40, 18), (39, 12))
        self.add_arc('e2-5', (39, 12), (35, 7), radius_x=11, sweep=False)
        self.add_arc('e2-6', (35, 7), (31, 5), radius_x=14, sweep=False)
        self.add_line('e2-7', (31, 5), (24, 4))
        self.add_line('e2-8', (24, 4), (14, 6))
        self.add_arc('e2-9', (14, 6), (8, 15), radius_x=10, sweep=False)
        self.add_arc('e2-10', (8, 15), (18, 23), radius_x=9, sweep=False)
        self.add_arc('e3-1', (23, 24), (23, 31), radius_x=4)
        self.add_arc('e3-2', (23, 31), (15, 38), radius_x=25)
        self.add_contour('c0', 'e0', 'e2-1', 'e2-2', 'e2-3', 'e2-4', 'e2-5', 'e2-6', 'e2-7', 'e2-8', 'e2-9', 'e2-10', 'e1', 'e3-1', 'e3-2', closed=True)
