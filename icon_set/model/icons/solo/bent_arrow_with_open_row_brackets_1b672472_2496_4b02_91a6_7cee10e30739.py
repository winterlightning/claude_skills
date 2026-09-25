'Insert Row With Right Arrow.\n\nSymbol plan: Original open row brackets and bent insertion arrow retained as a standalone layout diagram; do not invent missing cells or split incomplete enclosures.\nKeyshape: SQUARE; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1b672472-2496-4b02-91a6-7cee10e30739'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_23/insert row_1b672472-2496-4b02-91a6-7cee10e30739.svg'
AUTHOR = 'gpt-6'

class BentArrowWithOpenRowBrackets(Solo48):
    icon_id = 'bent-arrow-with-open-row-brackets'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('bent', 'arrow', 'with', 'open', 'row', 'brackets')

    def build(self):
        # Original open row brackets and bent insertion arrow retained as a standalone layout diagram; do not invent missing cells or split incomplete enclosures.
        axis_x = 24
        p_6_17 = (6, 17)
        p_6_31 = (6, 31)
        p_15_17 = (15, 17)
        p_15_31 = (15, 31)
        p_26_6 = (26, 6)
        p_26_24 = (26, 24)
        p_26_39 = (26, 39)
        p_26_42 = (26, 42)
        p_35_17 = (35, 17)
        p_35_31 = (35, 31)
        p_42_24 = (42, 24)
        p_42_39 = (42, 39)
        self.add_line('left-bracket-1', p_6_17, p_15_17)
        self.add_line('left-bracket-2', p_15_17, p_15_31)
        self.add_line('left-bracket-3', p_15_31, p_6_31)
        self.add_contour('left-bracket', 'left-bracket-1', 'left-bracket-2', 'left-bracket-3', closed=False)
        self.add_line('arrow-1', p_26_6, p_26_24)
        self.add_line('arrow-2', p_26_24, p_42_24)
        self.add_contour('arrow', 'arrow-1', 'arrow-2', closed=False)
        self.add_line('arrowhead-1', p_35_17, p_42_24)
        self.add_line('arrowhead-2', p_42_24, p_35_31)
        self.add_contour('arrowhead', 'arrowhead-1', 'arrowhead-2', closed=False)
        self.relate("connect", 'arrow', 'arrowhead')
        self.add_line('bottom-bracket-1', p_26_42, p_26_39)
        self.add_line('bottom-bracket-2', p_26_39, p_42_39)
        self.add_contour('bottom-bracket', 'bottom-bracket-1', 'bottom-bracket-2', closed=False)
