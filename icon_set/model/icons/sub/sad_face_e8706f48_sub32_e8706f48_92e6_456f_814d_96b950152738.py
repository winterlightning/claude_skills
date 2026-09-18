"""Independent 32px profile of sad-face-e8706f48.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'e8706f48-92e6-456f-814d-96b950152738'
SOURCE_PATH = 'pictographic-primitives/smileys/sad face_e8706f48-92e6-456f-814d-96b950152738.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('e8706f48-92e6-456f-814d-96b950152738', 'pictographic-primitives/smileys/sad face_e8706f48-92e6-456f-814d-96b950152738.svg'),)
PROFILE_SOURCE_KEYS = ('solo/sad-face-e8706f48',)
SOLO_SOURCE_ICON_IDS = ('sad-face-e8706f48',)
REFERENCE_EXPORT_SHA256 = '2a7717801be2e8181a60b04115407dc7f6f0662e574ed2f01106f348163272e0'

class Drawing(Sub32):
    icon_id = 'sad-face-e8706f48-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'smileys'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 14), (30, 14))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_bezier('p2-r1-1', (5, 14), ((6, 7), (7, 2), (12, 2)))
        self.add_bezier('p2-r1-2', (12, 2), ((14, 2), (18, 2), (20, 2)))
        self.add_bezier('p2-r1-3', (20, 2), ((25, 2), (26, 7), (27, 14)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_line('p3-r1-1', (10, 21), (10, 21))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (22, 21), (22, 21))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_arc('p5-r1-1', (7, 30), (25, 30), radius_x=9, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
