"""Independent 32px profile of lightning-with-wrench.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '7a4d7838-471b-4d28-87da-ddd67295cbe7'
SOURCE_PATH = 'pictographic-primitives/symbol/lightning with wrench_7a4d7838-471b-4d28-87da-ddd67295cbe7.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('7a4d7838-471b-4d28-87da-ddd67295cbe7', 'pictographic-primitives/symbol/lightning with wrench_7a4d7838-471b-4d28-87da-ddd67295cbe7.svg'), ('8b71e7e7-15cf-4d31-8c76-295ef5576f53', 'icon_set/dist/gallery/combination-originals/8b71e7e7-15cf-4d31-8c76-295ef5576f53.svg'))
PROFILE_SOURCE_KEYS = ('solo/lightning-with-wrench',)
SOLO_SOURCE_ICON_IDS = ('lightning-with-wrench',)
REFERENCE_EXPORT_SHA256 = '8499894bda8f20061b025c07c165f4022d6519d76adb62f1d7dc04a39dbd3237'

class Drawing(Sub32):
    icon_id = 'lightning-with-wrench-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 22), (11, 12))
        self.add_bezier('p1-r1-2', (11, 12), ((9, 12), (9, 11), (9, 9)))
        self.add_bezier('p1-r1-3', (9, 9), ((9, 9), (9, 8), (9, 7)))
        self.add_bezier('p1-r1-4', (9, 7), ((9, 4), (13, 2), (16, 2)))
        self.add_line('p1-r1-5', (16, 2), (21, 2))
        self.add_line('p1-r1-6', (21, 2), (16, 7))
        self.add_line('p1-r1-7', (16, 7), (18, 11))
        self.add_bezier('p1-r1-8', (18, 11), ((18, 11), (19, 12), (19, 12)))
        self.add_bezier('p1-r1-9', (19, 12), ((19, 15), (17, 17), (14, 17)))
        self.add_line('p1-r1-10', (14, 17), (8, 27))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', closed=False)
        self.add_line('p2-r1-1', (30, 13), (21, 21))
        self.add_line('p2-r1-2', (21, 21), (30, 21))
        self.add_line('p2-r1-3', (30, 21), (22, 30))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
