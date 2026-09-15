"""Folder (folders), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ddd2bcfe-2962-53d9-ae0a-b13b5cd53aa8'
SOURCE_PATH = 'icons-json/folders/folder_ddd2bcfe-2962-53d9-ae0a-b13b5cd53aa8.json'
AUTHOR = 'gpt-6'

class FolderDdd2bcfe(Solo48):
    icon_id = 'folder-ddd2bcfe'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'folders'
    aliases = ()
    keywords = ('folder', 'folders')

    def build(self):
        self.add_line('e0', (4, 37), (4, 12))
        self.add_line('e1', (8, 8), (17, 8))
        self.add_line('e2', (25, 14), (41, 14))
        self.add_line('e3', (44, 16), (44, 36))
        self.add_line('e4', (41, 40), (8, 40))
        self.add_arc('e5', (4, 12), (8, 8), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('e6-2', (17, 8), (22, 13))
        self.add_arc('e6-3', (22, 13), (25, 14), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_arc('e7', (41, 14), (44, 16), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('e8-1', (44, 36), (43, 39), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('e8-2', (43, 39), (41, 40), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('e9-1', (8, 40), (5, 39), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('e9-2', (5, 39), (4, 37), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('c0', 'e0', 'e5', 'e1', 'e6-2', 'e6-3', 'e2', 'e7', 'e3', 'e8-1', 'e8-2', 'e4', 'e9-1', 'e9-2', closed=True)
