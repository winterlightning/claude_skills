'Knight with Sword and Shield.\n\nSymbol plan: Helmet, shield and sword form one equipment scene. Shield emblem and shoulder seams omitted for spacing.\nKeyshape: SQUARE; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'da426a95-1cd7-478a-9e67-d0cce97ae1dd'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_39/video game knight_da426a95-1cd7-478a-9e67-d0cce97ae1dd.svg'
AUTHOR = 'gpt-6'

class KnightWithEquipment(Solo48):
    icon_id = 'knight-with-equipment'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/reference'
    aliases = ()
    keywords = ('knight', 'with', 'equipment')

    def build(self):
        # Helmet, shield and sword form one equipment scene. Shield emblem and shoulder seams omitted for spacing.
        axis_x = 24
        p_6_23 = (6, 23)
        p_6_31 = (6, 31)
        p_6_35 = (6, 35)
        p_6_39 = (6, 39)
        p_10_10 = (10, 10)
        p_11_6 = (11, 6)
        p_12_41 = (12, 41)
        p_16_6 = (16, 6)
        p_16_42 = (16, 42)
        p_19_6 = (19, 6)
        p_20_41 = (20, 41)
        p_25_6 = (25, 6)
        p_26_31 = (26, 31)
        p_26_35 = (26, 35)
        p_26_39 = (26, 39)
        p_28_12 = (28, 12)
        p_28_18 = (28, 18)
        p_28_23 = (28, 23)
        p_35_29 = (35, 29)
        p_40_6 = (40, 6)
        p_40_42 = (40, 42)
        p_42_29 = (42, 29)
        self.add_line('helmet-1', p_6_23, p_10_10)
        self.add_bezier('helmet-2', p_10_10, (p_11_6, p_16_6, p_19_6))
        self.add_bezier('helmet-3', p_19_6, (p_25_6, p_28_12, p_28_18))
        self.add_line('helmet-4', p_28_18, p_28_23)
        self.add_line('helmet-5', p_28_23, p_6_23)
        self.add_contour('helmet', 'helmet-1', 'helmet-2', 'helmet-3', 'helmet-4', 'helmet-5', closed=True)
        self.add_line('shield-1', p_6_31, p_26_31)
        self.add_line('shield-2', p_26_31, p_26_35)
        self.add_bezier('shield-3', p_26_35, (p_26_39, p_20_41, p_16_42))
        self.add_bezier('shield-4', p_16_42, (p_12_41, p_6_39, p_6_35))
        self.add_line('shield-5', p_6_35, p_6_31)
        self.add_contour('shield', 'shield-1', 'shield-2', 'shield-3', 'shield-4', 'shield-5', closed=True)
        self.add_line('sword-1', p_40_6, p_40_42)
        self.add_contour('sword', 'sword-1', closed=False)
        self.add_line('guard-1', p_35_29, p_42_29)
        self.add_contour('guard', 'guard-1', closed=False)
        self.relate("connect", 'sword', 'guard')
