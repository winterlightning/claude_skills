"""Independent 32px profile of circle-arrow-left.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '3aff8073-22e1-56e9-acc2-deec5055c179'
SOURCE_PATH = 'pictographic-primitives/arrows/circle arrow left_3aff8073-22e1-56e9-acc2-deec5055c179.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('3aff8073-22e1-56e9-acc2-deec5055c179', 'pictographic-primitives/arrows/circle arrow left_3aff8073-22e1-56e9-acc2-deec5055c179.svg'),)
PROFILE_SOURCE_KEYS = ('solo/circle-arrow-left',)
SOLO_SOURCE_ICON_IDS = ('circle-arrow-left',)
REFERENCE_EXPORT_SHA256 = 'bd3e8d64fc9ff2c287e829d35143e528daa7ecf655528f043e3a47e41efdce22'

class Drawing(Sub32):
    icon_id = 'circle-arrow-left-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'arrows'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (15, 10), (9, 16))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (15, 22), (9, 16))
        self.add_line('p2-r1-2', (9, 16), (23, 16))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_arc('p3-r1-1', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p3-r1-2', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-1', 'p2-r1-2')
