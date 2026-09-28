'Musical Saxophone Instrument.\n\nSymbol plan: Saxophone with curved bottom, upright body, mouthpiece and upward bell; omit tiny key ticks.\nKeyshape: VRECT_L; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5b1bdd1e-b98f-4cd3-8970-9fc4e618a5e9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_23/instrument saxophone_5b1bdd1e-b98f-4cd3-8970-9fc4e618a5e9.svg'
AUTHOR = 'gpt-6'

class CurvedSaxophone(Solo48):
    icon_id = 'curved-saxophone'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/reference'
    aliases = ()
    keywords = ('curved', 'saxophone')

    def build(self):
        # Saxophone with curved bottom, upright body, mouthpiece and upward bell; omit tiny key ticks.
        axis_x = 24
        p_8_4 = (8, 4)
        p_12_12 = (12, 12)
        p_12_30 = (12, 30)
        p_12_38 = (12, 38)
        p_16_44 = (16, 44)
        p_18_4 = (18, 4)
        p_22_10 = (22, 10)
        p_22_18 = (22, 18)
        p_22_30 = (22, 30)
        p_26_44 = (26, 44)
        p_32_16 = (32, 16)
        p_32_30 = (32, 30)
        p_34_44 = (34, 44)
        p_40_25 = (40, 25)
        p_40_30 = (40, 30)
        p_40_39 = (40, 39)
        self.add_bezier('sax-1', p_8_4, (p_18_4, p_22_10, p_22_18))
        self.add_line('sax-2', p_22_18, p_22_30)
        self.add_arc('sax-3', p_22_30, p_32_30, radius_x=5, radius_y=5, sweep=False)
        self.add_line('sax-4', p_32_30, p_32_16)
        self.add_line('sax-5', p_32_16, p_40_25)
        self.add_line('sax-6', p_40_25, p_40_30)
        self.add_bezier('sax-7', p_40_30, (p_40_39, p_34_44, p_26_44))
        self.add_bezier('sax-8', p_26_44, (p_16_44, p_12_38, p_12_30))
        self.add_line('sax-9', p_12_30, p_12_12)
        self.add_contour('sax', 'sax-1', 'sax-2', 'sax-3', 'sax-4', 'sax-5', 'sax-6', 'sax-7', 'sax-8', 'sax-9', closed=False)
