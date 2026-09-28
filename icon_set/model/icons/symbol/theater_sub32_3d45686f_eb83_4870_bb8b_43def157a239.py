"""Independent 32px profile of theater.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '3d45686f-eb83-4870-bb8b-43def157a239'
SOURCE_PATH = 'pictographic-primitives/symbol/theater_3d45686f-eb83-4870-bb8b-43def157a239.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('3d45686f-eb83-4870-bb8b-43def157a239', 'pictographic-primitives/symbol/theater_3d45686f-eb83-4870-bb8b-43def157a239.svg'),)
PROFILE_SOURCE_KEYS = ('solo/theater',)
SOLO_SOURCE_ICON_IDS = ('theater',)
REFERENCE_EXPORT_SHA256 = 'a80ae220b88e468166f966b1969937a8a884017eb25e90a5e8b46779f09287c8'

class Drawing(Sub32):
    icon_id = 'theater-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (4, 2), (10, 2))
        self.add_line('p1-r1-2', (10, 2), (22, 2))
        self.add_line('p1-r1-3', (22, 2), (28, 2))
        self.add_arc('p1-r1-4', (28, 2), (30, 4), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p1-r1-5', (30, 4), (30, 10))
        self.add_line('p1-r1-6', (30, 10), (30, 28))
        self.add_arc('p1-r1-7', (30, 28), (28, 30), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p1-r1-8', (28, 30), (22, 30))
        self.add_line('p1-r1-9', (22, 30), (10, 30))
        self.add_line('p1-r1-10', (10, 30), (4, 30))
        self.add_arc('p1-r1-11', (4, 30), (2, 28), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p1-r1-12', (2, 28), (2, 10))
        self.add_line('p1-r1-13', (2, 10), (2, 4))
        self.add_arc('p1-r1-14', (2, 4), (4, 2), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', 'p1-r1-13', 'p1-r1-14', closed=False)
        self.add_line('p2-r1-1', (2, 10), (30, 10))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_bezier('p3-r1-1', (2, 10), ((10, 13), (10, 22), (10, 30)))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_bezier('p4-r1-1', (30, 10), ((22, 13), (22, 22), (22, 30)))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate('connect', 'p1-r1-5', 'p2-r1-1')
        self.relate('connect', 'p1-r1-5', 'p4-r1-1')
        self.relate('connect', 'p1-r1-6', 'p2-r1-1')
        self.relate('connect', 'p1-r1-6', 'p4-r1-1')
        self.relate('connect', 'p1-r1-8', 'p4-r1-1')
        self.relate('connect', 'p1-r1-9', 'p3-r1-1')
        self.relate('connect', 'p1-r1-9', 'p4-r1-1')
        self.relate('connect', 'p1-r1-10', 'p3-r1-1')
        self.relate('connect', 'p1-r1-12', 'p2-r1-1')
        self.relate('connect', 'p1-r1-12', 'p3-r1-1')
        self.relate('connect', 'p1-r1-13', 'p2-r1-1')
        self.relate('connect', 'p1-r1-13', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p4-r1-1')
