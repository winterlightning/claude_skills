"""Independent 32px profile of house-b6632e92.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'b6632e92-d138-462e-a017-77d5e5b870dd'
SOURCE_PATH = 'pictographic-primitives/interface-essential/house_b6632e92-d138-462e-a017-77d5e5b870dd.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('b6632e92-d138-462e-a017-77d5e5b870dd', 'pictographic-primitives/interface-essential/house_b6632e92-d138-462e-a017-77d5e5b870dd.svg'),)
PROFILE_SOURCE_KEYS = ('solo/house-b6632e92',)
SOLO_SOURCE_ICON_IDS = ('house-b6632e92',)
REFERENCE_EXPORT_SHA256 = '6a73c41cd7d09f798690ebf6158c62280ab6d0b8aa8a67a50ea84ab3b895176c'

class Drawing(Sub32):
    icon_id = 'house-b6632e92-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (30, 17), (16, 5))
        self.add_line('p1-r1-2', (16, 5), (2, 17))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (26, 13), (26, 27))
        self.add_line('p2-r1-2', (26, 27), (6, 27))
        self.add_line('p2-r1-3', (6, 27), (6, 14))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_line('p3-r1-1', (20, 20), (12, 20))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
