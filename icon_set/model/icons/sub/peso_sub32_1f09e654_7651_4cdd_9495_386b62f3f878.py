"""Independent 32px profile of peso.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '1f09e654-7651-4cdd-9495-386b62f3f878'
SOURCE_PATH = 'pictographic-primitives/money/peso_1f09e654-7651-4cdd-9495-386b62f3f878.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('1f09e654-7651-4cdd-9495-386b62f3f878', 'pictographic-primitives/money/peso_1f09e654-7651-4cdd-9495-386b62f3f878.svg'),)
PROFILE_SOURCE_KEYS = ('solo/peso',)
SOLO_SOURCE_ICON_IDS = ('peso',)
REFERENCE_EXPORT_SHA256 = '3623dab61cbda8854df41afd6801ddccc4b981d10e9e4a0a8b3d0bb3d1254b39'

class Drawing(Sub32):
    icon_id = 'peso-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'money'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (5, 15), (9, 15))
        self.add_line('p1-r1-2', (9, 15), (9, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (9, 15), (22, 15))
        self.add_arc('p2-r1-2', (22, 15), (27, 9), radius_x=6, radius_y=6, large_arc=False, sweep=False)
        self.add_arc('p2-r1-3', (27, 9), (20, 2), radius_x=7, radius_y=7, large_arc=False, sweep=False)
        self.add_line('p2-r1-4', (20, 2), (9, 2))
        self.add_line('p2-r1-5', (9, 2), (9, 15))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-1', 'p2-r1-5')
        self.relate("connect", 'p1-r1-2', 'p2-r1-1')
        self.relate("connect", 'p1-r1-2', 'p2-r1-5')
