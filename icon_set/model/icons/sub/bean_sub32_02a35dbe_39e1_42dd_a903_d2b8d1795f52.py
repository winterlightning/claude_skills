"""Independent 32px profile of bean.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '02a35dbe-39e1-42dd-a903-d2b8d1795f52'
SOURCE_PATH = 'pictographic-primitives/symbol/peanut_02a35dbe-39e1-42dd-a903-d2b8d1795f52.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('02a35dbe-39e1-42dd-a903-d2b8d1795f52', 'pictographic-primitives/symbol/peanut_02a35dbe-39e1-42dd-a903-d2b8d1795f52.svg'),)
PROFILE_SOURCE_KEYS = ('solo/bean',)
SOLO_SOURCE_ICON_IDS = ('bean',)
REFERENCE_EXPORT_SHA256 = 'cc97f838ced67d583ecd052ba174121fc94dcdac494ec5a0cbb8ddeb2076bc10'

class Drawing(Sub32):
    icon_id = 'bean-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/symbols'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (16, 10), ((16, 7), (19, 5), (23, 5)))
        self.add_bezier('p1-r1-2', (23, 5), ((27, 5), (30, 7), (30, 10)))
        self.add_bezier('p1-r1-3', (30, 10), ((30, 15), (28, 19), (23, 22)))
        self.add_bezier('p1-r1-4', (23, 22), ((19, 25), (14, 27), (8, 27)))
        self.add_bezier('p1-r1-5', (8, 27), ((5, 27), (2, 25), (2, 22)))
        self.add_bezier('p1-r1-6', (2, 22), ((2, 19), (5, 16), (8, 16)))
        self.add_bezier('p1-r1-7', (8, 16), ((10, 16), (12, 15), (14, 14)))
        self.add_bezier('p1-r1-8', (14, 14), ((15, 13), (16, 12), (16, 10)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
