"""Independent 32px profile of camping-tent-outdoors.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '6abce5ce-492a-5630-a30e-c47fb4045166'
SOURCE_PATH = 'pictographic-primitives/outdoors/camping tent_6abce5ce-492a-5630-a30e-c47fb4045166.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('6abce5ce-492a-5630-a30e-c47fb4045166', 'pictographic-primitives/outdoors/camping tent_6abce5ce-492a-5630-a30e-c47fb4045166.svg'), ('e04ca869-614a-4a24-9bbc-53fa1cb01b84', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/tent_e04ca869-614a-4a24-9bbc-53fa1cb01b84.svg'))
PROFILE_SOURCE_KEYS = ('solo/camping-tent-outdoors',)
SOLO_SOURCE_ICON_IDS = ('camping-tent-outdoors',)
REFERENCE_EXPORT_SHA256 = '6236ef15cea4cf13ae53dd109bb450a0becfb9eea78bc74633e3f1275f571cdf'

class Drawing(Sub32):
    icon_id = 'camping-tent-outdoors-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'outdoors'
    categories = ('outdoors', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (2, 30), ((5, 16), (10, 2), (16, 2)))
        self.add_bezier('p1-r1-2', (16, 2), ((22, 2), (27, 16), (30, 30)))
        self.add_line('p1-r1-3', (30, 30), (22, 30))
        self.add_line('p1-r1-4', (22, 30), (10, 30))
        self.add_line('p1-r1-5', (10, 30), (2, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_bezier('p2-r1-1', (10, 30), ((11, 21), (13, 13), (16, 13)))
        self.add_bezier('p2-r1-2', (16, 13), ((19, 13), (21, 21), (22, 30)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.relate('connect', 'p1-r1-3', 'p2-r1-2')
        self.relate('connect', 'p1-r1-4', 'p2-r1-1')
        self.relate('connect', 'p1-r1-4', 'p2-r1-2')
        self.relate('connect', 'p1-r1-5', 'p2-r1-1')
