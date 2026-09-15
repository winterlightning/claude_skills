"""Folder empty (folders), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7d8b7227-dc25-5b0c-b0c7-40e77eaa84e6'
SOURCE_PATH = 'pictographic-primitives/folders/folder empty_7d8b7227-dc25-5b0c-b0c7-40e77eaa84e6.svg'
AUTHOR = 'gpt-6'

class FolderEmpty(Solo48):
    icon_id = 'folder-empty'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'folders'
    aliases = ()
    keywords = ('folder', 'empty', 'folders')

    def build(self):
        self.add_line('e0', (18, 8), (7, 8))
        self.add_line('e1', (4, 10), (4, 37))
        self.add_line('e2', (7, 40), (41, 40))
        self.add_line('e4', (42, 13), (23, 13))
        self.add_arc('e5-1', (7, 8), (5, 8), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('e5-2', (5, 8), (4, 10))
        self.add_arc('e6', (4, 37), (7, 40), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_line('e7-1', (41, 40), (44, 39))
        self.add_line('e7-2', (44, 39), (44, 16))
        self.add_arc('e8-1', (44, 16), (44, 15), radius_x=24, radius_y=24, large_arc=False, sweep=True)
        self.add_arc('e8-2', (44, 15), (42, 13), radius_x=2, radius_y=2, large_arc=False, sweep=False)
        self.add_line('e9', (23, 13), (18, 8))
        self.add_contour('c0', 'e0', 'e5-1', 'e5-2', 'e1', 'e6', 'e2', 'e7-1', 'e7-2', 'e8-1', 'e8-2', 'e4', 'e9', closed=True)
