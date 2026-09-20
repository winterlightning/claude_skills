"""Independent 32px profile of grid-four-squares.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'e611334b-e870-4c6a-94a2-cf370f8dd77f'
SOURCE_PATH = 'pictographic-primitives/symbol/grid of squares_e611334b-e870-4c6a-94a2-cf370f8dd77f.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('e611334b-e870-4c6a-94a2-cf370f8dd77f', 'pictographic-primitives/symbol/grid of squares_e611334b-e870-4c6a-94a2-cf370f8dd77f.svg'),)
PROFILE_SOURCE_KEYS = ('solo/grid-four-squares',)
SOLO_SOURCE_ICON_IDS = ('grid-four-squares',)
REFERENCE_EXPORT_SHA256 = '1a6d4ec901e79398b5955cca9e4179c30b25092d6c8e8aeb3ccdee8c15c5e0bf'

class Drawing(Sub32):
    icon_id = 'grid-four-squares-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/symbols'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (4, 2), (10, 2))
        self.add_arc('p1-r1-2', (10, 2), (11, 4), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (11, 4), (11, 10))
        self.add_arc('p1-r1-4', (11, 10), (10, 11), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p1-r1-5', (10, 11), (4, 11))
        self.add_arc('p1-r1-6', (4, 11), (2, 10), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p1-r1-7', (2, 10), (2, 4))
        self.add_arc('p1-r1-8', (2, 4), (4, 2), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_line('p2-r1-1', (22, 2), (28, 2))
        self.add_arc('p2-r1-2', (28, 2), (30, 4), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p2-r1-3', (30, 4), (30, 10))
        self.add_arc('p2-r1-4', (30, 10), (28, 11), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p2-r1-5', (28, 11), (22, 11))
        self.add_arc('p2-r1-6', (22, 11), (21, 10), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p2-r1-7', (21, 10), (21, 4))
        self.add_arc('p2-r1-8', (21, 4), (22, 2), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', 'p2-r1-8', closed=False)
        self.add_line('p3-r1-1', (4, 21), (10, 21))
        self.add_arc('p3-r1-2', (10, 21), (11, 22), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p3-r1-3', (11, 22), (11, 28))
        self.add_arc('p3-r1-4', (11, 28), (10, 30), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p3-r1-5', (10, 30), (4, 30))
        self.add_arc('p3-r1-6', (4, 30), (2, 28), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p3-r1-7', (2, 28), (2, 22))
        self.add_arc('p3-r1-8', (2, 22), (4, 21), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', 'p3-r1-6', 'p3-r1-7', 'p3-r1-8', closed=False)
        self.add_line('p4-r1-1', (22, 21), (28, 21))
        self.add_arc('p4-r1-2', (28, 21), (30, 22), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p4-r1-3', (30, 22), (30, 28))
        self.add_arc('p4-r1-4', (30, 28), (28, 30), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p4-r1-5', (28, 30), (22, 30))
        self.add_arc('p4-r1-6', (22, 30), (21, 28), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p4-r1-7', (21, 28), (21, 22))
        self.add_arc('p4-r1-8', (21, 22), (22, 21), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', 'p4-r1-5', 'p4-r1-6', 'p4-r1-7', 'p4-r1-8', closed=False)
