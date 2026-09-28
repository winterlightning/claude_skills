"""Independent 32px profile of standing-human-figure.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'de7e132d-7335-404c-ba94-0dc5f8acf724'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/full body person_de7e132d-7335-404c-ba94-0dc5f8acf724.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('de7e132d-7335-404c-ba94-0dc5f8acf724', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/full body person_de7e132d-7335-404c-ba94-0dc5f8acf724.svg'),)
PROFILE_SOURCE_KEYS = ('solo/standing-human-figure',)
SOLO_SOURCE_ICON_IDS = ('standing-human-figure',)
REFERENCE_EXPORT_SHA256 = '7f696c40b0b44efb4723e7e4f2a256b7f9a6b81dba00b5d61c826645bf492652'

class Drawing(Sub32):
    icon_id = 'standing-human-figure-sub32'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives-generate'
    categories = ('symbol', 'state', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (12, 6), (16, 2), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (16, 2), (20, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (20, 6), (16, 10), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p1-r1-4', (16, 10), (12, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_arc('p2-r1-1', (6, 22), (16, 16), radius_x=10, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('p2-r1-2', (16, 16), (26, 22), radius_x=10, radius_y=6, large_arc=False, sweep=True)
        self.add_line('p2-r1-3', (26, 22), (26, 24))
        self.add_line('p2-r1-4', (26, 24), (22, 24))
        self.add_line('p2-r1-5', (22, 24), (20, 30))
        self.add_line('p2-r1-6', (20, 30), (12, 30))
        self.add_line('p2-r1-7', (12, 30), (10, 24))
        self.add_line('p2-r1-8', (10, 24), (6, 24))
        self.add_line('p2-r1-9', (6, 24), (6, 22))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', 'p2-r1-8', 'p2-r1-9', closed=False)
