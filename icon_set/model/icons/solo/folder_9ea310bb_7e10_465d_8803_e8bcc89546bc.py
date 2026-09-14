"""Folder (folders), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9ea310bb-7e10-465d-8803-e8bcc89546bc'
SOURCE_PATH = 'icons-json/folders/folder_9ea310bb-7e10-465d-8803-e8bcc89546bc.json'
AUTHOR = 'json_to_solo'

class FolderFolders(Solo48):
    icon_id = 'folder-folders'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'folders'
    aliases = ()
    keywords = ('folder', 'folders')

    def build(self):
        self.add_line('e0', (41, 40), (7, 40))
        self.add_line('e1', (4, 36), (4, 11))
        self.add_line('e2', (8, 8), (17, 8))
        self.add_line('e3', (24, 13), (40, 13))
        self.add_line('e4', (44, 16), (44, 38))
        self.add_line('e5-1', (7, 40), (6, 40))
        self.add_arc('e5-2', (6, 40), (4, 38), radius_x=3)
        self.add_arc('e5-3', (4, 38), (4, 36), radius_x=7, sweep=False)
        self.add_arc('e6-1', (4, 11), (7, 8), radius_x=3)
        self.add_arc('e6-2', (7, 8), (8, 8), radius_x=8, sweep=False)
        self.add_line('e7', (17, 8), (24, 13))
        self.add_arc('e8-1', (40, 13), (44, 15), radius_x=3)
        self.add_arc('e8-2', (44, 15), (44, 16), radius_x=8, sweep=False)
        self.add_arc('e9', (44, 38), (41, 40), radius_x=4)
        self.add_contour('c0', 'e0', 'e5-1', 'e5-2', 'e5-3', 'e1', 'e6-1', 'e6-2', 'e2', 'e7', 'e3', 'e8-1', 'e8-2', 'e4', 'e9', closed=True)
