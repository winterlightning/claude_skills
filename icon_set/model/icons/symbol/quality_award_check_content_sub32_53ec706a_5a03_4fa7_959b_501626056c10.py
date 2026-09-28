"""Independent 32px profile of quality-award-check-content.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '53ec706a-5a03-4fa7-959b-501626056c10'
SOURCE_PATH = 'icon_set/dist/gallery/combination-originals/53ec706a-5a03-4fa7-959b-501626056c10.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('53ec706a-5a03-4fa7-959b-501626056c10', 'icon_set/dist/gallery/combination-originals/53ec706a-5a03-4fa7-959b-501626056c10.svg'),)
PROFILE_SOURCE_KEYS = ('solo/quality-award-check-content',)
SOLO_SOURCE_ICON_IDS = ('quality-award-check-content',)
REFERENCE_EXPORT_SHA256 = '5135882253e5ddc32063df5791063f24b4be810851b5e6ebcccba37c8b365da4'

class Drawing(Sub32):
    icon_id = 'quality-award-check-content-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (5, 13), (27, 13), radius_x=11, radius_y=11, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (27, 13), (5, 13), radius_x=11, radius_y=11, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (11, 13), (15, 17))
        self.add_line('p2-r1-2', (15, 17), (20, 11))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (8, 22), (5, 30))
        self.add_line('p3-r1-2', (5, 30), (13, 26))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_line('p4-r1-1', (24, 22), (27, 30))
        self.add_line('p4-r1-2', (27, 30), (19, 26))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
