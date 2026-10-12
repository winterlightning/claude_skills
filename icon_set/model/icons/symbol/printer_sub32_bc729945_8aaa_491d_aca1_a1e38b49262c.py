"""Independent 32px profile of printer.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'bc729945-8aaa-491d-aca1-a1e38b49262c'
SOURCE_PATH = 'pictographic-primitives/devices/printer_bc729945-8aaa-491d-aca1-a1e38b49262c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('bc729945-8aaa-491d-aca1-a1e38b49262c', 'pictographic-primitives/devices/printer_bc729945-8aaa-491d-aca1-a1e38b49262c.svg'),)
PROFILE_SOURCE_KEYS = ('solo/printer',)
SOLO_SOURCE_ICON_IDS = ('printer',)
REFERENCE_EXPORT_SHA256 = '09561cf6599a9b54d69a17844e84576ee96a663a3c107aa9411d5a1d2d3b6ad6'

class Drawing(Sub32):
    icon_id = 'printer-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'devices'
    categories = ('devices', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (23, 12), (23, 4))
        self.add_line('p1-r1-2', (23, 4), (22, 4))
        self.add_line('p1-r1-3', (22, 4), (20, 2))
        self.add_line('p1-r1-4', (20, 2), (10, 2))
        self.add_arc('p1-r1-5', (10, 2), (9, 3), radius_x=12, radius_y=12, large_arc=False, sweep=False)
        self.add_line('p1-r1-6', (9, 3), (9, 12))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_line('p2-r1-1', (24, 20), (26, 30))
        self.add_line('p2-r1-2', (26, 30), (6, 30))
        self.add_line('p2-r1-3', (6, 30), (8, 20))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_line('p3-r1-1', (28, 12), (28, 19))
        self.add_arc('p3-r1-2', (28, 19), (27, 20), radius_x=1, radius_y=1, large_arc=False, sweep=True)
        self.add_line('p3-r1-3', (27, 20), (5, 20))
        self.add_arc('p3-r1-4', (5, 20), (4, 19), radius_x=1, radius_y=1, large_arc=False, sweep=True)
        self.add_line('p3-r1-5', (4, 19), (4, 12))
        self.add_line('p3-r1-6', (4, 12), (28, 12))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', 'p3-r1-6', closed=False)
