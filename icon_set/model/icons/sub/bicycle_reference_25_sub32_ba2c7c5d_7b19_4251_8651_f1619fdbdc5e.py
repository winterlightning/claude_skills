"""Independent 32px profile of bicycle-reference-25-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'ba2c7c5d-7b19-4251-8651-f1619fdbdc5e'
SOURCE_PATH = 'pictographic-primitives/other/bike_ba2c7c5d-7b19-4251-8651-f1619fdbdc5e.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('ba2c7c5d-7b19-4251-8651-f1619fdbdc5e', 'pictographic-primitives/other/bike_ba2c7c5d-7b19-4251-8651-f1619fdbdc5e.svg'), ('e918e425-b0c9-444c-bdb5-9884044e4703', 'pictographic-primitives/other/bike_e918e425-b0c9-444c-bdb5-9884044e4703.svg'), ('3bd744bc-3a24-4a8e-92f3-02a013f3d4f0', 'pictographic-primitives/other/bike_3bd744bc-3a24-4a8e-92f3-02a013f3d4f0.svg'))
PROFILE_SOURCE_KEYS = ('solo/bicycle-reference-25-solo', 'solo/bicycle-reference-165-solo', 'solo/bicycle-reference-184-solo')
SOLO_SOURCE_ICON_IDS = ('bicycle-reference-25-solo', 'bicycle-reference-165-solo', 'bicycle-reference-184-solo')
REFERENCE_EXPORT_SHA256 = '715c83355c6af1534edaeebc5e3f7c45ec47d099c947d3457999f263cffb24c0'

class Drawing(Sub32):
    icon_id = 'bicycle-reference-25-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (2, 25), (12, 25), radius_x=5, radius_y=5, large_arc=True, sweep=False)
        self.add_arc('p1-r1-2', (12, 25), (2, 25), radius_x=5, radius_y=5, large_arc=True, sweep=False)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=True)
        self.add_arc('p2-r1-1', (20, 25), (30, 25), radius_x=5, radius_y=5, large_arc=True, sweep=False)
        self.add_arc('p2-r1-2', (30, 25), (20, 25), radius_x=5, radius_y=5, large_arc=True, sweep=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=True)
        self.add_line('p3-r1-1', (11, 8), (21, 8))
        self.add_line('p3-r1-2', (21, 8), (16, 18))
        self.add_line('p3-r1-3', (16, 18), (11, 8))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=True)
        self.add_line('p4-r1-1', (11, 8), (7, 20))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (21, 8), (25, 20))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (11, 2), (11, 8))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.add_line('p7-r1-1', (8, 2), (14, 2))
        self.add_contour('path-7-1', 'p7-r1-1', closed=False)
        self.add_line('p8-r1-1', (21, 8), (20, 2))
        self.add_line('p8-r1-2', (20, 2), (25, 2))
        self.add_contour('path-8-1', 'p8-r1-1', 'p8-r1-2', closed=False)
        self.relate("connect", 'p3-r1-1', 'p4-r1-1')
        self.relate("connect", 'p3-r1-1', 'p5-r1-1')
        self.relate("connect", 'p3-r1-1', 'p6-r1-1')
        self.relate("connect", 'p3-r1-1', 'p8-r1-1')
        self.relate("connect", 'p3-r1-2', 'p5-r1-1')
        self.relate("connect", 'p3-r1-2', 'p8-r1-1')
        self.relate("connect", 'p3-r1-3', 'p4-r1-1')
        self.relate("connect", 'p3-r1-3', 'p6-r1-1')
        self.relate("connect", 'p4-r1-1', 'p6-r1-1')
        self.relate("connect", 'p5-r1-1', 'p8-r1-1')
