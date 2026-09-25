'Lit Smoking Joint.\n\nSymbol plan: Diagonal rolled joint and one curling smoke trail; wrapper seam omitted.\nKeyshape: SQUARE; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0c832e3d-56fb-471c-93b0-dfb3889b8b4d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_24/joint_0c832e3d-56fb-471c-93b0-dfb3889b8b4d.svg'
AUTHOR = 'gpt-6'

class SmokingCannabisJoint(Solo48):
    icon_id = 'smoking-cannabis-joint'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('smoking', 'cannabis', 'joint')

    def build(self):
        # Diagonal rolled joint and one curling smoke trail; wrapper seam omitted.
        axis_x = 24
        p_6_35 = (6, 35)
        p_13_42 = (13, 42)
        p_28_18 = (28, 18)
        p_29_8 = (29, 8)
        p_35_25 = (35, 25)
        p_38_14 = (38, 14)
        p_42_6 = (42, 6)
        p_42_14 = (42, 14)
        self.add_line('joint-1', p_6_35, p_28_18)
        self.add_line('joint-2', p_28_18, p_35_25)
        self.add_line('joint-3', p_35_25, p_13_42)
        self.add_line('joint-4', p_13_42, p_6_35)
        self.add_contour('joint', 'joint-1', 'joint-2', 'joint-3', 'joint-4', closed=True)
        self.add_bezier('smoke-1', p_38_14, (p_29_8, p_42_14, p_42_6))
        self.add_contour('smoke', 'smoke-1', closed=False)
