"""Independent 32px profile of elevator-direction-doors.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '3b975376-341b-48a1-92cf-f4ed4b0af1eb'
SOURCE_PATH = 'icon_set/dist/gallery/combination-originals/3b975376-341b-48a1-92cf-f4ed4b0af1eb.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('3b975376-341b-48a1-92cf-f4ed4b0af1eb', 'icon_set/dist/gallery/combination-originals/3b975376-341b-48a1-92cf-f4ed4b0af1eb.svg'),)
PROFILE_SOURCE_KEYS = ('solo/elevator-direction-doors',)
SOLO_SOURCE_ICON_IDS = ('elevator-direction-doors',)
REFERENCE_EXPORT_SHA256 = '9d0b1049bec03a65635670cbe49d8192befb617bbb5ed249c4c17358c85fd48f'

class Drawing(Sub32):
    icon_id = 'elevator-direction-doors-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives-generate'
    categories = ('symbol', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (5, 13), (27, 13))
        self.add_arc('p1-r1-2', (27, 13), (30, 16), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (30, 16), (30, 24))
        self.add_arc('p1-r1-4', (30, 24), (27, 27), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-5', (27, 27), (5, 27))
        self.add_arc('p1-r1-6', (5, 27), (2, 24), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-7', (2, 24), (2, 16))
        self.add_arc('p1-r1-8', (2, 16), (5, 13), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_line('p2-r1-1', (16, 13), (16, 27))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (5, 7), (9, 5))
        self.add_line('p3-r1-2', (9, 5), (13, 7))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_line('p4-r1-1', (19, 5), (23, 7))
        self.add_line('p4-r1-2', (23, 7), (27, 5))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
