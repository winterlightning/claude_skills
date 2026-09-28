'Minecraft Creeper Face.\n\nSymbol plan: Creeper face with two square eyes and a blocky notched mouth. Filled tiny eyes become short thick marks.\nKeyshape: SQUARE; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2c8e85ee-be73-4c81-a956-f44ba809e1eb'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_39/video game logo creeper_2c8e85ee-be73-4c81-a956-f44ba809e1eb.svg'
AUTHOR = 'gpt-6'

class CreeperFace(Solo48):
    icon_id = 'creeper-face'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('creeper', 'face')

    def build(self):
        # Creeper face with two square eyes and a blocky notched mouth. Filled tiny eyes become short thick marks.
        axis_x = 24
        p_6_8 = (6, 8)
        p_6_40 = (6, 40)
        p_8_6 = (8, 6)
        p_8_42 = (8, 42)
        p_16_17 = (16, 17)
        p_17_26 = (17, 26)
        p_17_33 = (17, 33)
        p_18_17 = (18, 17)
        p_24_23 = (24, 23)
        p_24_26 = (24, 26)
        p_30_17 = (2 * axis_x - p_18_17[0], p_18_17[1])
        p_31_26 = (2 * axis_x - p_17_26[0], p_17_26[1])
        p_31_33 = (2 * axis_x - p_17_33[0], p_17_33[1])
        p_32_17 = (2 * axis_x - p_16_17[0], p_16_17[1])
        p_40_6 = (2 * axis_x - p_8_6[0], p_8_6[1])
        p_40_42 = (2 * axis_x - p_8_42[0], p_8_42[1])
        p_42_8 = (2 * axis_x - p_6_8[0], p_6_8[1])
        p_42_40 = (2 * axis_x - p_6_40[0], p_6_40[1])
        self.add_line('head-1', p_8_6, p_40_6)
        self.add_arc('head-2', p_40_6, p_42_8, radius_x=2, radius_y=2, sweep=True)
        self.add_line('head-3', p_42_8, p_42_40)
        self.add_arc('head-4', p_42_40, p_40_42, radius_x=2, radius_y=2, sweep=True)
        self.add_line('head-5', p_40_42, p_8_42)
        self.add_arc('head-6', p_8_42, p_6_40, radius_x=2, radius_y=2, sweep=True)
        self.add_line('head-7', p_6_40, p_6_8)
        self.add_arc('head-8', p_6_8, p_8_6, radius_x=2, radius_y=2, sweep=True)
        self.add_contour('head', 'head-1', 'head-2', 'head-3', 'head-4', 'head-5', 'head-6', 'head-7', 'head-8', closed=True)
        self.add_line('eye-left-1', p_16_17, p_18_17)
        self.add_contour('eye-left', 'eye-left-1', closed=False)
        self.add_line('eye-right-1', p_30_17, p_32_17)
        self.add_contour('eye-right', 'eye-right-1', closed=False)
        self.add_line('mouth-1', p_17_33, p_17_26)
        self.add_line('mouth-2', p_17_26, p_31_26)
        self.add_line('mouth-3', p_31_26, p_31_33)
        self.add_contour('mouth', 'mouth-1', 'mouth-2', 'mouth-3', closed=False)
        self.add_line('nose-1', p_24_23, p_24_26)
        self.add_contour('nose', 'nose-1', closed=False)
        self.relate("connect", 'nose', 'mouth')
