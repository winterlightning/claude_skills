"""Independent 32px profile of spiraling-tornado.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'dc2f84e2-1e3c-4253-9ea5-be6ccd2c901f'
SOURCE_PATH = 'pictographic-primitives/weather/hurricane_dc2f84e2-1e3c-4253-9ea5-be6ccd2c901f.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('dc2f84e2-1e3c-4253-9ea5-be6ccd2c901f', 'pictographic-primitives/weather/hurricane_dc2f84e2-1e3c-4253-9ea5-be6ccd2c901f.svg'),)
PROFILE_SOURCE_KEYS = ('solo/spiraling-tornado',)
SOLO_SOURCE_ICON_IDS = ('spiraling-tornado',)
REFERENCE_EXPORT_SHA256 = 'ff0341573f02b158b31d0b8fe7b6f66b34d300184969dc5471bc6b0582391c10'

class Drawing(Sub32):
    icon_id = 'spiraling-tornado-sub32'
    keyshape = Keyshape.HRECT_L
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/weather'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (16, 5), (2, 12), radius_x=14, radius_y=7, large_arc=False, sweep=False)
        self.add_arc('p1-r1-2', (2, 12), (30, 12), radius_x=14, radius_y=7, large_arc=False, sweep=False)
        self.add_arc('p1-r1-3', (30, 12), (17, 12), radius_x=6.5, radius_y=2.1666666666666665, large_arc=False, sweep=False)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_arc('p2-r1-1', (12, 25), (23, 25), radius_x=6, radius_y=2, large_arc=False, sweep=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
