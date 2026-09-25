"""Independent 32px profile of syringe-wide-barrel.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'e8bd0685-39d5-42cb-96ed-39a556fbf8e3'
SOURCE_PATH = 'pictographic-primitives/symbol/syringe_e8bd0685-39d5-42cb-96ed-39a556fbf8e3.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('e8bd0685-39d5-42cb-96ed-39a556fbf8e3', 'pictographic-primitives/symbol/syringe_e8bd0685-39d5-42cb-96ed-39a556fbf8e3.svg'),)
PROFILE_SOURCE_KEYS = ('solo/syringe-wide-barrel',)
SOLO_SOURCE_ICON_IDS = ('syringe-wide-barrel',)
REFERENCE_EXPORT_SHA256 = 'e16326add7195129e4f035ba75afad832fe6c2f2c15111774f1fff11b3e448ec'

class Drawing(Sub32):
    icon_id = 'syringe-wide-barrel-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (4, 15), (14, 5))
        self.add_line('p1-r1-2', (14, 5), (20, 11))
        self.add_line('p1-r1-3', (20, 11), (25, 17))
        self.add_line('p1-r1-4', (25, 17), (15, 27))
        self.add_arc('p1-r1-5', (15, 27), (8, 25), radius_x=12, radius_y=12, large_arc=False, sweep=True)
        self.add_arc('p1-r1-6', (8, 25), (4, 15), radius_x=12, radius_y=12, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_line('p2-r1-1', (8, 25), (2, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (20, 11), (27, 5))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (24, 2), (27, 5))
        self.add_line('p4-r1-2', (27, 5), (30, 8))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_line('p5-r1-1', (9, 10), (14, 14))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate("connect", 'p1-r1-2', 'p3-r1-1')
        self.relate("connect", 'p1-r1-3', 'p3-r1-1')
        self.relate("connect", 'p1-r1-5', 'p2-r1-1')
        self.relate("connect", 'p1-r1-6', 'p2-r1-1')
        self.relate("connect", 'p3-r1-1', 'p4-r1-1')
        self.relate("connect", 'p3-r1-1', 'p4-r1-2')
