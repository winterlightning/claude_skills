"""Independent 32px profile of sad-face-smileys.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '90663cc1-f016-4199-8cee-55a05f0d5515'
SOURCE_PATH = 'pictographic-primitives/smileys/sad face_90663cc1-f016-4199-8cee-55a05f0d5515.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('90663cc1-f016-4199-8cee-55a05f0d5515', 'pictographic-primitives/smileys/sad face_90663cc1-f016-4199-8cee-55a05f0d5515.svg'),)
PROFILE_SOURCE_KEYS = ('solo/sad-face-smileys',)
SOLO_SOURCE_ICON_IDS = ('sad-face-smileys',)
REFERENCE_EXPORT_SHA256 = 'c225a755b28b944525aa3eda2b775e6f527d6acc024221b23019dba1f567334b'

class Drawing(Sub32):
    icon_id = 'sad-face-smileys-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'smileys'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (5, 5), (5, 10))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_arc('p2-r1-1', (2, 27), (16, 18), radius_x=15, radius_y=15, large_arc=False, sweep=True)
        self.add_arc('p2-r1-2', (16, 18), (30, 27), radius_x=15, radius_y=15, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (27, 5), (27, 10))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
