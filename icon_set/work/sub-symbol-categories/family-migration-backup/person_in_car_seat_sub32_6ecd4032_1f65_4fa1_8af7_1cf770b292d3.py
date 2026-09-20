"""Independent 32px profile of person-in-car-seat.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '6ecd4032-1f65-4fa1-8af7-1cf770b292d3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/state/person with seat_6ecd4032-1f65-4fa1-8af7-1cf770b292d3.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('6ecd4032-1f65-4fa1-8af7-1cf770b292d3', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/state/person with seat_6ecd4032-1f65-4fa1-8af7-1cf770b292d3.svg'),)
PROFILE_SOURCE_KEYS = ('solo/person-in-car-seat',)
SOLO_SOURCE_ICON_IDS = ('person-in-car-seat',)
REFERENCE_EXPORT_SHA256 = 'ae12ec7071d82a451c117db4bbcdbabcfd97baf4b3d95028e7601f5d99b0a889'

class Drawing(Sub32):
    icon_id = 'person-in-car-seat-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/container-components'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (16, 10), (16, 2), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (16, 2), (16, 10), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (16, 16), (16, 22))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (16, 22), (24, 22))
        self.add_line('p3-r1-2', (24, 22), (30, 28))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_line('p4-r1-1', (16, 16), (23, 16))
        self.add_line('p4-r1-2', (23, 16), (28, 11))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_line('p5-r1-1', (2, 15), (2, 24))
        self.add_arc('p5-r1-2', (2, 24), (8, 30), radius_x=6, radius_y=6, large_arc=False, sweep=False)
        self.add_line('p5-r1-3', (8, 30), (22, 30))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', 'p5-r1-3', closed=False)
        self.relate("connect", 'p2-r1-1', 'p3-r1-1')
        self.relate("connect", 'p2-r1-1', 'p4-r1-1')
