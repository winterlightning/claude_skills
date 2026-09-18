"""Independent 32px profile of rosette-ribbon.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '4b8d63df-19f2-40b4-a07b-b9f5c17ba2a9'
SOURCE_PATH = 'pictographic-primitives/symbol/ribbon_4b8d63df-19f2-40b4-a07b-b9f5c17ba2a9.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('4b8d63df-19f2-40b4-a07b-b9f5c17ba2a9', 'pictographic-primitives/symbol/ribbon_4b8d63df-19f2-40b4-a07b-b9f5c17ba2a9.svg'),)
PROFILE_SOURCE_KEYS = ('solo/rosette-ribbon',)
SOLO_SOURCE_ICON_IDS = ('rosette-ribbon',)
REFERENCE_EXPORT_SHA256 = '1cbfb17661c7d9a0d7c112837ae221bf1e9ff4f741bbee4551b45bb872a54955'

class Drawing(Sub32):
    icon_id = 'rosette-ribbon-sub32'
    keyshape = Keyshape.VRECT_L
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/symbols'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (10, 5), (22, 5), radius_x=6, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (22, 5), (24, 8), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (24, 8), (24, 13), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p1-r1-4', (24, 13), (22, 16), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p1-r1-5', (22, 16), (10, 16), radius_x=6, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p1-r1-6', (10, 16), (8, 13), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p1-r1-7', (8, 13), (8, 8), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p1-r1-8', (8, 8), (10, 5), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_arc('p2-r1-1', (14, 10), (18, 10), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('p2-r1-2', (18, 10), (14, 10), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (8, 13), (8, 30))
        self.add_line('p3-r1-2', (8, 30), (16, 24))
        self.add_line('p3-r1-3', (16, 24), (24, 30))
        self.add_line('p3-r1-4', (24, 30), (24, 13))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.relate("connect", 'p1-r1-3', 'p3-r1-4')
        self.relate("connect", 'p1-r1-4', 'p3-r1-4')
        self.relate("connect", 'p1-r1-6', 'p3-r1-1')
        self.relate("connect", 'p1-r1-7', 'p3-r1-1')
