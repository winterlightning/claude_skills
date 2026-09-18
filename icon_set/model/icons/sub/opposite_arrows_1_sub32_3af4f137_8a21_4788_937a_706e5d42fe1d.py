"""Independent 32px profile of opposite-arrows-1.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '3af4f137-8a21-4788-937a-706e5d42fe1d'
SOURCE_PATH = 'pictographic-primitives/symbol/opposite arrows 1_3af4f137-8a21-4788-937a-706e5d42fe1d.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('3af4f137-8a21-4788-937a-706e5d42fe1d', 'pictographic-primitives/symbol/opposite arrows 1_3af4f137-8a21-4788-937a-706e5d42fe1d.svg'),)
PROFILE_SOURCE_KEYS = ('solo/opposite-arrows-1',)
SOLO_SOURCE_ICON_IDS = ('opposite-arrows-1',)
REFERENCE_EXPORT_SHA256 = 'd2bfd0af61f302df55f4fb029a1d5ad351b4088845d916e3f83c3246c39b11a3'

class Drawing(Sub32):
    icon_id = 'opposite-arrows-1-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (24, 5), (30, 10))
        self.add_line('p1-r1-2', (30, 10), (3, 10))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (8, 27), (2, 22))
        self.add_line('p2-r1-2', (2, 22), (29, 22))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
