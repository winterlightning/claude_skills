"""Independent 32px profile of person-with-presentation-board.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
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
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Person beside a presentation board, 4 units apart.
        self.add_polyline('board', (2, 4), (14, 4), (14, 16), (2, 16), closed=True)
        self.add_arc('head-1', (22, 9), (30, 9), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('head-2', (30, 9), (22, 9), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('head', 'head-1', 'head-2', closed=True)
        self.add_line('s-1', (20, 28), (20, 26))
        self.add_arc('s-2', (20, 26), (30, 26), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('s-3', (30, 26), (30, 28))
        self.add_contour('shoulders', 's-1', 's-2', 's-3')
