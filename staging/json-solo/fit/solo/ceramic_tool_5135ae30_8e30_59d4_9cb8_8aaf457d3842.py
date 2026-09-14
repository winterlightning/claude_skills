"""Ceramic tool (hobbies), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5135ae30-8e30-59d4-9cb8-8aaf457d3842'
SOURCE_PATH = 'icons-json/hobbies/ceramic tool_5135ae30-8e30-59d4-9cb8-8aaf457d3842.json'
AUTHOR = 'json_to_solo'

class CeramicToolHobbies(Solo48):
    icon_id = 'ceramic-tool-hobbies'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'hobbies'
    aliases = ()
    keywords = ('ceramic', 'tool', 'hobbies')

    def build(self):
        self.add_line('e0', (37, 18), (33, 14))
        self.add_arc('e1-1', (33, 14), (34, 5), radius_x=7)
        self.add_arc('e1-2', (34, 5), (34, 4), radius_x=1, sweep=False)
        self.add_line('e1-3', (34, 4), (21, 4))
        self.add_arc('e1-4', (21, 4), (14, 4), radius_x=71)
        self.add_arc('e1-5', (14, 4), (14, 5), radius_x=1, sweep=False)
        self.add_arc('e1-6', (14, 5), (16, 12), radius_x=8)
        self.add_arc('e1-7', (16, 12), (10, 19), radius_x=19)
        self.add_arc('e1-8', (10, 19), (8, 24), radius_x=10, sweep=False)
        self.add_arc('e1-9', (8, 24), (15, 41), radius_x=30, sweep=False)
        self.add_arc('e1-10', (15, 41), (18, 44), radius_x=5, sweep=False)
        self.add_arc('e1-11', (18, 44), (23, 44), radius_x=32)
        self.add_line('e1-12', (23, 44), (29, 44))
        self.add_arc('e1-13', (29, 44), (33, 41), radius_x=5, sweep=False)
        self.add_arc('e1-14', (33, 41), (40, 25), radius_x=34, sweep=False)
        self.add_arc('e1-15', (40, 25), (37, 18), radius_x=12, sweep=False)
        self.add_contour('c0', 'e0', 'e1-1', 'e1-2', 'e1-3', 'e1-4', 'e1-5', 'e1-6', 'e1-7', 'e1-8', 'e1-9', 'e1-10', 'e1-11', 'e1-12', 'e1-13', 'e1-14', 'e1-15', closed=True)
