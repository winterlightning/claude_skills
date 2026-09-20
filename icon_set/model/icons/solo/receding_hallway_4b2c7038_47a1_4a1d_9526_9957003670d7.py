'Perspective Hallway Corridor.\n\nSymbol plan: Perspective hallway: open front frame, inset rear wall and two floor diagonals. Mirrored architectural construction.\nKeyshape: SQUARE; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4b2c7038-47a1-4a1d-9526-9957003670d7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_22/hallway_4b2c7038-47a1-4a1d-9526-9957003670d7.svg'
AUTHOR = 'gpt-6'

class RecedingHallway(Solo48):
    icon_id = 'receding-hallway'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/reference'
    aliases = ()
    keywords = ('receding', 'hallway')

    def build(self):
        # Perspective hallway: open front frame, inset rear wall and two floor diagonals. Mirrored architectural construction.
        axis_x = 24
        p_6_6 = (6, 6)
        p_6_42 = (6, 42)
        p_16_16 = (16, 16)
        p_16_32 = (16, 32)
        p_32_16 = (2 * axis_x - p_16_16[0], p_16_16[1])
        p_32_32 = (2 * axis_x - p_16_32[0], p_16_32[1])
        p_42_6 = (2 * axis_x - p_6_6[0], p_6_6[1])
        p_42_42 = (2 * axis_x - p_6_42[0], p_6_42[1])
        self.add_line('front-1', p_6_42, p_6_6)
        self.add_line('front-2', p_6_6, p_42_6)
        self.add_line('front-3', p_42_6, p_42_42)
        self.add_contour('front', 'front-1', 'front-2', 'front-3', closed=False)
        self.add_line('rear-1', p_16_16, p_32_16)
        self.add_line('rear-2', p_32_16, p_32_32)
        self.add_line('rear-3', p_32_32, p_16_32)
        self.add_line('rear-4', p_16_32, p_16_16)
        self.add_contour('rear', 'rear-1', 'rear-2', 'rear-3', 'rear-4', closed=True)
        self.add_line('floor-left-1', p_6_42, p_16_32)
        self.add_contour('floor-left', 'floor-left-1', closed=False)
        self.add_line('floor-right-1', p_42_42, p_32_32)
        self.add_contour('floor-right', 'floor-right-1', closed=False)
        self.relate("connect", 'floor-left', 'front')
        self.relate("connect", 'floor-left', 'rear')
        self.relate("connect", 'floor-right', 'front')
        self.relate("connect", 'floor-right', 'rear')
