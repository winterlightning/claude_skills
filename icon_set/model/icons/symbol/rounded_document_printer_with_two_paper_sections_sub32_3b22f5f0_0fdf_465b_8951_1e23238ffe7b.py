"""Independent 32px profile of rounded-document-printer-with-two-paper-sections.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '3b22f5f0-0fdf-465b-8951-1e23238ffe7b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/devices/printer_3b22f5f0-0fdf-465b-8951-1e23238ffe7b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('3b22f5f0-0fdf-465b-8951-1e23238ffe7b', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/devices/printer_3b22f5f0-0fdf-465b-8951-1e23238ffe7b.svg'),)
PROFILE_SOURCE_KEYS = ('solo/rounded-document-printer-with-two-paper-sections',)
SOLO_SOURCE_ICON_IDS = ('rounded-document-printer-with-two-paper-sections',)
REFERENCE_EXPORT_SHA256 = 'a8677faf3717798c233097040d86daf5528c337149aa2ecb89f5f9e5f76b295a'

class Drawing(Sub32):
    icon_id = 'rounded-document-printer-with-two-paper-sections-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'devices'
    categories = ('devices', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Printer: paper on top, rounded body, output paper below, each 8 units clear.
        self.add_line('p1-r1-1', (5, 10), (8, 10))
        self.add_line('p1-r1-2', (8, 10), (24, 10))
        self.add_line('p1-r1-3', (24, 10), (27, 10))
        self.add_arc('p1-r1-4', (27, 10), (30, 13), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-5', (30, 13), (30, 19))
        self.add_arc('p1-r1-6', (30, 19), (27, 22), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-7', (27, 22), (24, 22))
        self.add_line('p1-r1-8', (24, 22), (8, 22))
        self.add_line('p1-r1-9', (8, 22), (5, 22))
        self.add_arc('p1-r1-10', (5, 22), (2, 19), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-11', (2, 19), (2, 13))
        self.add_arc('p1-r1-12', (2, 13), (5, 10), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', closed=True)
        self.add_line('p2-r1-1', (8, 10), (8, 2))
        self.add_line('p2-r1-2', (8, 2), (24, 2))
        self.add_line('p2-r1-3', (24, 2), (24, 10))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_line('p3-r1-1', (8, 22), (8, 30))
        self.add_line('p3-r1-2', (8, 30), (24, 30))
        self.add_line('p3-r1-3', (24, 30), (24, 22))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
        for a, b in (('p1-r1-1', 'p2-r1-1'), ('p1-r1-2', 'p2-r1-1'), ('p1-r1-2', 'p2-r1-3'), ('p1-r1-3', 'p2-r1-3'),
                     ('p1-r1-8', 'p3-r1-1'), ('p1-r1-9', 'p3-r1-1'), ('p1-r1-7', 'p3-r1-3'), ('p1-r1-8', 'p3-r1-3')):
            self.relate('connect', a, b)
