"""Independent 32px profile of lines.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '70edbe92-e5a7-4163-82c3-c5891c1950fd'
SOURCE_PATH = 'pictographic-primitives/symbol/lines_70edbe92-e5a7-4163-82c3-c5891c1950fd.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('70edbe92-e5a7-4163-82c3-c5891c1950fd', 'pictographic-primitives/symbol/lines_70edbe92-e5a7-4163-82c3-c5891c1950fd.svg'),)
PROFILE_SOURCE_KEYS = ('solo/lines',)
SOLO_SOURCE_ICON_IDS = ('lines',)
REFERENCE_EXPORT_SHA256 = '291e1867663e7bfaa7272952faa75a50328447a7bca1b4037b97e74378de7a3e'

class Drawing(Sub32):
    icon_id = 'lines-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 5), (10, 5))
        self.add_line('p1-r1-2', (10, 5), (13, 8))
        self.add_line('p1-r1-3', (13, 8), (22, 26))
        self.add_arc('p1-r1-4', (22, 26), (24, 27), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_line('p1-r1-5', (24, 27), (30, 27))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
