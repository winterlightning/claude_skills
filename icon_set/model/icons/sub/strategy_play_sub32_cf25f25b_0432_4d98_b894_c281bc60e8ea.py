"""Independent 32px profile of strategy-play.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'cf25f25b-0432-4d98-b894-c281bc60e8ea'
SOURCE_PATH = 'pictographic-primitives/symbol/strategy_cf25f25b-0432-4d98-b894-c281bc60e8ea.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('cf25f25b-0432-4d98-b894-c281bc60e8ea', 'pictographic-primitives/symbol/strategy_cf25f25b-0432-4d98-b894-c281bc60e8ea.svg'),)
PROFILE_SOURCE_KEYS = ('solo/strategy-play',)
SOLO_SOURCE_ICON_IDS = ('strategy-play',)
REFERENCE_EXPORT_SHA256 = '12f2cddb08d6a6b936834fd64f3caf3b6e1043a25627b64dfe1fddcf92081101'

class Drawing(Sub32):
    icon_id = 'strategy-play-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/symbols'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (2, 27), (8, 27), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (8, 27), (2, 27), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (5, 24), (5, 23))
        self.add_arc('p2-r1-2', (5, 23), (13, 15), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_line('p2-r1-3', (13, 15), (19, 15))
        self.add_arc('p2-r1-4', (19, 15), (27, 7), radius_x=8, radius_y=8, large_arc=False, sweep=False)
        self.add_line('p2-r1-5', (27, 7), (27, 2))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
        self.add_line('p3-r1-1', (22, 7), (27, 2))
        self.add_line('p3-r1-2', (27, 2), (30, 7))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_line('p4-r1-1', (2, 2), (5, 5))
        self.add_line('p4-r1-2', (5, 5), (8, 8))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_line('p5-r1-1', (2, 8), (5, 5))
        self.add_line('p5-r1-2', (5, 5), (8, 2))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', closed=False)
        self.add_line('p6-r1-1', (24, 24), (27, 27))
        self.add_line('p6-r1-2', (27, 27), (30, 30))
        self.add_contour('path-6-1', 'p6-r1-1', 'p6-r1-2', closed=False)
        self.add_line('p7-r1-1', (24, 30), (27, 27))
        self.add_line('p7-r1-2', (27, 27), (30, 24))
        self.add_contour('path-7-1', 'p7-r1-1', 'p7-r1-2', closed=False)
        self.relate("connect", 'p2-r1-5', 'p3-r1-1')
        self.relate("connect", 'p2-r1-5', 'p3-r1-2')
        self.relate("connect", 'p4-r1-1', 'p5-r1-1')
        self.relate("connect", 'p4-r1-1', 'p5-r1-2')
        self.relate("connect", 'p4-r1-2', 'p5-r1-1')
        self.relate("connect", 'p4-r1-2', 'p5-r1-2')
        self.relate("connect", 'p6-r1-1', 'p7-r1-1')
        self.relate("connect", 'p6-r1-1', 'p7-r1-2')
        self.relate("connect", 'p6-r1-2', 'p7-r1-1')
        self.relate("connect", 'p6-r1-2', 'p7-r1-2')
