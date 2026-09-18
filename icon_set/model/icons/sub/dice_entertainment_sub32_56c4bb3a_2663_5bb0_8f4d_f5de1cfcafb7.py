"""Independent 32px profile of dice-entertainment.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '56c4bb3a-2663-5bb0-8f4d-f5de1cfcafb7'
SOURCE_PATH = 'pictographic-primitives/entertainment/dice_56c4bb3a-2663-5bb0-8f4d-f5de1cfcafb7.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('56c4bb3a-2663-5bb0-8f4d-f5de1cfcafb7', 'pictographic-primitives/entertainment/dice_56c4bb3a-2663-5bb0-8f4d-f5de1cfcafb7.svg'),)
PROFILE_SOURCE_KEYS = ('solo/dice-entertainment',)
SOLO_SOURCE_ICON_IDS = ('dice-entertainment',)
REFERENCE_EXPORT_SHA256 = '65cd5fc7a2d62dbf513efd8d82ba848c9fd30f4cb3da305163c379d5ae67f3b7'

class Drawing(Sub32):
    icon_id = 'dice-entertainment-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'entertainment'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (7, 30), (4, 29))
        self.add_arc('p1-r1-2', (4, 29), (2, 25), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (2, 25), (2, 25))
        self.add_line('p1-r1-4', (2, 25), (2, 7))
        self.add_arc('p1-r1-5', (2, 7), (7, 2), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('p1-r1-6', (7, 2), (25, 2))
        self.add_bezier('p1-r1-7', (25, 2), ((26, 2), (27, 3), (28, 3)))
        self.add_bezier('p1-r1-8', (28, 3), ((29, 4), (30, 5), (30, 6)))
        self.add_line('p1-r1-9', (30, 6), (30, 25))
        self.add_line('p1-r1-10', (30, 25), (30, 25))
        self.add_arc('p1-r1-11', (30, 25), (25, 30), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('p1-r1-12', (25, 30), (25, 30))
        self.add_line('p1-r1-13', (25, 30), (7, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', 'p1-r1-13', closed=False)
        self.add_arc('p2-r1-1', (9, 9), (9, 10), radius_x=12, radius_y=12, large_arc=False, sweep=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_arc('p3-r1-1', (23, 9), (23, 10), radius_x=16, radius_y=16, large_arc=False, sweep=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_arc('p4-r1-1', (23, 22), (23, 23), radius_x=26, radius_y=26, large_arc=False, sweep=False)
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_arc('p5-r1-1', (16, 16), (16, 17), radius_x=19, radius_y=19, large_arc=False, sweep=False)
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_arc('p6-r1-1', (9, 22), (9, 23), radius_x=34, radius_y=34, large_arc=False, sweep=False)
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
