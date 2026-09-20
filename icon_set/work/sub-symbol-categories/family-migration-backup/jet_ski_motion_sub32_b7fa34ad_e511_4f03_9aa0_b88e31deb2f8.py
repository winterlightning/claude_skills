"""Independent 32px profile of jet-ski-motion.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'b7fa34ad-e511-4f03-9aa0-b88e31deb2f8'
SOURCE_PATH = 'pictographic-primitives/symbol/water scooter_b7fa34ad-e511-4f03-9aa0-b88e31deb2f8.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('b7fa34ad-e511-4f03-9aa0-b88e31deb2f8', 'pictographic-primitives/symbol/water scooter_b7fa34ad-e511-4f03-9aa0-b88e31deb2f8.svg'),)
PROFILE_SOURCE_KEYS = ('solo/jet-ski-motion',)
SOLO_SOURCE_ICON_IDS = ('jet-ski-motion',)
REFERENCE_EXPORT_SHA256 = 'e2577ec44abbc3833925193c31b006ba4f1682a3214911d66ca91052bdb950f6'

class Drawing(Sub32):
    icon_id = 'jet-ski-motion-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/symbols'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 8), (14, 19))
        self.add_line('p1-r1-2', (14, 19), (22, 14))
        self.add_line('p1-r1-3', (22, 14), (16, 11))
        self.add_line('p1-r1-4', (16, 11), (7, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (16, 11), (16, 2))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (2, 21), (11, 27))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (2, 28), (4, 30))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_arc('p5-r1-1', (19, 27), (25, 27), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_bezier('p5-r1-2', (25, 27), ((25, 29), (26, 30), (28, 30)))
        self.add_bezier('p5-r1-3', (28, 30), ((29, 30), (30, 29), (30, 27)))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', 'p5-r1-3', closed=False)
        self.relate("connect", 'p1-r1-3', 'p2-r1-1')
        self.relate("connect", 'p1-r1-4', 'p2-r1-1')
