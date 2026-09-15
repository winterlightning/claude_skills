"""File (emails), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2eca0df0-2d08-4674-b1e3-d443392e4f65'
SOURCE_PATH = 'pictographic-primitives/emails/file_2eca0df0-2d08-4674-b1e3-d443392e4f65.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class File(Solo48):
    icon_id = 'file'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'emails'
    aliases = ()
    keywords = ('file', 'emails')

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
