"""Independent 32px profile of grid-globe.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'f68cfed4-af07-4707-93e1-6c92d2e4e588'
SOURCE_PATH = 'pictographic-primitives/maps/earth_f68cfed4-af07-4707-93e1-6c92d2e4e588.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('f68cfed4-af07-4707-93e1-6c92d2e4e588', 'pictographic-primitives/maps/earth_f68cfed4-af07-4707-93e1-6c92d2e4e588.svg'),)
PROFILE_SOURCE_KEYS = ('solo/grid-globe',)
SOLO_SOURCE_ICON_IDS = ('grid-globe',)
REFERENCE_EXPORT_SHA256 = 'a453e1b32864b0cbb9a7d310bda7543aa788eb898dee362ded5855db863c554c'

class Drawing(Sub32):
    icon_id = 'grid-globe-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/maps'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (16, 2), (24, 5), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (24, 5), (30, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (30, 16), (24, 27), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p1-r1-4', (24, 27), (16, 30), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p1-r1-5', (16, 30), (8, 27), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p1-r1-6', (8, 27), (2, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p1-r1-7', (2, 16), (8, 5), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p1-r1-8', (8, 5), (16, 2), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_line('p2-r1-1', (8, 5), (8, 16))
        self.add_line('p2-r1-2', (8, 16), (8, 27))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (24, 5), (24, 16))
        self.add_line('p3-r1-2', (24, 16), (24, 27))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_line('p4-r1-1', (2, 16), (8, 16))
        self.add_line('p4-r1-2', (8, 16), (24, 16))
        self.add_line('p4-r1-3', (24, 16), (30, 16))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', closed=False)
        self.relate("connect", 'p1-r1-1', 'p3-r1-1')
        self.relate("connect", 'p1-r1-2', 'p3-r1-1')
        self.relate("connect", 'p1-r1-2', 'p4-r1-3')
        self.relate("connect", 'p1-r1-3', 'p3-r1-2')
        self.relate("connect", 'p1-r1-3', 'p4-r1-3')
        self.relate("connect", 'p1-r1-4', 'p3-r1-2')
        self.relate("connect", 'p1-r1-5', 'p2-r1-2')
        self.relate("connect", 'p1-r1-6', 'p2-r1-2')
        self.relate("connect", 'p1-r1-6', 'p4-r1-1')
        self.relate("connect", 'p1-r1-7', 'p2-r1-1')
        self.relate("connect", 'p1-r1-7', 'p4-r1-1')
        self.relate("connect", 'p1-r1-8', 'p2-r1-1')
        self.relate("connect", 'p2-r1-1', 'p4-r1-1')
        self.relate("connect", 'p2-r1-1', 'p4-r1-2')
        self.relate("connect", 'p2-r1-2', 'p4-r1-1')
        self.relate("connect", 'p2-r1-2', 'p4-r1-2')
        self.relate("connect", 'p3-r1-1', 'p4-r1-2')
        self.relate("connect", 'p3-r1-1', 'p4-r1-3')
        self.relate("connect", 'p3-r1-2', 'p4-r1-2')
        self.relate("connect", 'p3-r1-2', 'p4-r1-3')
