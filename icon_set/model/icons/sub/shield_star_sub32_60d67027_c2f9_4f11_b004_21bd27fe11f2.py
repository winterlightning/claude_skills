"""Independent 32px profile of shield-star.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '60d67027-c2f9-4f11-b004-21bd27fe11f2'
SOURCE_PATH = 'pictographic-primitives/protection/shield star_60d67027-c2f9-4f11-b004-21bd27fe11f2.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('60d67027-c2f9-4f11-b004-21bd27fe11f2', 'pictographic-primitives/protection/shield star_60d67027-c2f9-4f11-b004-21bd27fe11f2.svg'),)
PROFILE_SOURCE_KEYS = ('solo/shield-star',)
SOLO_SOURCE_ICON_IDS = ('shield-star',)
REFERENCE_EXPORT_SHA256 = '23557e4569ad216f72d950d2ecca0672700cf127096ad68e6803641b5696365d'

class Drawing(Sub32):
    icon_id = 'shield-star-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'protection'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (5, 6), ((8, 3), (12, 2), (16, 2)))
        self.add_bezier('p1-r1-2', (16, 2), ((20, 2), (24, 3), (27, 6)))
        self.add_line('p1-r1-3', (27, 6), (27, 18))
        self.add_bezier('p1-r1-4', (27, 18), ((27, 24), (22, 28), (16, 30)))
        self.add_bezier('p1-r1-5', (16, 30), ((10, 28), (5, 24), (5, 18)))
        self.add_line('p1-r1-6', (5, 18), (5, 6))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_line('p2-r1-1', (16, 9), (18, 13))
        self.add_line('p2-r1-2', (18, 13), (21, 14))
        self.add_line('p2-r1-3', (21, 14), (19, 17))
        self.add_line('p2-r1-4', (19, 17), (19, 20))
        self.add_line('p2-r1-5', (19, 20), (16, 19))
        self.add_line('p2-r1-6', (16, 19), (13, 20))
        self.add_line('p2-r1-7', (13, 20), (13, 17))
        self.add_line('p2-r1-8', (13, 17), (11, 14))
        self.add_line('p2-r1-9', (11, 14), (14, 13))
        self.add_line('p2-r1-10', (14, 13), (16, 9))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', 'p2-r1-8', 'p2-r1-9', 'p2-r1-10', closed=False)
