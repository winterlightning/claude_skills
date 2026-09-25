"""Independent 32px profile of document-upload-content.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'b724f792-07ff-4baa-b3d7-a8da4f357c76'
SOURCE_PATH = 'icon_set/dist/gallery/combination-originals/b724f792-07ff-4baa-b3d7-a8da4f357c76.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('b724f792-07ff-4baa-b3d7-a8da4f357c76', 'icon_set/dist/gallery/combination-originals/b724f792-07ff-4baa-b3d7-a8da4f357c76.svg'),)
PROFILE_SOURCE_KEYS = ('solo/document-upload-content',)
SOLO_SOURCE_ICON_IDS = ('document-upload-content',)
REFERENCE_EXPORT_SHA256 = '3d3d14f8d10dccd1734d89969b202376f4983a61b862dabce0df990667ead827'

class Drawing(Sub32):
    icon_id = 'document-upload-content-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (8, 2), (24, 2))
        self.add_arc('p1-r1-2', (24, 2), (27, 5), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (27, 5), (27, 23))
        self.add_line('p1-r1-4', (27, 23), (20, 30))
        self.add_line('p1-r1-5', (20, 30), (8, 30))
        self.add_arc('p1-r1-6', (8, 30), (5, 27), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-7', (5, 27), (5, 5))
        self.add_arc('p1-r1-8', (5, 5), (8, 2), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_line('p2-r1-1', (11, 15), (16, 10))
        self.add_line('p2-r1-2', (16, 10), (21, 15))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (16, 10), (16, 22))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-2', 'p3-r1-1')
