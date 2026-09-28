"""Folder stand (folders), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6097ccbb-155d-40ab-ba25-2e3dbaeb6923'
SOURCE_PATH = 'pictographic-primitives/folders/folder stand_6097ccbb-155d-40ab-ba25-2e3dbaeb6923.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class FolderStandFolders(Solo48):
    icon_id = 'folder-stand-folders'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'folders'
    categories = ('folders', 'primitives')
    aliases = ()
    keywords = ('folder', 'stand', 'folders')

    def build(self):
        # Plan: restore exact straight junctions; remove short fitted corner detours.
        # Reference: existing subject and its ideal straight-edge intersections.
        self.add_line('e0', (24, 42), (24, 33))
        self.add_line('e1', (15, 42), (33, 42))
        self.add_line('e2', (6, 33), (6, 6))
        self.add_line('e3', (6, 6), (17, 6))
        self.add_line('e4', (22, 12), (42, 12))
        self.add_line('e5', (42, 12), (42, 33))
        self.add_line('e6', (42, 33), (6, 33))
        self.add_line('e9-1', (17, 6), (19, 7))
        self.add_line('e9-2', (19, 7), (22, 12))
        self.add_contour('c0', 'e0', closed=False)
        self.add_contour('c1', 'e1', closed=False)
        self.add_contour('c2', 'e2', 'e3', 'e9-1', 'e9-2', 'e4', 'e5', 'e6', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
