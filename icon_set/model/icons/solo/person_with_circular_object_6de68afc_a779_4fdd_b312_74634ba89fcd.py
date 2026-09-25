'Person with small circular object.\n\nSymbol plan: Bust with a neutral round object at lower right. Object has no identifying mark; preserve the source ambiguity in the report.\nKeyshape: VRECT_L; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6de68afc-a779-4fdd-b312-74634ba89fcd'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_19/forager_6de68afc-a779-4fdd-b312-74634ba89fcd.svg'
AUTHOR = 'gpt-6'

class PersonWithCircularObject(Solo48):
    icon_id = 'person-with-circular-object'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('person', 'with', 'circular', 'object')

    def build(self):
        # Bust with a neutral round object at lower right. Object has no identifying mark; preserve the source ambiguity in the report.
        axis_x = 24
        p_8_38 = (8, 38)
        p_8_44 = (8, 44)
        p_16_12 = (16, 12)
        p_24_24 = (24, 24)
        p_28_38 = (28, 38)
        p_32_12 = (2 * axis_x - p_16_12[0], p_16_12[1])
        p_40_38 = (2 * axis_x - p_8_38[0], p_8_38[1])
        self.add_arc('head-1', p_16_12, p_32_12, radius_x=8, radius_y=8, sweep=True)
        self.add_arc('head-2', p_32_12, p_16_12, radius_x=8, radius_y=8, sweep=True)
        self.add_contour('head', 'head-1', 'head-2', closed=True)
        self.add_line('body-1', p_8_44, p_8_38)
        self.add_arc('body-2', p_8_38, p_24_24, radius_x=16, radius_y=14, sweep=True)
        self.add_contour('body', 'body-1', 'body-2', closed=False)
        self.relate("connect", 'head', 'body')
        self.add_arc('object-1', p_28_38, p_40_38, radius_x=6, radius_y=6, sweep=True)
        self.add_arc('object-2', p_40_38, p_28_38, radius_x=6, radius_y=6, sweep=True)
        self.add_contour('object', 'object-1', 'object-2', closed=True)
