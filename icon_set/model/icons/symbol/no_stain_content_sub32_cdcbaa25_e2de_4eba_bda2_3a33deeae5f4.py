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
        # Adopted from the production stroke edit (Browser Edit by hina).
        self.add_bezier('p1-r1-1', (10, 3), ((12, 1), (17, 2), (19, 4)))
        self.add_bezier('p1-r1-2', (19, 4), ((21, 6), (21, 8), (21, 9)))
        self.add_line('p1-r1-3', (21, 9), (24, 9))
        self.add_arc('p1-r1-4', (24, 9), (30, 15), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_bezier('p1-r1-5', (30, 15), ((30, 17), (29, 19), (28, 20)))
        self.add_bezier('p1-r1-6', (28, 20), ((27, 21), (25, 22), (24, 22)))
        self.add_line('p1-r1-7', (24, 22), (21, 22))
        self.add_arc('p1-r1-8', (21, 22), (11, 30), radius_x=10, radius_y=6.403124, large_arc=False, sweep=True)
        self.add_arc('p1-r1-9', (11, 30), (6, 21), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('p1-r1-10', (6, 21), (6, 21))
        self.add_arc('p1-r1-11', (6, 21), (6, 7), radius_x=5.597905, radius_y=7.5, large_arc=False, sweep=True)
        self.add_arc('p1-r1-12', (6, 7), (6, 7), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('p1-r1-13', (6, 7), (10, 3))
        self.add_line('p2-r1-1', (2, 2), (30, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', 'p1-r1-13', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
