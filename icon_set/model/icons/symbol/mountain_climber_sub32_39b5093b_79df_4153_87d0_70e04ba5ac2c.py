"""Independent 32px profile of mountain-climber.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '39b5093b-79df-4153-87d0-70e04ba5ac2c'
SOURCE_PATH = 'pictographic-primitives/sports/climbing mountain_39b5093b-79df-4153-87d0-70e04ba5ac2c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('39b5093b-79df-4153-87d0-70e04ba5ac2c', 'pictographic-primitives/sports/climbing mountain_39b5093b-79df-4153-87d0-70e04ba5ac2c.svg'), ('c63b6ce9-917b-4f7e-a312-f05bbdf42679', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/climb_c63b6ce9-917b-4f7e-a312-f05bbdf42679.svg'))
PROFILE_SOURCE_KEYS = ('solo/mountain-climber',)
SOLO_SOURCE_ICON_IDS = ('mountain-climber',)
REFERENCE_EXPORT_SHA256 = 'a1a189c8ba0c55beae8fee4f4d551ba5c6848be6aa60a0a307e33cc65a3aaa49'

class Drawing(Sub32):
    icon_id = 'mountain-climber-sub32'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'sports'
    categories = ('sports', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Mountain climber: head dot, arm reaching up to the wall, the other arm out, legs apart.
        self.add_arc('head-1', (10, 4), (14, 4), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('head-2', (14, 4), (10, 4), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('head', 'head-1', 'head-2', closed=True)
        self.add_line('torso', (12, 15), (12, 23))
        self.add_line('arm-up', (12, 15), (26, 10))
        self.add_line('arm-out', (12, 15), (6, 19))
        self.add_line('leg-l', (12, 23), (6, 30))
        self.add_line('leg-r', (12, 23), (18, 30))
        self.add_line('wall', (26, 2), (26, 30))
        self.relate('connect', 'torso', 'arm-up')
        self.relate('connect', 'torso', 'arm-out')
        self.relate('connect', 'arm-up', 'arm-out')
        self.relate('connect', 'arm-up', 'wall')
        self.relate('connect', 'torso', 'leg-l')
        self.relate('connect', 'torso', 'leg-r')
        self.relate('connect', 'leg-l', 'leg-r')
