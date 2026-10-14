"""Independent 32px profile of gas-pump.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '5e926d0b-c0ce-4cda-8027-a4553f9978ac'
SOURCE_PATH = 'pictographic-primitives/symbol/gas pump_5e926d0b-c0ce-4cda-8027-a4553f9978ac.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('5e926d0b-c0ce-4cda-8027-a4553f9978ac', 'pictographic-primitives/symbol/gas pump_5e926d0b-c0ce-4cda-8027-a4553f9978ac.svg'),)
PROFILE_SOURCE_KEYS = ('solo/gas-pump',)
SOLO_SOURCE_ICON_IDS = ('gas-pump',)
REFERENCE_EXPORT_SHA256 = 'cd33e5be5d2f2c091c37a189d5e3ee444d9ae995e4889d225189dfafe331ddc0'

class Drawing(Sub32):
    icon_id = 'gas-pump-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (8, 2), (16, 2))
        self.add_bezier('p1-r1-2', (16, 2), ((18, 2), (20, 3), (20, 4)))
        self.add_line('p1-r1-3', (20, 4), (20, 24))
        self.add_line('p1-r1-4', (20, 24), (20, 28))
        self.add_bezier('p1-r1-5', (20, 28), ((20, 29), (18, 30), (16, 30)))
        self.add_line('p1-r1-6', (16, 30), (8, 30))
        self.add_bezier('p1-r1-7', (8, 30), ((6, 30), (4, 30), (4, 28)))
        self.add_line('p1-r1-8', (4, 28), (4, 4))
        self.add_bezier('p1-r1-9', (4, 4), ((4, 3), (6, 2), (8, 2)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', closed=False)
        self.add_line('p2-r1-1', (12, 10), (12, 10))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (20, 24), (23, 24))
        self.add_bezier('p3-r1-2', (23, 24), ((23, 24), (23, 24), (23, 24)))
        self.add_bezier('p3-r1-3', (23, 24), ((26, 24), (28, 22), (28, 20)))
        self.add_line('p3-r1-4', (28, 20), (28, 10))
        self.add_bezier('p3-r1-5', (28, 10), ((28, 9), (27, 8), (26, 8)))
        self.add_bezier('p3-r1-6', (26, 8), ((26, 8), (25, 8), (24, 8)))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', 'p3-r1-6', closed=False)
        self.relate('connect', 'p1-r1-3', 'p3-r1-1')
        self.relate('connect', 'p1-r1-4', 'p3-r1-1')
