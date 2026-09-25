'Poisoned Dagger with Drops.\n\nSymbol plan: Diagonal dagger with transverse guard and three surrounding drop marks. Hollow drop details and pommel ring omitted for spacing; no specific poison meaning assigned.\nKeyshape: SQUARE; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a44c8381-f482-4b4b-995e-3d8b71f84688'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_18/fantasy medieval assassins knife poison_a44c8381-f482-4b4b-995e-3d8b71f84688.svg'
AUTHOR = 'gpt-6'

class DaggerBesideThreePointedDroplets(Solo48):
    icon_id = 'dagger-beside-three-pointed-droplets'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('dagger', 'beside', 'three', 'pointed', 'droplets')

    def build(self):
        # Diagonal dagger with transverse guard and three surrounding drop marks. Hollow drop details and pommel ring omitted for spacing; no specific poison meaning assigned.
        axis_x = 24
        p_6_6 = (6, 6)
        p_8_42 = (8, 42)
        p_10_34 = (10, 34)
        p_17_27 = (17, 27)
        p_22_22 = (22, 22)
        p_27_17 = (27, 17)
        p_34_10 = (34, 10)
        p_41_22 = (41, 22)
        p_42_8 = (42, 8)
        p_42_42 = (42, 42)
        self.add_line('blade-1', p_17_27, p_42_42)
        self.add_line('blade-2', p_42_42, p_27_17)
        self.add_contour('blade', 'blade-1', 'blade-2', closed=False)
        self.add_line('guard-1', p_10_34, p_17_27)
        self.add_line('guard-2', p_17_27, p_22_22)
        self.add_line('guard-3', p_22_22, p_27_17)
        self.add_line('guard-4', p_27_17, p_34_10)
        self.add_contour('guard', 'guard-1', 'guard-2', 'guard-3', 'guard-4', closed=False)
        self.add_line('grip-1', p_6_6, p_22_22)
        self.add_contour('grip', 'grip-1', closed=False)
        self.relate("connect", 'blade', 'guard')
        self.relate("connect", 'grip', 'guard')
        self.add_line('a-1', p_42_8, p_42_8)
        self.add_contour('a', 'a-1', closed=False)
        self.add_line('b-1', p_8_42, p_8_42)
        self.add_contour('b', 'b-1', closed=False)
        self.add_line('c-1', p_41_22, p_41_22)
        self.add_contour('c', 'c-1', closed=False)
