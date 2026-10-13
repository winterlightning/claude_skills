"""Independent 32px profile of snowboarding.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '6bd421c1-b45f-42f7-bc55-f1a7d00409df'
SOURCE_PATH = 'pictographic-primitives/symbol/skiing_6bd421c1-b45f-42f7-bc55-f1a7d00409df.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('6bd421c1-b45f-42f7-bc55-f1a7d00409df', 'pictographic-primitives/symbol/skiing_6bd421c1-b45f-42f7-bc55-f1a7d00409df.svg'),)
PROFILE_SOURCE_KEYS = ('solo/snowboarding',)
SOLO_SOURCE_ICON_IDS = ('snowboarding',)
REFERENCE_EXPORT_SHA256 = '98706e3f5edaf11862d3eeafe16e4c01339420b23272ca9d1902f55181afb345'

class Drawing(Sub32):
    icon_id = 'snowboarding-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Snowboarder: head dot, torso leaning forward, arms out to both sides, legs on the slanted board.
        self.add_arc('head-1', (26, 4), (30, 4), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('head-2', (30, 4), (26, 4), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('head', 'head-1', 'head-2', closed=True)
        self.add_line('board', (2, 22), (30, 30))
        self.add_line('torso', (14, 16), (20, 10))
        self.add_line('arm-back', (20, 10), (12, 8))
        self.add_line('arm-front', (20, 10), (25, 17))
        self.add_polyline('leg-back', (14, 16), (10, 21), (9, 24))
        self.relate('connect', 'torso', 'arm-back')
        self.relate('connect', 'torso', 'arm-front')
        self.relate('connect', 'arm-back', 'arm-front')
        self.relate('connect', 'torso', 'leg-back')
        self.relate('connect', 'leg-back', 'board')
        self.relate('connect', 'leg-back', 'torso')
