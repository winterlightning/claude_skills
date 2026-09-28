"""Independent 32px profile of focus-circle.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '194127a0-095c-4aa9-bd19-038532bd3355'
SOURCE_PATH = 'pictographic-primitives/symbol/focus circle_194127a0-095c-4aa9-bd19-038532bd3355.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('194127a0-095c-4aa9-bd19-038532bd3355', 'pictographic-primitives/symbol/focus circle_194127a0-095c-4aa9-bd19-038532bd3355.svg'),)
PROFILE_SOURCE_KEYS = ('solo/focus-circle',)
SOLO_SOURCE_ICON_IDS = ('focus-circle',)
REFERENCE_EXPORT_SHA256 = '9f7bb9edcd8283a3fe9d3447c28fb106d7803938e63c61bb0e922b823fbf1e2c'

class Drawing(Sub32):
    icon_id = 'focus-circle-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (9, 2), (2, 2))
        self.add_line('p1-r1-2', (2, 2), (2, 9))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (23, 2), (30, 2))
        self.add_line('p2-r1-2', (30, 2), (30, 9))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (2, 23), (2, 30))
        self.add_line('p3-r1-2', (2, 30), (9, 30))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_line('p4-r1-1', (30, 23), (30, 30))
        self.add_line('p4-r1-2', (30, 30), (23, 30))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_arc('p5-r1-1', (10, 16), (22, 16), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('p5-r1-2', (22, 16), (10, 16), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', closed=False)
