'Office Fax Machine.\n\nSymbol plan: Fax machine with top and front sheets. Front body wall ends at sheet edges, so paper occludes the housing rather than adding a crossing line. Small controls omitted.\nKeyshape: SQUARE; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '81ffb76f-c36f-43c6-af40-2cb0ed42411a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_18/fax_81ffb76f-c36f-43c6-af40-2cb0ed42411a.svg'
AUTHOR = 'gpt-6'

class FaxMachineWithTwoSheets(Solo48):
    icon_id = 'fax-machine-with-two-sheets'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('fax', 'machine', 'with', 'two', 'sheets')

    def build(self):
        # Fax machine with top and front sheets. Front body wall ends at sheet edges, so paper occludes the housing rather than adding a crossing line. Small controls omitted.
        axis_x = 24
        p_6_20 = (6, 20)
        p_6_30 = (6, 30)
        p_10_16 = (10, 16)
        p_10_34 = (10, 34)
        p_15_6 = (15, 6)
        p_15_16 = (15, 16)
        p_18_26 = (18, 26)
        p_18_34 = (18, 34)
        p_18_42 = (18, 42)
        p_33_6 = (2 * axis_x - p_15_6[0], p_15_6[1])
        p_33_16 = (2 * axis_x - p_15_16[0], p_15_16[1])
        p_34_26 = (34, 26)
        p_34_34 = (34, 34)
        p_34_42 = (34, 42)
        p_38_16 = (2 * axis_x - p_10_16[0], p_10_16[1])
        p_38_34 = (2 * axis_x - p_10_34[0], p_10_34[1])
        p_42_20 = (2 * axis_x - p_6_20[0], p_6_20[1])
        p_42_30 = (2 * axis_x - p_6_30[0], p_6_30[1])
        self.add_line('machine-1', p_18_34, p_10_34)
        self.add_arc('machine-2', p_10_34, p_6_30, radius_x=4, radius_y=4, sweep=True)
        self.add_line('machine-3', p_6_30, p_6_20)
        self.add_arc('machine-4', p_6_20, p_10_16, radius_x=4, radius_y=4, sweep=True)
        self.add_line('machine-5', p_10_16, p_38_16)
        self.add_arc('machine-6', p_38_16, p_42_20, radius_x=4, radius_y=4, sweep=True)
        self.add_line('machine-7', p_42_20, p_42_30)
        self.add_arc('machine-8', p_42_30, p_38_34, radius_x=4, radius_y=4, sweep=True)
        self.add_line('machine-9', p_38_34, p_34_34)
        self.add_contour('machine', 'machine-1', 'machine-2', 'machine-3', 'machine-4', 'machine-5', 'machine-6', 'machine-7', 'machine-8', 'machine-9', closed=False)
        self.add_line('rear-sheet-1', p_15_16, p_15_6)
        self.add_line('rear-sheet-2', p_15_6, p_33_6)
        self.add_line('rear-sheet-3', p_33_6, p_33_16)
        self.add_contour('rear-sheet', 'rear-sheet-1', 'rear-sheet-2', 'rear-sheet-3', closed=False)
        self.relate("connect", 'machine', 'rear-sheet')
        self.add_line('front-sheet-1', p_18_26, p_34_26)
        self.add_line('front-sheet-2', p_34_26, p_34_42)
        self.add_line('front-sheet-3', p_34_42, p_18_42)
        self.add_line('front-sheet-4', p_18_42, p_18_26)
        self.add_contour('front-sheet', 'front-sheet-1', 'front-sheet-2', 'front-sheet-3', 'front-sheet-4', closed=True)
        self.relate("connect", 'machine', 'front-sheet')
