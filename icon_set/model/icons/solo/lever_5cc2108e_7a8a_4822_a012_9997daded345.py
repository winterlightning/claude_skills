'Mechanical Control Lever.\n\nSymbol plan: Lever with circular grip and baseline at pivot.\nKeyshape: SQUARE; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5cc2108e-7a8a-4822-a012-9997daded345'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_25/lever_5cc2108e-7a8a-4822-a012-9997daded345.svg'
AUTHOR = 'gpt-6'

class Lever(Solo48):
    icon_id = 'lever'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('lever',)

    def build(self):
        # Lever with circular grip and baseline at pivot.
        axis_x = 24
        p_6_42 = (6, 42)
        p_8_42 = (8, 42)
        p_30_12 = (30, 12)
        p_32_16 = (32, 16)
        p_42_12 = (42, 12)
        p_42_42 = (2 * axis_x - p_6_42[0], p_6_42[1])
        self.add_line('base-1', p_6_42, p_42_42)
        self.add_contour('base', 'base-1', closed=False)
        self.add_line('lever-1', p_8_42, p_32_16)
        self.add_contour('lever', 'lever-1', closed=False)
        self.relate("connect", 'base', 'lever')
        self.add_arc('knob-1', p_30_12, p_42_12, radius_x=6, radius_y=6, sweep=True)
        self.add_arc('knob-2', p_42_12, p_30_12, radius_x=6, radius_y=6, sweep=True)
        self.add_contour('knob', 'knob-1', 'knob-2', closed=True)
        self.relate("connect", 'lever', 'knob')
