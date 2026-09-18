"""Independent 32px profile of state32-bacc3012-d61e-47f0-8068-aba74c1f83c7.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'bacc3012-d61e-47f0-8068-aba74c1f83c7'
SOURCE_PATH = 'pictographic-primitives/state/circle R_bacc3012-d61e-47f0-8068-aba74c1f83c7.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('bacc3012-d61e-47f0-8068-aba74c1f83c7', 'pictographic-primitives/state/circle R_bacc3012-d61e-47f0-8068-aba74c1f83c7.svg'),)
PROFILE_SOURCE_KEYS = ('solo/circle-r',)
SOLO_SOURCE_ICON_IDS = ('circle-r',)
REFERENCE_EXPORT_SHA256 = '38a11656f54ee6ff5d6eee39c65dc436947790c4d57343173b90260348bce589'

class Drawing(Sub32):
    icon_id = 'state32-bacc3012-d61e-47f0-8068-aba74c1f83c7'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (11, 22), (11, 10))
        self.add_line('p1-r1-2', (11, 10), (16, 10))
        self.add_bezier('p1-r1-3', (16, 10), ((19, 10), (20, 11), (20, 13)))
        self.add_bezier('p1-r1-4', (20, 13), ((20, 15), (19, 16), (16, 16)))
        self.add_line('p1-r1-5', (16, 16), (11, 16))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p2-r1-1', (16, 16), (21, 22))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_arc('p3-r1-1', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=True, sweep=False)
        self.add_arc('p3-r1-2', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=True, sweep=False)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.relate("connect", 'p1-r1-4', 'p2-r1-1')
        self.relate("connect", 'p1-r1-5', 'p2-r1-1')
