"""Independent 32px profile of no-stain-content.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'cdcbaa25-e2de-4eba-bda2-3a33deeae5f4'
SOURCE_PATH = 'icon_set/dist/gallery/combination-originals/cdcbaa25-e2de-4eba-bda2-3a33deeae5f4.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('cdcbaa25-e2de-4eba-bda2-3a33deeae5f4', 'icon_set/dist/gallery/combination-originals/cdcbaa25-e2de-4eba-bda2-3a33deeae5f4.svg'),)
PROFILE_SOURCE_KEYS = ('solo/no-stain-content',)
SOLO_SOURCE_ICON_IDS = ('no-stain-content',)
REFERENCE_EXPORT_SHA256 = '910ce8c41d6b7183a56baa147263ce48df09bf31aef62006ec2ca7644a4790b3'

class Drawing(Sub32):
    icon_id = 'no-stain-content-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (11, 2), ((13, 2), (15, 3), (16, 4)))
        self.add_bezier('p1-r1-2', (16, 4), ((17, 5), (18, 7), (18, 8)))
        self.add_line('p1-r1-3', (18, 8), (24, 8))
        self.add_arc('p1-r1-4', (24, 8), (30, 14), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_bezier('p1-r1-5', (30, 14), ((30, 16), (29, 18), (28, 19)))
        self.add_bezier('p1-r1-6', (28, 19), ((27, 20), (25, 21), (24, 21)))
        self.add_line('p1-r1-7', (24, 21), (18, 21))
        self.add_arc('p1-r1-8', (18, 21), (11, 27), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('p1-r1-9', (11, 27), (5, 21), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('p1-r1-10', (5, 21), (5, 14))
        self.add_arc('p1-r1-11', (5, 14), (2, 11), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p1-r1-12', (2, 11), (8, 5), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('p1-r1-13', (8, 5), (11, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', 'p1-r1-13', closed=False)
        self.add_line('p2-r1-1', (2, 2), (30, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
