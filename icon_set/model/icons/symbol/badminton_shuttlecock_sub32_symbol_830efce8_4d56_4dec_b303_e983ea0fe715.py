"""Independent 32px profile of badminton-shuttlecock.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '830efce8-4d56-4dec-b303-e983ea0fe715'
SOURCE_PATH = 'pictographic-primitives/symbol/shutterstock badminton_830efce8-4d56-4dec-b303-e983ea0fe715.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('830efce8-4d56-4dec-b303-e983ea0fe715', 'pictographic-primitives/symbol/shutterstock badminton_830efce8-4d56-4dec-b303-e983ea0fe715.svg'), ('a72d1038-bdfa-446e-bd28-56516d6ea08b', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/badminton ball_a72d1038-bdfa-446e-bd28-56516d6ea08b.svg'))
PROFILE_SOURCE_KEYS = ('solo/badminton-shuttlecock',)
SOLO_SOURCE_ICON_IDS = ('badminton-shuttlecock',)
REFERENCE_EXPORT_SHA256 = '27e0b5e5659b3f3520409839326142c2b17464982a08d3101bf443c24b0822f9'

class DrawingContainerSymbol(Sub32):
    icon_id = 'badminton-shuttlecock-sub32-symbol'
    related_origin_icon_id = 'badminton-shuttlecock-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/badminton-shuttlecock-sub32'
    counterpart_icon_id = 'badminton-shuttlecock-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (8, 18), (11, 5))
        self.add_arc('p1-r1-2', (11, 5), (19, 5), radius_x=4, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (19, 5), (27, 10), radius_x=8, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('p1-r1-4', (27, 10), (30, 18), radius_x=3, radius_y=8, large_arc=False, sweep=True)
        self.add_line('p1-r1-5', (30, 18), (14, 24))
        self.add_arc('p1-r1-6', (14, 24), (2, 24), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('p1-r1-7', (2, 24), (8, 18), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=False)
        self.add_line('p2-r1-1', (8, 18), (14, 24))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-5', 'p2-r1-1')
        self.relate('connect', 'p1-r1-6', 'p2-r1-1')
        self.relate('connect', 'p1-r1-7', 'p2-r1-1')
