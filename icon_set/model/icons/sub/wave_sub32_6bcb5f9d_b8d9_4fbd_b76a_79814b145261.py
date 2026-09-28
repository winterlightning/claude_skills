"""Independent 32px profile of wave.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '6bcb5f9d-b8d9-4fbd-b76a-79814b145261'
SOURCE_PATH = 'pictographic-primitives/wayfinding/wave_6bcb5f9d-b8d9-4fbd-b76a-79814b145261.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('6bcb5f9d-b8d9-4fbd-b76a-79814b145261', 'pictographic-primitives/wayfinding/wave_6bcb5f9d-b8d9-4fbd-b76a-79814b145261.svg'),)
PROFILE_SOURCE_KEYS = ('solo/wave',)
SOLO_SOURCE_ICON_IDS = ('wave',)
REFERENCE_EXPORT_SHA256 = 'e991b8ce952af2ead99b6db010ea17288caaee38b93005c35cd629b416de1c92'

class Drawing(Sub32):
    icon_id = 'wave-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'wayfinding'
    categories = ('wayfinding', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (7, 2), ((5, 4), (2, 6), (2, 9)))
        self.add_bezier('p1-r1-2', (2, 9), ((2, 15), (8, 17), (8, 23)))
        self.add_bezier('p1-r1-3', (8, 23), ((8, 26), (5, 28), (4, 30)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_bezier('p2-r1-1', (18, 2), ((16, 4), (13, 6), (13, 9)))
        self.add_bezier('p2-r1-2', (13, 9), ((13, 15), (19, 17), (19, 23)))
        self.add_bezier('p2-r1-3', (19, 23), ((19, 26), (16, 28), (14, 30)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_bezier('p3-r1-1', (28, 2), ((27, 4), (24, 6), (24, 9)))
        self.add_bezier('p3-r1-2', (24, 9), ((24, 15), (30, 17), (30, 23)))
        self.add_bezier('p3-r1-3', (30, 23), ((30, 26), (27, 28), (25, 30)))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
