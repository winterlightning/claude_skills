"""Independent 32px profile of vote.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '18b92527-4c62-4167-b94f-8857d15829a6'
SOURCE_PATH = 'pictographic-primitives/symbol/vote_18b92527-4c62-4167-b94f-8857d15829a6.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('18b92527-4c62-4167-b94f-8857d15829a6', 'pictographic-primitives/symbol/vote_18b92527-4c62-4167-b94f-8857d15829a6.svg'),)
PROFILE_SOURCE_KEYS = ('solo/vote',)
SOLO_SOURCE_ICON_IDS = ('vote',)
REFERENCE_EXPORT_SHA256 = 'dddbb4b24e42c697734dab8b9507f80cb47776516dbec058ed4fde1d86d472b9'

class Drawing(Sub32):
    icon_id = 'vote-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (16, 2), (23, 9))
        self.add_line('p1-r1-2', (23, 9), (16, 16))
        self.add_line('p1-r1-3', (16, 16), (9, 9))
        self.add_line('p1-r1-4', (9, 9), (16, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (8, 16), (16, 16))
        self.add_line('p2-r1-2', (16, 16), (24, 16))
        self.add_arc('p2-r1-3', (24, 16), (27, 19), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p2-r1-4', (27, 19), (27, 27))
        self.add_arc('p2-r1-5', (27, 27), (24, 30), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p2-r1-6', (24, 30), (16, 30))
        self.add_line('p2-r1-7', (16, 30), (8, 30))
        self.add_arc('p2-r1-8', (8, 30), (5, 27), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p2-r1-9', (5, 27), (5, 19))
        self.add_arc('p2-r1-10', (5, 19), (8, 16), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', 'p2-r1-8', 'p2-r1-9', 'p2-r1-10', closed=False)
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-2')
        self.relate('connect', 'p1-r1-3', 'p2-r1-1')
        self.relate('connect', 'p1-r1-3', 'p2-r1-2')
