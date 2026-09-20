'Kettle Drum with Sticks.\n\nSymbol plan: Bowl drum with three splayed legs and paired mallets; simplify elliptical head to straight rim for clear bowl interior.\nKeyshape: HRECT_L; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '774c5880-ea63-49fa-8f40-de081565a574'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_24/kettledrum_774c5880-ea63-49fa-8f40-de081565a574.svg'
AUTHOR = 'gpt-6'

class KettledrumWithMallets(Solo48):
    icon_id = 'kettledrum-with-mallets'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/reference'
    aliases = ()
    keywords = ('kettledrum', 'with', 'mallets')

    def build(self):
        # Bowl drum with three splayed legs and paired mallets; simplify elliptical head to straight rim for clear bowl interior.
        axis_x = 24
        p_4_8 = (4, 8)
        p_6_20 = (6, 20)
        p_6_30 = (6, 30)
        p_10_40 = (10, 40)
        p_13_8 = (13, 8)
        p_13_10 = (13, 10)
        p_13_34 = (13, 34)
        p_14_32 = (14, 32)
        p_17_10 = (17, 10)
        p_24_34 = (24, 34)
        p_24_40 = (24, 40)
        p_31_10 = (2 * axis_x - p_17_10[0], p_17_10[1])
        p_34_32 = (2 * axis_x - p_14_32[0], p_14_32[1])
        p_35_8 = (2 * axis_x - p_13_8[0], p_13_8[1])
        p_35_10 = (2 * axis_x - p_13_10[0], p_13_10[1])
        p_35_34 = (2 * axis_x - p_13_34[0], p_13_34[1])
        p_38_40 = (2 * axis_x - p_10_40[0], p_10_40[1])
        p_42_20 = (2 * axis_x - p_6_20[0], p_6_20[1])
        p_42_30 = (2 * axis_x - p_6_30[0], p_6_30[1])
        p_44_8 = (2 * axis_x - p_4_8[0], p_4_8[1])
        self.add_line('drum-1', p_6_20, p_42_20)
        self.add_bezier('drum-2', p_42_20, (p_42_30, p_35_34, p_24_34))
        self.add_bezier('drum-3', p_24_34, (p_13_34, p_6_30, p_6_20))
        self.add_contour('drum', 'drum-1', 'drum-2', 'drum-3', closed=True)
        self.add_line('left-leg-1', p_14_32, p_10_40)
        self.add_contour('left-leg', 'left-leg-1', closed=False)
        self.relate("connect", 'left-leg', 'drum')
        self.add_line('middle-leg-1', p_24_34, p_24_40)
        self.add_contour('middle-leg', 'middle-leg-1', closed=False)
        self.relate("connect", 'middle-leg', 'drum')
        self.add_line('right-leg-1', p_34_32, p_38_40)
        self.add_contour('right-leg', 'right-leg-1', closed=False)
        self.relate("connect", 'right-leg', 'drum')
        self.add_arc('mallet-left-1', p_13_10, p_17_10, radius_x=2, radius_y=2, sweep=True)
        self.add_arc('mallet-left-2', p_17_10, p_13_10, radius_x=2, radius_y=2, sweep=True)
        self.add_contour('mallet-left', 'mallet-left-1', 'mallet-left-2', closed=True)
        self.add_line('handle-left-1', p_13_8, p_4_8)
        self.add_contour('handle-left', 'handle-left-1', closed=False)
        self.relate("connect", 'mallet-left', 'handle-left')
        self.add_arc('mallet-right-1', p_31_10, p_35_10, radius_x=2, radius_y=2, sweep=True)
        self.add_arc('mallet-right-2', p_35_10, p_31_10, radius_x=2, radius_y=2, sweep=True)
        self.add_contour('mallet-right', 'mallet-right-1', 'mallet-right-2', closed=True)
        self.add_line('handle-right-1', p_35_8, p_44_8)
        self.add_contour('handle-right', 'handle-right-1', closed=False)
        self.relate("connect", 'mallet-right', 'handle-right')
