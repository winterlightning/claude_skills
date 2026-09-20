"""Independent 32px profile of rounded-document-printer-with-two-paper-sections.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

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
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/devices'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (8, 24), (5, 24))
        self.add_arc('p1-r1-2', (5, 24), (2, 21), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (2, 21), (2, 14))
        self.add_arc('p1-r1-4', (2, 14), (5, 11), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-5', (5, 11), (8, 11))
        self.add_line('p1-r1-6', (8, 11), (24, 11))
        self.add_line('p1-r1-7', (24, 11), (27, 11))
        self.add_arc('p1-r1-8', (27, 11), (30, 14), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-9', (30, 14), (30, 21))
        self.add_arc('p1-r1-10', (30, 21), (27, 24), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-11', (27, 24), (24, 24))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', closed=False)
        self.add_line('p2-r1-1', (8, 11), (8, 2))
        self.add_line('p2-r1-2', (8, 2), (19, 2))
        self.add_line('p2-r1-3', (19, 2), (24, 7))
        self.add_line('p2-r1-4', (24, 7), (24, 11))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_line('p3-r1-1', (8, 24), (8, 18))
        self.add_line('p3-r1-2', (8, 18), (24, 18))
        self.add_line('p3-r1-3', (24, 18), (24, 24))
        self.add_line('p3-r1-4', (24, 24), (24, 30))
        self.add_line('p3-r1-5', (24, 30), (8, 30))
        self.add_line('p3-r1-6', (8, 30), (8, 24))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', 'p3-r1-6', closed=False)
        self.relate("connect", 'p1-r1-1', 'p3-r1-1')
        self.relate("connect", 'p1-r1-1', 'p3-r1-6')
        self.relate("connect", 'p1-r1-5', 'p2-r1-1')
        self.relate("connect", 'p1-r1-6', 'p2-r1-1')
        self.relate("connect", 'p1-r1-6', 'p2-r1-4')
        self.relate("connect", 'p1-r1-7', 'p2-r1-4')
        self.relate("connect", 'p1-r1-11', 'p3-r1-3')
        self.relate("connect", 'p1-r1-11', 'p3-r1-4')
