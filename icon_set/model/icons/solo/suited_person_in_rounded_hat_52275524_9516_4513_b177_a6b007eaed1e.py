'Person wearing suit and hat.\n\nSymbol plan: Rounded-hat formal portrait with a single tie stroke. Circular lower jaw and shoulders touch; omit crowded lapels.\nKeyshape: VRECT_L; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '52275524-9516-4513-b177-a6b007eaed1e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_21/governor_52275524-9516-4513-b177-a6b007eaed1e.svg'
AUTHOR = 'gpt-6'

class SuitedPersonInRoundedHat(Solo48):
    icon_id = 'suited-person-in-rounded-hat'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('suited', 'person', 'in', 'rounded', 'hat')

    def build(self):
        # Rounded-hat formal portrait with a single tie stroke. Circular lower jaw and shoulders touch; omit crowded lapels.
        axis_x = 24
        p_8_44 = (8, 44)
        p_10_8 = (10, 8)
        p_10_16 = (10, 16)
        p_10_20 = (10, 20)
        p_14_20 = (14, 20)
        p_16_4 = (16, 4)
        p_24_4 = (24, 4)
        p_24_34 = (24, 34)
        p_24_42 = (24, 42)
        p_32_4 = (2 * axis_x - p_16_4[0], p_16_4[1])
        p_34_20 = (2 * axis_x - p_14_20[0], p_14_20[1])
        p_38_8 = (2 * axis_x - p_10_8[0], p_10_8[1])
        p_38_16 = (2 * axis_x - p_10_16[0], p_10_16[1])
        p_38_20 = (2 * axis_x - p_10_20[0], p_10_20[1])
        p_40_44 = (2 * axis_x - p_8_44[0], p_8_44[1])
        self.add_arc('head-1', p_14_20, p_34_20, radius_x=10, radius_y=10, sweep=False)
        self.add_contour('head', 'head-1', closed=False)
        self.add_arc('body-1', p_8_44, p_24_34, radius_x=16, radius_y=10, sweep=True)
        self.add_arc('body-2', p_24_34, p_40_44, radius_x=16, radius_y=10, sweep=True)
        self.add_contour('body', 'body-1', 'body-2', closed=False)
        self.relate("connect", 'head', 'body')
        self.add_line('hat-1', p_10_20, p_10_16)
        self.add_bezier('hat-2', p_10_16, (p_10_8, p_16_4, p_24_4))
        self.add_bezier('hat-3', p_24_4, (p_32_4, p_38_8, p_38_16))
        self.add_line('hat-4', p_38_16, p_38_20)
        self.add_line('hat-5', p_38_20, p_34_20)
        self.add_line('hat-6', p_34_20, p_14_20)
        self.add_line('hat-7', p_14_20, p_10_20)
        self.add_contour('hat', 'hat-1', 'hat-2', 'hat-3', 'hat-4', 'hat-5', 'hat-6', 'hat-7', closed=True)
        self.relate("connect", 'head', 'hat')
        self.add_line('tie-1', p_24_34, p_24_42)
        self.add_contour('tie', 'tie-1', closed=False)
        self.relate("connect", 'tie', 'body')
