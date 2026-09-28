'Mesh Grid Pattern.\n\nSymbol plan: Three vertical and three horizontal strands in a shared evenly spaced open grid; no border.\nKeyshape: SQUARE; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0c6bb5c3-4099-45c0-a5cc-c11211751d4d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_17/fabric_0c6bb5c3-4099-45c0-a5cc-c11211751d4d.svg'
AUTHOR = 'gpt-6'

class OrthogonalMeshGrid(Solo48):
    icon_id = 'orthogonal-mesh-grid'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('orthogonal', 'mesh', 'grid')

    def build(self):
        # Three vertical and three horizontal strands in a shared evenly spaced open grid; no border.
        axis_x = 24
        p_6_14 = (6, 14)
        p_6_24 = (6, 24)
        p_6_34 = (6, 34)
        p_14_6 = (14, 6)
        p_14_42 = (14, 42)
        p_24_6 = (24, 6)
        p_24_42 = (24, 42)
        p_34_6 = (2 * axis_x - p_14_6[0], p_14_6[1])
        p_34_42 = (2 * axis_x - p_14_42[0], p_14_42[1])
        p_42_14 = (2 * axis_x - p_6_14[0], p_6_14[1])
        p_42_24 = (2 * axis_x - p_6_24[0], p_6_24[1])
        p_42_34 = (2 * axis_x - p_6_34[0], p_6_34[1])
        self.add_line('vertical-14-1', p_14_6, p_14_42)
        self.add_contour('vertical-14', 'vertical-14-1', closed=False)
        self.add_line('vertical-24-1', p_24_6, p_24_42)
        self.add_contour('vertical-24', 'vertical-24-1', closed=False)
        self.add_line('vertical-34-1', p_34_6, p_34_42)
        self.add_contour('vertical-34', 'vertical-34-1', closed=False)
        self.add_line('horizontal-14-1', p_6_14, p_42_14)
        self.add_contour('horizontal-14', 'horizontal-14-1', closed=False)
        self.relate("connect", 'vertical-14', 'horizontal-14')
        self.relate("connect", 'vertical-24', 'horizontal-14')
        self.relate("connect", 'vertical-34', 'horizontal-14')
        self.add_line('horizontal-24-1', p_6_24, p_42_24)
        self.add_contour('horizontal-24', 'horizontal-24-1', closed=False)
        self.relate("connect", 'vertical-14', 'horizontal-24')
        self.relate("connect", 'vertical-24', 'horizontal-24')
        self.relate("connect", 'vertical-34', 'horizontal-24')
        self.add_line('horizontal-34-1', p_6_34, p_42_34)
        self.add_contour('horizontal-34', 'horizontal-34-1', closed=False)
        self.relate("connect", 'vertical-14', 'horizontal-34')
        self.relate("connect", 'vertical-24', 'horizontal-34')
        self.relate("connect", 'vertical-34', 'horizontal-34')
