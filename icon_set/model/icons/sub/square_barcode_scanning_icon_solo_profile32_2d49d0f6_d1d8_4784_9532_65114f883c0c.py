"""Independent 32px profile of square-barcode-scanning-icon-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '2d49d0f6-d1d8-4784-9532-65114f883c0c'
SOURCE_PATH = 'pictographic-primitives/shopping/barcode_2d49d0f6-d1d8-4784-9532-65114f883c0c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('2d49d0f6-d1d8-4784-9532-65114f883c0c', 'pictographic-primitives/shopping/barcode_2d49d0f6-d1d8-4784-9532-65114f883c0c.svg'),)
PROFILE_SOURCE_KEYS = ('solo/square-barcode-scanning-icon-solo',)
SOLO_SOURCE_ICON_IDS = ('square-barcode-scanning-icon-solo',)
REFERENCE_EXPORT_SHA256 = '9c5a50472323fbff80f02b4c27bfa82552864fe4384c4c6bd9597436b3381566'

class Drawing(Sub32):
    icon_id = 'square-barcode-scanning-icon-solo-profile32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (6, 2), (26, 2))
        self.add_arc('p1-r1-2', (26, 2), (30, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (30, 6), (30, 26))
        self.add_arc('p1-r1-4', (30, 26), (26, 30), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p1-r1-5', (26, 30), (6, 30))
        self.add_arc('p1-r1-6', (6, 30), (2, 26), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p1-r1-7', (2, 26), (2, 6))
        self.add_arc('p1-r1-8', (2, 6), (6, 2), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_line('p2-r1-1', (9, 9), (9, 23))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (16, 9), (16, 23))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (23, 9), (23, 23))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
