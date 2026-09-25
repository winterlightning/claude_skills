'Navigation Location Pointer Arrow.\n\nSymbol plan: Navigation arrow with pointed upper-right tip and deeply indented rear arms.\nKeyshape: SQUARE; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0546719f-bfc2-42e3-90df-e61e439689be'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_25/location arrow_0546719f-bfc2-42e3-90df-e61e439689be.svg'
AUTHOR = 'gpt-6'

class ArrowLocation(Solo48):
    icon_id = 'arrow-location'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('arrow', 'location')

    def build(self):
        # Navigation arrow with pointed upper-right tip and deeply indented rear arms.
        axis_x = 24
        p_6_24 = (6, 24)
        p_22_27 = (22, 27)
        p_24_42 = (24, 42)
        p_42_6 = (42, 6)
        self.add_line('arrow-1', p_6_24, p_42_6)
        self.add_line('arrow-2', p_42_6, p_24_42)
        self.add_line('arrow-3', p_24_42, p_22_27)
        self.add_line('arrow-4', p_22_27, p_6_24)
        self.add_contour('arrow', 'arrow-1', 'arrow-2', 'arrow-3', 'arrow-4', closed=True)
