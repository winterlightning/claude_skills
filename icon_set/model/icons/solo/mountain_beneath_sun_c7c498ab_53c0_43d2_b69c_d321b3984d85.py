'Mountain and Sun Landscape.\n\nSymbol plan: Broad mountain beneath upper-right sun and a detached ground line.\nKeyshape: SQUARE; authored on SOLO48, not scaled from source.\nLucide: mountain-snow.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c7c498ab-53c0-43d2-b69c-d321b3984d85'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_21/glen_c7c498ab-53c0-43d2-b69c-d321b3984d85.svg'
AUTHOR = 'gpt-6'

class MountainBeneathSun(Solo48):
    icon_id = 'mountain-beneath-sun'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/reference'
    aliases = ()
    keywords = ('mountain', 'beneath', 'sun')

    def build(self):
        # Broad mountain beneath upper-right sun and a detached ground line.
        axis_x = 24
        p_6_33 = (6, 33)
        p_6_42 = (6, 42)
        p_19_18 = (19, 18)
        p_30_12 = (30, 12)
        p_38_33 = (38, 33)
        p_42_12 = (42, 12)
        p_42_42 = (2 * axis_x - p_6_42[0], p_6_42[1])
        self.add_line('mountain-1', p_6_33, p_19_18)
        self.add_line('mountain-2', p_19_18, p_38_33)
        self.add_line('mountain-3', p_38_33, p_6_33)
        self.add_contour('mountain', 'mountain-1', 'mountain-2', 'mountain-3', closed=True)
        self.add_arc('sun-1', p_30_12, p_42_12, radius_x=6, radius_y=6, sweep=True)
        self.add_arc('sun-2', p_42_12, p_30_12, radius_x=6, radius_y=6, sweep=True)
        self.add_contour('sun', 'sun-1', 'sun-2', closed=True)
        self.add_line('ground-1', p_6_42, p_42_42)
        self.add_contour('ground', 'ground-1', closed=False)
