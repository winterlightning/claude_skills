'Jackal Side Profile.\n\nSymbol plan: Standing jackal facing right, pointed ear, muzzle, foreleg and bent rear leg; omit tiny toe curls.\nKeyshape: SQUARE; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fafdef3d-ee1f-46a0-aacf-a32be3611bc1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_23/jackal_fafdef3d-ee1f-46a0-aacf-a32be3611bc1.svg'
AUTHOR = 'gpt-6'

class PointedEaredJackal(Solo48):
    icon_id = 'pointed-eared-jackal'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('pointed', 'eared', 'jackal')

    def build(self):
        # Standing jackal facing right, pointed ear, muzzle, foreleg and bent rear leg; omit tiny toe curls.
        axis_x = 24
        p_6_42 = (6, 42)
        p_8_24 = (8, 24)
        p_9_18 = (9, 18)
        p_15_34 = (15, 34)
        p_15_42 = (15, 42)
        p_16_20 = (16, 20)
        p_19_30 = (19, 30)
        p_23_18 = (23, 18)
        p_27_30 = (27, 30)
        p_28_42 = (28, 42)
        p_30_6 = (30, 6)
        p_35_15 = (35, 15)
        p_37_26 = (37, 26)
        p_37_42 = (37, 42)
        p_40_26 = (40, 26)
        p_42_18 = (42, 18)
        self.add_line('jackal-1', p_6_42, p_8_24)
        self.add_bezier('jackal-2', p_8_24, (p_9_18, p_16_20, p_23_18))
        self.add_line('jackal-3', p_23_18, p_30_6)
        self.add_line('jackal-4', p_30_6, p_35_15)
        self.add_line('jackal-5', p_35_15, p_42_18)
        self.add_line('jackal-6', p_42_18, p_40_26)
        self.add_line('jackal-7', p_40_26, p_37_26)
        self.add_line('jackal-8', p_37_26, p_37_42)
        self.add_line('jackal-9', p_37_42, p_28_42)
        self.add_line('jackal-10', p_28_42, p_27_30)
        self.add_line('jackal-11', p_27_30, p_19_30)
        self.add_line('jackal-12', p_19_30, p_15_34)
        self.add_line('jackal-13', p_15_34, p_15_42)
        self.add_line('jackal-14', p_15_42, p_6_42)
        self.add_contour('jackal', 'jackal-1', 'jackal-2', 'jackal-3', 'jackal-4', 'jackal-5', 'jackal-6', 'jackal-7', 'jackal-8', 'jackal-9', 'jackal-10', 'jackal-11', 'jackal-12', 'jackal-13', 'jackal-14', closed=True)
