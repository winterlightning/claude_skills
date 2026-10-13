"""Independent 32px profile of person-kicking-ball.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '33e0f679-82d2-4c2a-b9d1-af30c1a9b528'
SOURCE_PATH = 'pictographic-primitives/symbol/person playing ball_33e0f679-82d2-4c2a-b9d1-af30c1a9b528.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('33e0f679-82d2-4c2a-b9d1-af30c1a9b528', 'pictographic-primitives/symbol/person playing ball_33e0f679-82d2-4c2a-b9d1-af30c1a9b528.svg'),)
PROFILE_SOURCE_KEYS = ('solo/person-kicking-ball',)
SOLO_SOURCE_ICON_IDS = ('person-kicking-ball',)
REFERENCE_EXPORT_SHA256 = 'bda8bb7e341247519c7d6c30c44997e357ac735977992e9a1fb35c58c4c685e4'

class Drawing(Sub32):
    icon_id = 'person-kicking-ball-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Person kicking a ball: head dot, leaning torso, arms out, standing leg and kicking leg, ball dot.
        self.add_arc('head-1', (18, 4), (22, 4), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('head-2', (22, 4), (18, 4), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('head', 'head-1', 'head-2', closed=True)
        self.add_line('torso', (16, 14), (13, 21))
        self.add_line('arm-back', (16, 14), (2, 10))
        self.add_line('arm-front', (16, 14), (28, 15))
        self.add_line('leg-stand', (13, 21), (6, 30))
        self.add_line('leg-kick', (13, 21), (19, 23))
        self.add_arc('ball-1', (26, 28), (30, 28), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('ball-2', (30, 28), (26, 28), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('ball', 'ball-1', 'ball-2', closed=True)
        self.relate('connect', 'torso', 'arm-back')
        self.relate('connect', 'torso', 'arm-front')
        self.relate('connect', 'arm-back', 'arm-front')
        self.relate('connect', 'torso', 'leg-stand')
        self.relate('connect', 'torso', 'leg-kick')
        self.relate('connect', 'leg-stand', 'leg-kick')
