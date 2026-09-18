"""Independent 32px profile of personal-hotspot.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '45b73137-0503-4586-8373-394aa93d3ff8'
SOURCE_PATH = 'pictographic-primitives/symbol/personal hotspot_45b73137-0503-4586-8373-394aa93d3ff8.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('45b73137-0503-4586-8373-394aa93d3ff8', 'pictographic-primitives/symbol/personal hotspot_45b73137-0503-4586-8373-394aa93d3ff8.svg'),)
PROFILE_SOURCE_KEYS = ('solo/personal-hotspot',)
SOLO_SOURCE_ICON_IDS = ('personal-hotspot',)
REFERENCE_EXPORT_SHA256 = '3081e67b396e4bf666300a0653f366436ba9f7cf669b5ce3d638d80a853f779e'

class Drawing(Sub32):
    icon_id = 'personal-hotspot-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (20, 12), (13, 12))
        self.add_bezier('p1-r1-2', (13, 12), ((10, 12), (7, 17), (7, 21)))
        self.add_bezier('p1-r1-3', (7, 21), ((7, 21), (7, 22), (7, 23)))
        self.add_bezier('p1-r1-4', (7, 23), ((8, 26), (11, 27), (14, 27)))
        self.add_bezier('p1-r1-5', (14, 27), ((14, 27), (14, 27), (14, 27)))
        self.add_bezier('p1-r1-6', (14, 27), ((14, 27), (14, 27), (14, 27)))
        self.add_bezier('p1-r1-7', (14, 27), ((14, 27), (14, 27), (14, 27)))
        self.add_line('p1-r1-8', (14, 27), (22, 27))
        self.add_bezier('p1-r1-9', (22, 27), ((22, 27), (22, 27), (22, 27)))
        self.add_bezier('p1-r1-10', (22, 27), ((25, 27), (28, 27), (29, 24)))
        self.add_bezier('p1-r1-11', (29, 24), ((30, 23), (30, 22), (30, 22)))
        self.add_bezier('p1-r1-12', (30, 22), ((30, 22), (30, 22), (30, 22)))
        self.add_bezier('p1-r1-13', (30, 22), ((30, 21), (30, 20), (30, 19)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', 'p1-r1-13', closed=False)
        self.add_bezier('p2-r1-1', (2, 14), ((2, 13), (2, 12), (2, 11)))
        self.add_bezier('p2-r1-2', (2, 11), ((2, 11), (2, 10), (2, 10)))
        self.add_bezier('p2-r1-3', (2, 10), ((4, 7), (7, 5), (9, 5)))
        self.add_bezier('p2-r1-4', (9, 5), ((10, 5), (10, 5), (10, 5)))
        self.add_line('p2-r1-5', (10, 5), (20, 5))
        self.add_bezier('p2-r1-6', (20, 5), ((20, 5), (20, 5), (20, 5)))
        self.add_bezier('p2-r1-7', (20, 5), ((21, 5), (22, 5), (23, 5)))
        self.add_bezier('p2-r1-8', (23, 5), ((25, 6), (26, 9), (26, 11)))
        self.add_bezier('p2-r1-9', (26, 11), ((26, 13), (25, 16), (24, 18)))
        self.add_bezier('p2-r1-10', (24, 18), ((22, 19), (20, 20), (18, 20)))
        self.add_bezier('p2-r1-11', (18, 20), ((17, 20), (16, 19), (15, 19)))
        self.add_bezier('p2-r1-12', (15, 19), ((14, 19), (14, 19), (14, 19)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', 'p2-r1-8', 'p2-r1-9', 'p2-r1-10', 'p2-r1-11', 'p2-r1-12', closed=False)
