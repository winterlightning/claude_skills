"""Independent 32px profile of person-with-presentation-board.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '9fa20be8-04fc-4e2a-a019-e3c81b35c5a7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/man square_9fa20be8-04fc-4e2a-a019-e3c81b35c5a7.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('9fa20be8-04fc-4e2a-a019-e3c81b35c5a7', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/man square_9fa20be8-04fc-4e2a-a019-e3c81b35c5a7.svg'),)
PROFILE_SOURCE_KEYS = ('solo/person-with-presentation-board',)
SOLO_SOURCE_ICON_IDS = ('person-with-presentation-board',)
REFERENCE_EXPORT_SHA256 = 'c5a53a5c8e958380e958cf26fd8f293917ed7f35dd5cb19299842d1e760adc41'

class Drawing(Sub32):
    icon_id = 'person-with-presentation-board-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/container-components'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (3, 5), (12, 5))
        self.add_arc('p1-r1-2', (12, 5), (13, 6), radius_x=1, radius_y=1, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (13, 6), (13, 13))
        self.add_arc('p1-r1-4', (13, 13), (12, 15), radius_x=1.118033988749895, radius_y=1.118033988749895, large_arc=False, sweep=True)
        self.add_line('p1-r1-5', (12, 15), (3, 15))
        self.add_bezier('p1-r1-6', (3, 15), ((3, 15), (3, 14), (2, 14)))
        self.add_bezier('p1-r1-7', (2, 14), ((2, 14), (2, 14), (2, 13)))
        self.add_line('p1-r1-8', (2, 13), (2, 6))
        self.add_arc('p1-r1-9', (2, 6), (3, 5), radius_x=1, radius_y=1, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', closed=False)
        self.add_arc('p2-r1-1', (21, 10), (24, 7), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p2-r1-2', (24, 7), (28, 10), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p2-r1-3', (28, 10), (24, 14), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p2-r1-4', (24, 14), (21, 10), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_line('p3-r1-1', (19, 27), (19, 22))
        self.add_arc('p3-r1-2', (19, 22), (30, 22), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('p3-r1-3', (30, 22), (30, 27))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
