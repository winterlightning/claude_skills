"""Independent 32px profile of face.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'e79d0d3c-9833-42da-b29a-025ab29b3d7b'
SOURCE_PATH = 'pictographic-primitives/symbol/face_e79d0d3c-9833-42da-b29a-025ab29b3d7b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('e79d0d3c-9833-42da-b29a-025ab29b3d7b', 'pictographic-primitives/symbol/face_e79d0d3c-9833-42da-b29a-025ab29b3d7b.svg'),)
PROFILE_SOURCE_KEYS = ('solo/face',)
SOLO_SOURCE_ICON_IDS = ('face',)
REFERENCE_EXPORT_SHA256 = 'ffdba2a9aa7c36f7a78496ee135c6aa1491c45e74c5f69613839992d2be10b43'

class Drawing(Sub32):
    icon_id = 'face-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (2, 16), (16, 2), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (16, 2), (30, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (30, 16), (16, 30), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p1-r1-4', (16, 30), (2, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_bezier('p2-r1-1', (2, 16), ((8, 16), (13, 12), (16, 8)))
        self.add_bezier('p2-r1-2', (16, 8), ((19, 12), (24, 16), (30, 16)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-2', 'p2-r1-2')
        self.relate("connect", 'p1-r1-3', 'p2-r1-2')
        self.relate("connect", 'p1-r1-4', 'p2-r1-1')
