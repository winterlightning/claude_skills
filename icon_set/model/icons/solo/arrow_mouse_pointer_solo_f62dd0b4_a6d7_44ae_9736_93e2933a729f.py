'Mouse Cursor Pointer Arrow.\n\nSymbol plan: Diagonal mouse cursor with broad pointed tip, inset shoulder and angled shaft.\nKeyshape: VRECT_L; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f62dd0b4-a6d7-44ae-9736-93e2933a729f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_23/i cursor_f62dd0b4-a6d7-44ae-9736-93e2933a729f.svg'
AUTHOR = 'gpt-6'

class ArrowMousePointerSolo(Solo48):
    icon_id = 'arrow-mouse-pointer-solo'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('arrow', 'mouse', 'pointer', 'solo')

    def build(self):
        # Diagonal mouse cursor with broad pointed tip, inset shoulder and angled shaft.
        axis_x = 24
        p_8_4 = (8, 4)
        p_8_40 = (8, 40)
        p_18_31 = (18, 31)
        p_25_44 = (25, 44)
        p_27_29 = (27, 29)
        p_34_40 = (34, 40)
        p_40_27 = (40, 27)
        self.add_line('pointer-1', p_8_4, p_40_27)
        self.add_line('pointer-2', p_40_27, p_27_29)
        self.add_line('pointer-3', p_27_29, p_34_40)
        self.add_line('pointer-4', p_34_40, p_25_44)
        self.add_line('pointer-5', p_25_44, p_18_31)
        self.add_line('pointer-6', p_18_31, p_8_40)
        self.add_line('pointer-7', p_8_40, p_8_4)
        self.add_contour('pointer', 'pointer-1', 'pointer-2', 'pointer-3', 'pointer-4', 'pointer-5', 'pointer-6', 'pointer-7', closed=True)
