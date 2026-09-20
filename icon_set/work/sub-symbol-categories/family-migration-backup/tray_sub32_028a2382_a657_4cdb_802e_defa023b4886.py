"""Independent 32px profile of tray.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '028a2382-a657-4cdb-802e-defa023b4886'
SOURCE_PATH = 'pictographic-primitives/symbol/tray_028a2382-a657-4cdb-802e-defa023b4886.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('028a2382-a657-4cdb-802e-defa023b4886', 'pictographic-primitives/symbol/tray_028a2382-a657-4cdb-802e-defa023b4886.svg'),)
PROFILE_SOURCE_KEYS = ('solo/tray',)
SOLO_SOURCE_ICON_IDS = ('tray',)
REFERENCE_EXPORT_SHA256 = '6cf15d1864c879ed0951fdf3e3f45d8ad6470dbfa947e4abdaf16ef2012d2faf'

class Drawing(Sub32):
    icon_id = 'tray-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 27), (30, 27))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (5, 27), (5, 19))
        self.add_arc('p2-r1-2', (5, 19), (27, 19), radius_x=11, radius_y=11, large_arc=False, sweep=True)
        self.add_line('p2-r1-3', (27, 19), (27, 27))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_line('p3-r1-1', (16, 5), (16, 8))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
