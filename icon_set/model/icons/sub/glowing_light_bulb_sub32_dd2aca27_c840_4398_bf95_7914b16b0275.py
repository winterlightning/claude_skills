"""Independent 32px profile of glowing-light-bulb.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'dd2aca27-c840-4398-bf95-7914b16b0275'
SOURCE_PATH = 'pictographic-primitives/work/bulb_dd2aca27-c840-4398-bf95-7914b16b0275.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('dd2aca27-c840-4398-bf95-7914b16b0275', 'pictographic-primitives/work/bulb_dd2aca27-c840-4398-bf95-7914b16b0275.svg'),)
PROFILE_SOURCE_KEYS = ('solo/glowing-light-bulb',)
SOLO_SOURCE_ICON_IDS = ('glowing-light-bulb',)
REFERENCE_EXPORT_SHA256 = '8477e7a59ac3339135b35afa0da804400a8910ba44e0598bc50182a02f908527'

class Drawing(Sub32):
    icon_id = 'glowing-light-bulb-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/work'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (9, 16), (23, 16), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (23, 16), (20, 24), radius_x=11, radius_y=11, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (20, 24), (20, 30))
        self.add_line('p1-r1-4', (20, 30), (12, 30))
        self.add_line('p1-r1-5', (12, 30), (12, 24))
        self.add_arc('p1-r1-6', (12, 24), (9, 16), radius_x=11, radius_y=11, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_line('p2-r1-1', (16, 2), (16, 2))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (2, 16), (2, 16))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (30, 16), (30, 16))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (5, 5), (5, 5))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (27, 5), (27, 5))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
