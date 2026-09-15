"""Folder file (folders), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '186efa63-6969-47ce-9079-53d58afb504d'
SOURCE_PATH = 'pictographic-primitives/folders/folder file_186efa63-6969-47ce-9079-53d58afb504d.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class FolderFile(Solo48):
    icon_id = 'folder-file'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'folders'
    aliases = ()
    keywords = ('folder', 'file', 'folders')

    def build(self):
        # Plan: restore exact straight junctions; remove short fitted corner detours.
        # Reference: existing subject and its ideal straight-edge intersections.
        self.add_line('e0', (13, 22), (11, 22))
        self.add_line('e1', (8, 24), (8, 44))
        self.add_line('e2', (8, 44), (32, 44))
        self.add_line('e3', (32, 44), (32, 26))
        self.add_line('e4', (32, 26), (21, 26))
        self.add_line('e5', (15, 22), (13, 22))
        self.add_line('e6', (13, 22), (13, 4))
        self.add_line('e7', (13, 4), (40, 4))
        self.add_line('e8', (40, 4), (40, 41))
        self.add_line('e9', (40, 41), (32, 41))
        self.add_line('e10-1', (11, 22), (8, 23))
        self.add_arc('e10-2', (8, 23), (8, 24), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('e14', (21, 26), (15, 22))
        self.add_contour('c0', 'e0', 'e10-1', 'e10-2', 'e1', 'e2', 'e3', 'e4', 'e14', 'e5', 'e6', 'e7', 'e8', 'e9', closed=False)
