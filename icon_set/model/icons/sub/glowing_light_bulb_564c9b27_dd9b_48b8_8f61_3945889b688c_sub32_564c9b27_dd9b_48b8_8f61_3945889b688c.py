"""Independent 32px profile of glowing-light-bulb-564c9b27-dd9b-48b8-8f61-3945889b688c.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '564c9b27-dd9b-48b8-8f61-3945889b688c'
SOURCE_PATH = 'pictographic-primitives/lights/light bulb 1_564c9b27-dd9b-48b8-8f61-3945889b688c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('564c9b27-dd9b-48b8-8f61-3945889b688c', 'pictographic-primitives/lights/light bulb 1_564c9b27-dd9b-48b8-8f61-3945889b688c.svg'),)
PROFILE_SOURCE_KEYS = ('solo/glowing-light-bulb-564c9b27-dd9b-48b8-8f61-3945889b688c',)
SOLO_SOURCE_ICON_IDS = ('glowing-light-bulb-564c9b27-dd9b-48b8-8f61-3945889b688c',)
REFERENCE_EXPORT_SHA256 = 'b70d54d9fde4151a94a831f8c44d9ec9d8445f885cb4a5a8b8bbe7e4352a158d'

class Drawing(Sub32):
    icon_id = 'glowing-light-bulb-564c9b27-dd9b-48b8-8f61-3945889b688c-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/lighting'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (10, 18), (22, 18), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (22, 18), (21, 21), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (21, 21), (19, 24), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_arc('p1-r1-4', (19, 24), (13, 24), radius_x=3, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('p1-r1-5', (13, 24), (11, 21), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_arc('p1-r1-6', (11, 21), (10, 18), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_line('p2-r1-1', (13, 24), (19, 24))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (16, 2), (16, 4))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (2, 18), (3, 18))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (5, 5), (7, 7))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (30, 18), (29, 18))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.add_line('p7-r1-1', (27, 5), (25, 7))
        self.add_contour('path-7-1', 'p7-r1-1', closed=False)
        self.relate("connect", 'p1-r1-3', 'p2-r1-1')
        self.relate("connect", 'p1-r1-4', 'p2-r1-1')
        self.relate("connect", 'p1-r1-5', 'p2-r1-1')
