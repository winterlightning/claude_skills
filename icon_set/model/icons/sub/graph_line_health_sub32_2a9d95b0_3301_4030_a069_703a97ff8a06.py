"""Independent 32px profile of graph-line-health.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '2a9d95b0-3301-4030-a069-703a97ff8a06'
SOURCE_PATH = 'pictographic-primitives/health/graph line_2a9d95b0-3301-4030-a069-703a97ff8a06.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('2a9d95b0-3301-4030-a069-703a97ff8a06', 'pictographic-primitives/health/graph line_2a9d95b0-3301-4030-a069-703a97ff8a06.svg'),)
PROFILE_SOURCE_KEYS = ('solo/graph-line-health',)
SOLO_SOURCE_ICON_IDS = ('graph-line-health',)
REFERENCE_EXPORT_SHA256 = '357849dafd9624ac81e7d738906047483cd470237e34fe60b4b6e8bd1d78931d'

class Drawing(Sub32):
    icon_id = 'graph-line-health-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'health'
    categories = ('health', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (24, 13), (24, 16))
        self.add_line('p1-r1-2', (24, 16), (25, 17))
        self.add_line('p1-r1-3', (25, 17), (30, 18))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (2, 18), (8, 18))
        self.add_arc('p2-r1-2', (8, 18), (11, 15), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('p2-r1-3', (11, 15), (13, 5))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_line('p3-r1-1', (13, 5), (19, 27))
        self.add_line('p3-r1-2', (19, 27), (24, 13))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.relate("connect", 'p1-r1-1', 'p3-r1-2')
        self.relate("connect", 'p2-r1-3', 'p3-r1-1')
