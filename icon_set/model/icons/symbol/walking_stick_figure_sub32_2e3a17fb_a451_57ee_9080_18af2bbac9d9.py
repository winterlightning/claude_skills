"""Independent 32px profile of walking-stick-figure.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '2e3a17fb-a451-57ee-9080-18af2bbac9d9'
SOURCE_PATH = 'pictographic-primitives/wayfinding/walking_2e3a17fb-a451-57ee-9080-18af2bbac9d9.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('2e3a17fb-a451-57ee-9080-18af2bbac9d9', 'pictographic-primitives/wayfinding/walking_2e3a17fb-a451-57ee-9080-18af2bbac9d9.svg'), ('7ce62344-aeae-474c-9800-f2104921b059', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/wayfinding/walking_7ce62344-aeae-474c-9800-f2104921b059.svg'))
PROFILE_SOURCE_KEYS = ('solo/walking-stick-figure',)
SOLO_SOURCE_ICON_IDS = ('walking-stick-figure',)
REFERENCE_EXPORT_SHA256 = '2c5a88771118fbec864ddc22b0ec466999bf304605e281927a6932fa6de9a7c0'

class Drawing(Sub32):
    icon_id = 'walking-stick-figure-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Walking figure: head dot, torso, arms swinging, legs in stride with the front foot flat.
        self.add_arc('head-1', (15, 4), (19, 4), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('head-2', (19, 4), (15, 4), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('head', 'head-1', 'head-2', closed=True)
        self.add_line('torso', (16, 14), (14, 22))
        self.add_line('arm-back', (16, 14), (6, 16))
        self.add_line('arm-front', (16, 14), (28, 18))
        self.add_line('leg-back', (14, 22), (4, 30))
        self.add_polyline('leg-front', (14, 22), (23, 30), (27, 30))
        self.relate('connect', 'torso', 'arm-back')
        self.relate('connect', 'torso', 'arm-front')
        self.relate('connect', 'arm-back', 'arm-front')
        self.relate('connect', 'torso', 'leg-back')
        self.relate('connect', 'torso', 'leg-front')
        self.relate('connect', 'leg-back', 'leg-front')
