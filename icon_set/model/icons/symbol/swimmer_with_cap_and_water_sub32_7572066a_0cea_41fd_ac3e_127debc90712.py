"""Independent 32px profile of swimmer-with-cap-and-water.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '7572066a-0cea-41fd-ac3e-127debc90712'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/state/swim compete_7572066a-0cea-41fd-ac3e-127debc90712.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('7572066a-0cea-41fd-ac3e-127debc90712', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/state/swim compete_7572066a-0cea-41fd-ac3e-127debc90712.svg'),)
PROFILE_SOURCE_KEYS = ('solo/swimmer-with-cap-and-water',)
SOLO_SOURCE_ICON_IDS = ('swimmer-with-cap-and-water',)
REFERENCE_EXPORT_SHA256 = '4eeea497954343d9b5627b02964c3fcd0433aff4ad6259f71c20e3642c36b876'

class Drawing(Sub32):
    icon_id = 'swimmer-with-cap-and-water-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (9, 9), (16, 2), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (16, 2), (23, 9), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (23, 9), (16, 16), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_arc('p1-r1-4', (16, 16), (9, 9), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (9, 9), (23, 9))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_arc('p3-r1-1', (8, 22), (16, 19), radius_x=8, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p3-r1-2', (16, 19), (24, 22), radius_x=8, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_bezier('p4-r1-1', (2, 30), ((7, 30), (7, 28), (11, 28)))
        self.add_bezier('p4-r1-2', (11, 28), ((16, 28), (16, 30), (21, 30)))
        self.add_bezier('p4-r1-3', (21, 30), ((25, 30), (25, 28), (30, 28)))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-3', 'p2-r1-1')
        self.relate('connect', 'p1-r1-4', 'p2-r1-1')
