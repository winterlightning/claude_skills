'Medieval Executioner Axe.\n\nSymbol plan: Broad convex medieval axe blade on a long diagonal handle.\nKeyshape: SQUARE; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9cc63cfd-be10-4af6-b277-92e252919cc7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_18/fantasy medieval excutioner axe_9cc63cfd-be10-4af6-b277-92e252919cc7.svg'
AUTHOR = 'gpt-6'

class BroadBladedMedievalAxe(Solo48):
    icon_id = 'broad-bladed-medieval-axe'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/reference'
    aliases = ()
    keywords = ('broad', 'bladed', 'medieval', 'axe')

    def build(self):
        # Broad convex medieval axe blade on a long diagonal handle.
        axis_x = 24
        p_6_42 = (6, 42)
        p_22_22 = (22, 22)
        p_31_12 = (31, 12)
        p_32_34 = (32, 34)
        p_36_6 = (36, 6)
        p_38_34 = (38, 34)
        p_41_14 = (41, 14)
        p_42_16 = (42, 16)
        p_42_18 = (42, 18)
        p_42_22 = (42, 22)
        p_42_29 = (42, 29)
        self.add_line('handle-1', p_6_42, p_36_6)
        self.add_contour('handle', 'handle-1', closed=False)
        self.add_line('blade-1', p_31_12, p_41_14)
        self.add_bezier('blade-2', p_41_14, (p_42_16, p_42_18, p_42_22))
        self.add_bezier('blade-3', p_42_22, (p_42_29, p_38_34, p_32_34))
        self.add_line('blade-4', p_32_34, p_22_22)
        self.add_contour('blade', 'blade-1', 'blade-2', 'blade-3', 'blade-4', closed=False)
        self.relate("connect", 'handle', 'blade')
