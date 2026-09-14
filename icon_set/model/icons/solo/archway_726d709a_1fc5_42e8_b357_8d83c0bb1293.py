"""Archway (_uncategorized_04), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '726d709a-1fc5-42e8-b357-8d83c0bb1293'
SOURCE_PATH = 'icons-json/_uncategorized_04/archway_726d709a-1fc5-42e8-b357-8d83c0bb1293.json'
AUTHOR = 'json_to_solo'

class Archway(Solo48):
    icon_id = 'archway'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized_04'
    aliases = ()
    keywords = ('archway', '_uncategorized_04')

    def build(self):
        self.add_line('e0', (13, 42), (7, 42))
        self.add_line('e1', (6, 41), (6, 22))
        self.add_line('e2', (42, 22), (42, 41))
        self.add_line('e3', (41, 42), (35, 42))
        self.add_line('e4', (34, 41), (34, 23))
        self.add_line('e5', (14, 23), (14, 41))
        self.add_arc('e6', (7, 42), (6, 41), radius_x=1)
        self.add_arc('e7-1', (6, 22), (24, 6), radius_x=19)
        self.add_arc('e7-2', (24, 6), (42, 22), radius_x=19)
        self.add_arc('e8', (42, 41), (41, 42), radius_x=1)
        self.add_line('e9', (35, 42), (34, 41))
        self.add_arc('e10-1', (34, 23), (22, 14), radius_x=10, sweep=False)
        self.add_arc('e10-2', (22, 14), (14, 23), radius_x=11, sweep=False)
        self.add_arc('e11', (14, 41), (13, 42), radius_x=2, sweep=False)
        self.add_contour('c0', 'e0', 'e6', 'e1', 'e7-1', 'e7-2', 'e2', 'e8', 'e3', 'e9', 'e4', 'e10-1', 'e10-2', 'e5', 'e11', closed=True)
