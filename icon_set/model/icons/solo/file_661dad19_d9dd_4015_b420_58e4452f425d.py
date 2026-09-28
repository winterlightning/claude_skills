"""File (files), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '661dad19-d9dd-4015-b420-58e4452f425d'
SOURCE_PATH = 'pictographic-primitives/files/file_661dad19-d9dd-4015-b420-58e4452f425d.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class FileFiles(Solo48):
    icon_id = 'file-files'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'files'
    categories = ('files', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('file', 'files')

    def build(self):
        # Plan: restore exact straight junctions; remove short fitted corner detours.
        # Reference: existing subject and its ideal straight-edge intersections.
        self.add_line('e0', (8, 4), (32, 4))
        self.add_line('e1', (32, 4), (39, 12))
        self.add_line('e2', (40, 13), (40, 44))
        self.add_line('e3', (40, 44), (8, 44))
        self.add_line('e4', (8, 44), (8, 4))
        self.add_line('e5', (39, 12), (40, 13))
        self.add_contour('c0', 'e0', 'e1', 'e5', 'e2', 'e3', 'e4', closed=True)
