"""Batch-04/cd broken (computers), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '35902389-7674-5992-88ac-62b704c11f7f'
SOURCE_PATH = 'icons-json/computers/batch-04/cd broken_35902389-7674-5992-88ac-62b704c11f7f.json'
AUTHOR = 'json_to_solo'

class Batch04CdBroken(Solo48):
    icon_id = 'batch-04-cd-broken'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'computers'
    aliases = ()
    keywords = ('batch', 'cd', 'broken', 'computers')

    def build(self):
        self.add_line('e0', (28, 7), (21, 19))
        self.add_line('e1', (21, 19), (31, 17))
        self.add_line('e2', (31, 17), (19, 31))
        self.add_arc('e3-1', (22, 6), (6, 23), radius_x=18, sweep=False)
        self.add_line('e3-2', (6, 23), (7, 30))
        self.add_arc('e3-3', (7, 30), (23, 42), radius_x=18, sweep=False)
        self.add_arc('e3-4', (23, 42), (42, 23), radius_x=19, sweep=False)
        self.add_arc('e3-5', (42, 23), (28, 7), radius_x=17, sweep=False)
        self.add_arc('e4', (19, 31), (28, 28), radius_x=29, sweep=False)
        self.add_contour('c0', 'e3-1', 'e3-2', 'e3-3', 'e3-4', 'e3-5', 'e0', 'e1', 'e2', 'e4')
