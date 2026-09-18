"""Independent 32px profile of state32-17fe1005-9f31-49fb-8527-ec82c8c4be78.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '17fe1005-9f31-49fb-8527-ec82c8c4be78'
SOURCE_PATH = 'icon_set/assets/combination-state32/17fe1005-9f31-49fb-8527-ec82c8c4be78.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('17fe1005-9f31-49fb-8527-ec82c8c4be78', 'icon_set/assets/combination-state32/17fe1005-9f31-49fb-8527-ec82c8c4be78.svg'),)
PROFILE_SOURCE_KEYS = ()
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = '2b38dc2d352b257f7a54ca72eaba2c89c0f5966a28dade52e017c189ecfd0f91'

class Drawing(Sub32):
    icon_id = 'state32-17fe1005-9f31-49fb-8527-ec82c8c4be78'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (21, 6), (9, 17))
        self.add_line('p1-r1-2', (9, 17), (22, 17))
        self.add_line('p1-r1-3', (22, 17), (11, 26))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (2, 4), (2, 4))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (9, 6), (9, 6))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (2, 16), (2, 16))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (9, 22), (9, 22))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (3, 28), (3, 28))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.add_line('p7-r1-1', (25, 4), (25, 4))
        self.add_contour('path-7-1', 'p7-r1-1', closed=False)
        self.add_line('p8-r1-1', (30, 9), (30, 9))
        self.add_contour('path-8-1', 'p8-r1-1', closed=False)
        self.add_line('p9-r1-1', (25, 24), (25, 24))
        self.add_contour('path-9-1', 'p9-r1-1', closed=False)
