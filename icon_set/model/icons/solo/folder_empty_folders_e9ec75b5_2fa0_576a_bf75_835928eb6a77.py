"""Folder empty (folders), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e9ec75b5-2fa0-576a-bf75-835928eb6a77'
SOURCE_PATH = 'icons-json/folders/folder empty_e9ec75b5-2fa0-576a-bf75-835928eb6a77.json'
AUTHOR = 'gpt-6'

class FolderEmptyFolders(Solo48):
    icon_id = 'folder-empty-folders'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'folders'
    aliases = ()
    keywords = ('folder', 'empty', 'folders')

    def build(self):
        self.add_line('e0', (19, 8), (7, 8))
        self.add_line('e1', (4, 11), (4, 38))
        self.add_line('e3', (44, 37), (44, 16))
        self.add_line('e4', (41, 13), (23, 13))
        self.add_arc('e5', (7, 8), (4, 11), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_arc('e6-2', (4, 38), (6, 40), radius_x=2, radius_y=2, large_arc=False, sweep=False)
        self.add_line('e6-3', (6, 40), (41, 40))
        self.add_line('e7-1', (41, 40), (44, 38))
        self.add_arc('e7-2', (44, 38), (44, 37), radius_x=38, radius_y=38, large_arc=False, sweep=True)
        self.add_arc('e8-1', (44, 16), (44, 15), radius_x=24, radius_y=24, large_arc=False, sweep=True)
        self.add_arc('e8-2', (44, 15), (41, 13), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_line('e9', (23, 13), (19, 8))
        self.add_contour('c0', 'e0', 'e5', 'e1', 'e6-2', 'e6-3', 'e7-1', 'e7-2', 'e3', 'e8-1', 'e8-2', 'e4', 'e9', closed=True)
