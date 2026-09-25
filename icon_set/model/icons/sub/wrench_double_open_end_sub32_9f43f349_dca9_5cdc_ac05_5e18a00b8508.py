"""Independent 32px profile of wrench-double-open-end.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '9f43f349-dca9-5cdc-ac05-5e18a00b8508'
SOURCE_PATH = 'pictographic-primitives/symbol/wrench right_9f43f349-dca9-5cdc-ac05-5e18a00b8508.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('9f43f349-dca9-5cdc-ac05-5e18a00b8508', 'pictographic-primitives/symbol/wrench right_9f43f349-dca9-5cdc-ac05-5e18a00b8508.svg'),)
PROFILE_SOURCE_KEYS = ('solo/wrench-double-open-end',)
SOLO_SOURCE_ICON_IDS = ('wrench-double-open-end',)
REFERENCE_EXPORT_SHA256 = 'abd86a2f04749f276576d7138ea54bdee8063b87ddc4e1f2c7bfa7c61b8340b5'

class Drawing(Sub32):
    icon_id = 'wrench-double-open-end-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (30, 2), (26, 2))
        self.add_arc('p1-r1-2', (26, 2), (23, 8), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_arc('p1-r1-3', (23, 8), (26, 10), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('p1-r1-4', (26, 10), (30, 10))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (2, 30), (6, 30))
        self.add_arc('p2-r1-2', (6, 30), (9, 24), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_arc('p2-r1-3', (9, 24), (6, 22), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('p2-r1-4', (6, 22), (2, 22))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_line('p3-r1-1', (9, 24), (23, 8))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.relate("connect", 'p1-r1-2', 'p3-r1-1')
        self.relate("connect", 'p1-r1-3', 'p3-r1-1')
        self.relate("connect", 'p2-r1-2', 'p3-r1-1')
        self.relate("connect", 'p2-r1-3', 'p3-r1-1')
