"""Independent 32px profile of downhill-skier.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'c92285fd-d928-4a7c-a2c3-2e02288f502f'
SOURCE_PATH = 'pictographic-primitives/sports/skiing slide down_c92285fd-d928-4a7c-a2c3-2e02288f502f.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('c92285fd-d928-4a7c-a2c3-2e02288f502f', 'pictographic-primitives/sports/skiing slide down_c92285fd-d928-4a7c-a2c3-2e02288f502f.svg'), ('5a60755a-84e0-4d24-9372-1ab838965a3f', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/snowboard_5a60755a-84e0-4d24-9372-1ab838965a3f.svg'))
PROFILE_SOURCE_KEYS = ('solo/downhill-skier',)
SOLO_SOURCE_ICON_IDS = ('downhill-skier',)
REFERENCE_EXPORT_SHA256 = '91c9cdc3c3597fb096af5663cdaecf19d1b7363da504d1bd92ae78b271305a81'

class Drawing(Sub32):
    icon_id = 'downhill-skier-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'sports'
    categories = ('sports', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Downhill skier: head dot, torso leaning forward, arm back, legs bent onto the slanted ski.
        self.add_arc('head-1', (26, 4), (30, 4), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('head-2', (30, 4), (26, 4), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('head', 'head-1', 'head-2', closed=True)
        self.add_line('ski', (2, 22), (30, 30))
        self.add_line('torso', (14, 16), (20, 10))
        self.add_line('arm', (20, 10), (12, 8))
        self.add_polyline('leg-back', (14, 16), (10, 21), (9, 24))
        self.relate('connect', 'torso', 'arm')
        self.relate('connect', 'torso', 'leg-back')
        self.relate('connect', 'leg-back', 'ski')
        self.relate('connect', 'leg-back', 'torso')
