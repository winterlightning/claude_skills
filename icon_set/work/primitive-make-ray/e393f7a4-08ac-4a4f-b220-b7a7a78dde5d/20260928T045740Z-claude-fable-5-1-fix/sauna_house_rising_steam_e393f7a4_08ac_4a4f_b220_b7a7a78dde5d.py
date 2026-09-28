"""A sauna house with a peaked roof and an arched door, with three wisps of steam rising above it.

Plan: VRECT_L (8,4)-(40,44). Three S-shaped steam wisps (in-phase cubics, 10 apart) fill y 4-12. The house below: a roof from the eaves (8,31) and (40,31) to the peak (24,21), walls down to the floor at y=44, and an arched door 8 wide (r4 top at 35) in the middle of the front wall.
Review of the rejected drawing: the house was a squat 44-wide box with a notch for a door and the steam was three tight curls, so it read as a barn with commas over it; the original is a tall house with a proper door and tall wavy steam.
Omissions: none beyond the reduction to single strokes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'e393f7a4-08ac-4a4f-b220-b7a7a78dde5d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__sauna-house-rising-steam/20260928T042731Z-thuan-mac-1/reference/sauna heat_e393f7a4-08ac-4a4f-b220-b7a7a78dde5d.svg'
AUTHOR = 'thuan-mac-1/claude-fable-5-1'


class SaunaHouseRisingSteam(Solo48):
    icon_id = 'sauna-house-rising-steam'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'spas'
    categories = ('primitives', 'spas')
    aliases = ('sauna-heat', 'sauna-cabin')
    keywords = ('sauna', 'heat', 'steam', 'house', 'spa', 'cabin')

    def build(self) -> None:
        for x in (14, 24, 34):
            self.add_bezier(f'steam-{x}', (x, 4), ((x + 3, 6), (x - 3, 10), (x, 12)))
        # house: roof, walls and floor as one closed loop split at the door feet
        self.add_line('roof-left', (8, 31), (24, 21))
        self.add_line('roof-right', (24, 21), (40, 31))
        self.add_line('wall-right', (40, 31), (40, 44))
        self.add_line('floor-right', (40, 44), (28, 44))
        self.add_line('floor-door', (28, 44), (20, 44))
        self.add_line('floor-left', (20, 44), (8, 44))
        self.add_line('wall-left', (8, 44), (8, 31))
        self.add_contour('house', 'roof-left', 'roof-right', 'wall-right', 'floor-right',
                         'floor-door', 'floor-left', 'wall-left', closed=True)
        self.add_line('door-left', (20, 44), (20, 39))
        self.add_arc('door-top', (20, 39), (28, 39), radius_x=4, sweep=True)
        self.add_line('door-right', (28, 39), (28, 44))
        self.add_contour('door', 'door-left', 'door-top', 'door-right')
        self.relate('connect', 'door', 'house')
