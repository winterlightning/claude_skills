'Passenger Airplane Side View.\n\nSymbol plan: Right-facing fuselage, tall tail and swept near wing. Hidden wing/body edges are omitted.\nKeyshape: HRECT_L; authored on SOLO48, not scaled from source.\nLucide: plane.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9de328f1-e686-4c93-955f-3977dc939c3a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_01/airfield_9de328f1-e686-4c93-955f-3977dc939c3a.svg'
AUTHOR = 'gpt-6'

class AirplaneSideProfileSingleWing(Solo48):
    icon_id = 'airplane-side-profile-single-wing'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/reference'
    aliases = ()
    keywords = ('airplane', 'side', 'profile', 'single', 'wing')

    def build(self):
        # Right-facing fuselage, tall tail and swept near wing. Hidden wing/body edges are omitted.
        axis_x = 24
        p_4_8 = (4, 8)
        p_4_22 = (4, 22)
        p_4_25 = (4, 25)
        p_4_28 = (4, 28)
        p_5_30 = (5, 30)
        p_6_20 = (6, 20)
        p_8_20 = (8, 20)
        p_9_30 = (9, 30)
        p_9_40 = (9, 40)
        p_12_8 = (12, 8)
        p_17_30 = (17, 30)
        p_19_40 = (19, 40)
        p_22_20 = (22, 20)
        p_29_32 = (29, 32)
        p_36_20 = (36, 20)
        p_36_32 = (36, 32)
        p_41_20 = (41, 20)
        p_41_32 = (41, 32)
        p_44_23 = (44, 23)
        p_44_26 = (44, 26)
        p_44_29 = (44, 29)
        self.add_line('plane-1', p_4_8, p_12_8)
        self.add_line('plane-2', p_12_8, p_22_20)
        self.add_line('plane-3', p_22_20, p_36_20)
        self.add_bezier('plane-4', p_36_20, (p_41_20, p_44_23, p_44_26))
        self.add_bezier('plane-5', p_44_26, (p_44_29, p_41_32, p_36_32))
        self.add_line('plane-6', p_36_32, p_29_32)
        self.add_line('plane-7', p_29_32, p_19_40)
        self.add_line('plane-8', p_19_40, p_9_40)
        self.add_line('plane-9', p_9_40, p_17_30)
        self.add_line('plane-10', p_17_30, p_9_30)
        self.add_bezier('plane-11', p_9_30, (p_5_30, p_4_28, p_4_25))
        self.add_bezier('plane-12', p_4_25, (p_4_22, p_6_20, p_8_20))
        self.add_line('plane-13', p_8_20, p_4_8)
        self.add_contour('plane', 'plane-1', 'plane-2', 'plane-3', 'plane-4', 'plane-5', 'plane-6', 'plane-7', 'plane-8', 'plane-9', 'plane-10', 'plane-11', 'plane-12', 'plane-13', closed=True)
