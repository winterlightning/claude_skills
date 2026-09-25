'Paper Money Bill.\n\nSymbol plan: Banknote with central seal. Corner diagonals omitted after their enclosed pockets failed the minimum-hole check.\nKeyshape: HRECT_M; authored on SOLO48, not scaled from source.\nLucide: banknote.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '27ee2524-58a6-4c71-b2f7-61ee5b81b03e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_01/accounting bills 1_27ee2524-58a6-4c71-b2f7-61ee5b81b03e.svg'
AUTHOR = 'gpt-6'

class BanknoteCircleCornerPanels(Solo48):
    icon_id = 'banknote-circle-corner-panels'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('banknote', 'circle', 'corner', 'panels')

    def build(self):
        # Banknote with central seal. Corner diagonals omitted after their enclosed pockets failed the minimum-hole check.
        axis_x = 24
        p_4_13 = (4, 13)
        p_4_35 = (4, 35)
        p_7_10 = (7, 10)
        p_7_38 = (7, 38)
        p_19_24 = (19, 24)
        p_29_24 = (2 * axis_x - p_19_24[0], p_19_24[1])
        p_41_10 = (2 * axis_x - p_7_10[0], p_7_10[1])
        p_41_38 = (2 * axis_x - p_7_38[0], p_7_38[1])
        p_44_13 = (2 * axis_x - p_4_13[0], p_4_13[1])
        p_44_35 = (2 * axis_x - p_4_35[0], p_4_35[1])
        self.add_line('frame-1', p_7_10, p_41_10)
        self.add_arc('frame-2', p_41_10, p_44_13, radius_x=3, radius_y=3, sweep=True)
        self.add_line('frame-3', p_44_13, p_44_35)
        self.add_arc('frame-4', p_44_35, p_41_38, radius_x=3, radius_y=3, sweep=True)
        self.add_line('frame-5', p_41_38, p_7_38)
        self.add_arc('frame-6', p_7_38, p_4_35, radius_x=3, radius_y=3, sweep=True)
        self.add_line('frame-7', p_4_35, p_4_13)
        self.add_arc('frame-8', p_4_13, p_7_10, radius_x=3, radius_y=3, sweep=True)
        self.add_contour('frame', 'frame-1', 'frame-2', 'frame-3', 'frame-4', 'frame-5', 'frame-6', 'frame-7', 'frame-8', closed=True)
        self.add_arc('seal-1', p_19_24, p_29_24, radius_x=5, radius_y=5, sweep=True)
        self.add_arc('seal-2', p_29_24, p_19_24, radius_x=5, radius_y=5, sweep=True)
        self.add_contour('seal', 'seal-1', 'seal-2', closed=True)
