"""Independent 32px profile of cycling.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '8d3730da-df45-48a8-9d4e-6cf0a350df28'
SOURCE_PATH = 'pictographic-primitives/symbol/cycling_8d3730da-df45-48a8-9d4e-6cf0a350df28.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('8d3730da-df45-48a8-9d4e-6cf0a350df28', 'pictographic-primitives/symbol/cycling_8d3730da-df45-48a8-9d4e-6cf0a350df28.svg'),)
PROFILE_SOURCE_KEYS = ('solo/cycling',)
SOLO_SOURCE_ICON_IDS = ('cycling',)
REFERENCE_EXPORT_SHA256 = '79f19792932b7ed28723b4f90d07ff21bb1c8645dcd232b4737940c04059f98b'

class Drawing(Sub32):
    icon_id = 'cycling-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbols/standalone'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (6, 22), (6, 30), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (6, 30), (6, 22), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_arc('p2-r1-1', (26, 22), (26, 30), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p2-r1-2', (26, 30), (26, 22), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_arc('p3-r1-1', (19, 2), (19, 8), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p3-r1-2', (19, 8), (19, 2), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_bezier('p4-r1-1', (19, 14), ((19, 16), (17, 16), (15, 16)))
        self.add_bezier('p4-r1-2', (15, 16), ((13, 16), (12, 16), (11, 16)))
        self.add_bezier('p4-r1-3', (11, 16), ((11, 16), (10, 16), (10, 16)))
        self.add_line('p4-r1-4', (10, 16), (16, 19))
        self.add_line('p4-r1-5', (16, 19), (16, 21))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', 'p4-r1-5', closed=False)
        self.add_line('p5-r1-1', (19, 14), (21, 15))
        self.add_line('p5-r1-2', (21, 15), (27, 15))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', closed=False)
        self.relate("connect", 'p4-r1-1', 'p5-r1-1')
