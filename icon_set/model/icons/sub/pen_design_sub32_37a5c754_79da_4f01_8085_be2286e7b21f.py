"""Independent 32px profile of pen-design.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '37a5c754-79da-4f01-8085-be2286e7b21f'
SOURCE_PATH = 'pictographic-primitives/design/pen_37a5c754-79da-4f01-8085-be2286e7b21f.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('37a5c754-79da-4f01-8085-be2286e7b21f', 'pictographic-primitives/design/pen_37a5c754-79da-4f01-8085-be2286e7b21f.svg'), ('8c7f7f5f-bef6-4d10-8dac-a93a4842e584', 'pictographic-primitives/design/pen_8c7f7f5f-bef6-4d10-8dac-a93a4842e584.svg'))
PROFILE_SOURCE_KEYS = ('solo/pen-design', 'solo/pen-8c7f7f5f')
SOLO_SOURCE_ICON_IDS = ('pen-design', 'pen-8c7f7f5f')
REFERENCE_EXPORT_SHA256 = '05b92a72b6643143645143f753fac09ba997e9eba1484d67ce5d742c6db0c508'

class Drawing(Sub32):
    icon_id = 'pen-design-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'design'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (8, 11))
        self.add_bezier('p1-r1-2', (8, 11), ((11, 7), (13, 7), (17, 7)))
        self.add_bezier('p1-r1-3', (17, 7), ((19, 7), (21, 7), (23, 9)))
        self.add_bezier('p1-r1-4', (23, 9), ((25, 11), (25, 12), (25, 15)))
        self.add_bezier('p1-r1-5', (25, 15), ((25, 19), (25, 21), (21, 24)))
        self.add_line('p1-r1-6', (21, 24), (2, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_line('p2-r1-1', (2, 30), (16, 16))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (23, 9), (30, 2))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-3', 'p3-r1-1')
        self.relate("connect", 'p1-r1-4', 'p3-r1-1')
        self.relate("connect", 'p1-r1-6', 'p2-r1-1')
