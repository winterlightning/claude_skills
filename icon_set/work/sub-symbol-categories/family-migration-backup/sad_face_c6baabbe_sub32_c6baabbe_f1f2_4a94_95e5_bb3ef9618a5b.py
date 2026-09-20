"""Independent 32px profile of sad-face-c6baabbe.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'c6baabbe-f1f2-4a94-95e5-bb3ef9618a5b'
SOURCE_PATH = 'pictographic-primitives/smileys/sad face_c6baabbe-f1f2-4a94-95e5-bb3ef9618a5b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('c6baabbe-f1f2-4a94-95e5-bb3ef9618a5b', 'pictographic-primitives/smileys/sad face_c6baabbe-f1f2-4a94-95e5-bb3ef9618a5b.svg'),)
PROFILE_SOURCE_KEYS = ('solo/sad-face-c6baabbe',)
SOLO_SOURCE_ICON_IDS = ('sad-face-c6baabbe',)
REFERENCE_EXPORT_SHA256 = '9b7d7542d78e88a56f697a9fda0d3e8b79a6264cd7aae95982e62fb6b4c99829'

class Drawing(Sub32):
    icon_id = 'sad-face-c6baabbe-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'smileys'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (12, 10), (12, 13))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (20, 10), (20, 13))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_arc('p4-r1-1', (11, 22), (21, 22), radius_x=5, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
