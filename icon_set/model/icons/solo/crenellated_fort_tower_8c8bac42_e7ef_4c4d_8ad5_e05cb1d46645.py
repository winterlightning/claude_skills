'Medieval Stone Castle Tower.\n\nSymbol plan: Two broad crenellations and central notch above flared tower with arched doorway; reduce three tiny merlons to two.\nKeyshape: VRECT_L; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8c8bac42-e7ef-4c4d-8ad5-e05cb1d46645'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_19/fort_8c8bac42-e7ef-4c4d-8ad5-e05cb1d46645.svg'
AUTHOR = 'gpt-6'

class CrenellatedFortTower(Solo48):
    icon_id = 'crenellated-fort-tower'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('crenellated', 'fort', 'tower')

    def build(self):
        # Two broad crenellations and central notch above flared tower with arched doorway; reduce three tiny merlons to two.
        axis_x = 24
        p_8_4 = (8, 4)
        p_8_22 = (8, 22)
        p_8_44 = (8, 44)
        p_13_22 = (13, 22)
        p_18_4 = (18, 4)
        p_18_14 = (18, 14)
        p_19_34 = (19, 34)
        p_19_44 = (19, 44)
        p_29_34 = (2 * axis_x - p_19_34[0], p_19_34[1])
        p_29_44 = (2 * axis_x - p_19_44[0], p_19_44[1])
        p_30_4 = (2 * axis_x - p_18_4[0], p_18_4[1])
        p_30_14 = (2 * axis_x - p_18_14[0], p_18_14[1])
        p_35_22 = (2 * axis_x - p_13_22[0], p_13_22[1])
        p_40_4 = (2 * axis_x - p_8_4[0], p_8_4[1])
        p_40_22 = (2 * axis_x - p_8_22[0], p_8_22[1])
        p_40_44 = (2 * axis_x - p_8_44[0], p_8_44[1])
        self.add_line('tower-1', p_8_4, p_18_4)
        self.add_line('tower-2', p_18_4, p_18_14)
        self.add_line('tower-3', p_18_14, p_30_14)
        self.add_line('tower-4', p_30_14, p_30_4)
        self.add_line('tower-5', p_30_4, p_40_4)
        self.add_line('tower-6', p_40_4, p_40_22)
        self.add_line('tower-7', p_40_22, p_35_22)
        self.add_line('tower-8', p_35_22, p_40_44)
        self.add_line('tower-9', p_40_44, p_8_44)
        self.add_line('tower-10', p_8_44, p_13_22)
        self.add_line('tower-11', p_13_22, p_8_22)
        self.add_line('tower-12', p_8_22, p_8_4)
        self.add_contour('tower', 'tower-1', 'tower-2', 'tower-3', 'tower-4', 'tower-5', 'tower-6', 'tower-7', 'tower-8', 'tower-9', 'tower-10', 'tower-11', 'tower-12', closed=True)
        self.add_line('door-1', p_19_44, p_19_34)
        self.add_arc('door-2', p_19_34, p_29_34, radius_x=5, radius_y=5, sweep=True)
        self.add_line('door-3', p_29_34, p_29_44)
        self.add_contour('door', 'door-1', 'door-2', 'door-3', closed=False)
        self.relate("connect", 'tower', 'door')
