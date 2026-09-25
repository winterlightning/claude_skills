'Professional Studio Spotlight.\n\nSymbol plan: Studio spotlight has a flared body with sufficient rear thickness and a three-legged tripod.\nKeyshape: VRECT_L; authored on SOLO48, not scaled from source.\nLucide: megaphone.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0f453147-194d-46ac-8c4d-5734b7d8d1e1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_25/light 2_0f453147-194d-46ac-8c4d-5734b7d8d1e1.svg'
AUTHOR = 'gpt-6'

class StudioSpotlight(Solo48):
    icon_id = 'studio-spotlight'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'Uncategorized'
    aliases = ()
    keywords = ('studio', 'spotlight')

    def build(self):
        # Studio spotlight has a flared body with sufficient rear thickness and a three-legged tripod.
        axis_x = 24
        p_8_10 = (8, 10)
        p_8_18 = (8, 18)
        p_12_44 = (12, 44)
        p_21_8 = (21, 8)
        p_24_20 = (24, 20)
        p_24_34 = (24, 34)
        p_24_44 = (24, 44)
        p_34_4 = (34, 4)
        p_34_24 = (34, 24)
        p_36_44 = (2 * axis_x - p_12_44[0], p_12_44[1])
        p_40_4 = (40, 4)
        p_40_8 = (40, 8)
        p_40_14 = (40, 14)
        p_40_20 = (40, 20)
        p_40_24 = (40, 24)
        self.add_line('lamp-1', p_8_10, p_21_8)
        self.add_line('lamp-2', p_21_8, p_34_4)
        self.add_bezier('lamp-3', p_34_4, (p_40_4, p_40_8, p_40_14))
        self.add_bezier('lamp-4', p_40_14, (p_40_20, p_40_24, p_34_24))
        self.add_line('lamp-5', p_34_24, p_24_20)
        self.add_line('lamp-6', p_24_20, p_8_18)
        self.add_line('lamp-7', p_8_18, p_8_10)
        self.add_contour('lamp', 'lamp-1', 'lamp-2', 'lamp-3', 'lamp-4', 'lamp-5', 'lamp-6', 'lamp-7', closed=True)
        self.add_line('stand-1', p_24_20, p_24_34)
        self.add_line('stand-2', p_24_34, p_12_44)
        self.add_contour('stand', 'stand-1', 'stand-2', closed=False)
        self.add_line('right-leg-1', p_24_34, p_36_44)
        self.add_contour('right-leg', 'right-leg-1', closed=False)
        self.add_line('center-leg-1', p_24_34, p_24_44)
        self.add_contour('center-leg', 'center-leg-1', closed=False)
        self.relate("connect", 'lamp', 'stand')
        self.relate("connect", 'stand', 'right-leg')
        self.relate("connect", 'stand', 'center-leg')
