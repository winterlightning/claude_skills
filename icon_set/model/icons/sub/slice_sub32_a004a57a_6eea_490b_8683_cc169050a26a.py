"""Independent 32px profile of slice.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'a004a57a-6eea-490b-8683-cc169050a26a'
SOURCE_PATH = 'pictographic-primitives/state/slice_a004a57a-6eea-490b-8683-cc169050a26a.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('a004a57a-6eea-490b-8683-cc169050a26a', 'pictographic-primitives/state/slice_a004a57a-6eea-490b-8683-cc169050a26a.svg'),)
PROFILE_SOURCE_KEYS = ('solo/slice',)
SOLO_SOURCE_ICON_IDS = ('slice',)
REFERENCE_EXPORT_SHA256 = 'a13683073eeb717d606c2c545962d1d8c742beafe9328b8885f14906bba3639e'

class Drawing(Sub32):
    icon_id = 'slice-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'state'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_arc('p2-r1-1', (22, 13), (20, 22), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_arc('p3-r1-1', (14, 23), (9, 19), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_arc('p4-r1-1', (9, 13), (15, 8), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
