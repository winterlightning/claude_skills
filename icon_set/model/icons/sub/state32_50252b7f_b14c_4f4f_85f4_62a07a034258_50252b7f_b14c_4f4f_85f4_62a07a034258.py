"""Independent 32px profile of state32-50252b7f-b14c-4f4f-85f4-62a07a034258.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '50252b7f-b14c-4f4f-85f4-62a07a034258'
SOURCE_PATH = 'pictographic-primitives/state/three dots horizontal_50252b7f-b14c-4f4f-85f4-62a07a034258.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('50252b7f-b14c-4f4f-85f4-62a07a034258', 'pictographic-primitives/state/three dots horizontal_50252b7f-b14c-4f4f-85f4-62a07a034258.svg'),)
PROFILE_SOURCE_KEYS = ('solo/three-dots-horizontal',)
SOLO_SOURCE_ICON_IDS = ('three-dots-horizontal',)
REFERENCE_EXPORT_SHA256 = '212c70a81123cdf0115dc6ae81a137feafa69706bcd7632d34c80ef4281946eb'

class Drawing(Sub32):
    icon_id = 'state32-50252b7f-b14c-4f4f-85f4-62a07a034258'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (5, 5), (27, 5))
        self.add_bezier('p1-r1-2', (27, 5), ((29, 5), (30, 6), (30, 8)))
        self.add_line('p1-r1-3', (30, 8), (30, 24))
        self.add_bezier('p1-r1-4', (30, 24), ((30, 26), (29, 27), (27, 27)))
        self.add_line('p1-r1-5', (27, 27), (5, 27))
        self.add_bezier('p1-r1-6', (5, 27), ((3, 27), (2, 26), (2, 24)))
        self.add_line('p1-r1-7', (2, 24), (2, 8))
        self.add_bezier('p1-r1-8', (2, 8), ((2, 6), (3, 5), (5, 5)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_line('p2-r1-1', (8, 16), (8, 16))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (16, 16), (16, 16))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (24, 16), (24, 16))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
