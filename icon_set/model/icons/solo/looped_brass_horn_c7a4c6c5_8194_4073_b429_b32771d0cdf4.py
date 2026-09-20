'Musical Brass Horn.\n\nSymbol plan: Looped brass horn with broad flared bell and left mouthpiece. Simplify doubled tubing to one coherent curved stroke.\nKeyshape: HRECT_L; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c7a4c6c5-8194-4073-b429-b32771d0cdf4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_19/flugelhorn_c7a4c6c5-8194-4073-b429-b32771d0cdf4.svg'
AUTHOR = 'gpt-6'

class LoopedBrassHorn(Solo48):
    icon_id = 'looped-brass-horn'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/reference'
    aliases = ()
    keywords = ('looped', 'brass', 'horn')

    def build(self):
        # Looped brass horn with broad flared bell and left mouthpiece. Simplify doubled tubing to one coherent curved stroke.
        axis_x = 24
        p_4_20 = (4, 20)
        p_12_29 = (12, 29)
        p_13_40 = (13, 40)
        p_19_20 = (19, 20)
        p_22_29 = (22, 29)
        p_22_40 = (22, 40)
        p_29_40 = (29, 40)
        p_30_29 = (30, 29)
        p_32_20 = (32, 20)
        p_33_33 = (33, 33)
        p_33_37 = (33, 37)
        p_35_26 = (35, 26)
        p_36_13 = (36, 13)
        p_40_8 = (40, 8)
        p_40_36 = (40, 36)
        p_44_8 = (44, 8)
        p_44_36 = (44, 36)
        self.add_line('horn-1', p_4_20, p_19_20)
        self.add_bezier('horn-2', p_19_20, (p_32_20, p_36_13, p_40_8))
        self.add_line('horn-3', p_40_8, p_44_8)
        self.add_line('horn-4', p_44_8, p_44_36)
        self.add_line('horn-5', p_44_36, p_40_36)
        self.add_bezier('horn-6', p_40_36, (p_35_26, p_30_29, p_22_29))
        self.add_bezier('horn-7', p_22_29, (p_12_29, p_13_40, p_22_40))
        self.add_bezier('horn-8', p_22_40, (p_29_40, p_33_37, p_33_33))
        self.add_contour('horn', 'horn-1', 'horn-2', 'horn-3', 'horn-4', 'horn-5', 'horn-6', 'horn-7', 'horn-8', closed=False)
