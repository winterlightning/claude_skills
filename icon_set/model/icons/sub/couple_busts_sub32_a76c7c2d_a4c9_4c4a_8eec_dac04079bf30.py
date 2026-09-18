"""Independent 32px profile of couple-busts.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'a76c7c2d-a4c9-4c4a-8eec-dac04079bf30'
SOURCE_PATH = 'pictographic-primitives/symbol/couple_a76c7c2d-a4c9-4c4a-8eec-dac04079bf30.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('a76c7c2d-a4c9-4c4a-8eec-dac04079bf30', 'pictographic-primitives/symbol/couple_a76c7c2d-a4c9-4c4a-8eec-dac04079bf30.svg'),)
PROFILE_SOURCE_KEYS = ('solo/couple-busts',)
SOLO_SOURCE_ICON_IDS = ('couple-busts',)
REFERENCE_EXPORT_SHA256 = '072bea1081dd2f5d8546c56ad997c0c4bb65af05e3c726f78d0d817df0782b08'

class Drawing(Sub32):
    icon_id = 'couple-busts-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbols/standalone'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (7, 5), (7, 13), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (7, 13), (7, 5), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_arc('p2-r1-1', (2, 27), (12, 27), radius_x=5, radius_y=6, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_arc('p3-r1-1', (25, 5), (25, 13), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p3-r1-2', (25, 13), (25, 5), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_arc('p4-r1-1', (20, 27), (30, 27), radius_x=5, radius_y=6, large_arc=False, sweep=True)
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
