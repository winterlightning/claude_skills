'Person Standing In Circle.\n\nSymbol plan: Standing figure inside an open ground ring. Shortened legs leave a clear ground opening; exact head gap.\nKeyshape: VRECT_L; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '49e0b9d1-bc0c-4794-9bf3-4015f1ce8d7a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_25/location user_49e0b9d1-bc0c-4794-9bf3-4015f1ce8d7a.svg'
AUTHOR = 'gpt-6'

class PersonLocation(Solo48):
    icon_id = 'person-location'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('person', 'location')

    def build(self):
        # Standing figure inside an open ground ring. Shortened legs leave a clear ground opening; exact head gap.
        axis_x = 24
        p_8_34 = (8, 34)
        p_8_36 = (8, 36)
        p_8_40 = (8, 40)
        p_9_31 = (9, 31)
        p_12_29 = (12, 29)
        p_15_44 = (15, 44)
        p_16_22 = (16, 22)
        p_19_9 = (19, 9)
        p_19_34 = (19, 34)
        p_24_22 = (24, 22)
        p_24_28 = (24, 28)
        p_24_44 = (24, 44)
        p_29_9 = (2 * axis_x - p_19_9[0], p_19_9[1])
        p_29_34 = (2 * axis_x - p_19_34[0], p_19_34[1])
        p_32_22 = (2 * axis_x - p_16_22[0], p_16_22[1])
        p_33_44 = (2 * axis_x - p_15_44[0], p_15_44[1])
        p_36_29 = (2 * axis_x - p_12_29[0], p_12_29[1])
        p_39_31 = (2 * axis_x - p_9_31[0], p_9_31[1])
        p_40_34 = (2 * axis_x - p_8_34[0], p_8_34[1])
        p_40_36 = (2 * axis_x - p_8_36[0], p_8_36[1])
        p_40_40 = (2 * axis_x - p_8_40[0], p_8_40[1])
        self.add_arc('head-1', p_19_9, p_29_9, radius_x=5, radius_y=5, sweep=True)
        self.add_arc('head-2', p_29_9, p_19_9, radius_x=5, radius_y=5, sweep=True)
        self.add_contour('head', 'head-1', 'head-2', closed=True)
        self.add_line('torso-1', p_24_22, p_24_28)
        self.add_contour('torso', 'torso-1', closed=False)
        self.mark_human_figure("person", head="head", torso="torso-1", torso_junction="start")
        self.add_line('legs-1', p_19_34, p_24_28)
        self.add_line('legs-2', p_24_28, p_29_34)
        self.add_contour('legs', 'legs-1', 'legs-2', closed=False)
        self.relate("connect", 'legs', 'torso')
        self.add_line('arms-1', p_16_22, p_24_22)
        self.add_line('arms-1-join-1', p_24_22, p_32_22)
        self.add_contour('arms', 'arms-1', 'arms-1-join-1', closed=False)
        self.relate("connect", 'arms', 'torso')
        self.add_bezier('ground-1', p_12_29, (p_9_31, p_8_34, p_8_36))
        self.add_bezier('ground-2', p_8_36, (p_8_40, p_15_44, p_24_44))
        self.add_bezier('ground-3', p_24_44, (p_33_44, p_40_40, p_40_36))
        self.add_bezier('ground-4', p_40_36, (p_40_34, p_39_31, p_36_29))
        self.add_contour('ground', 'ground-1', 'ground-2', 'ground-3', 'ground-4', closed=False)
