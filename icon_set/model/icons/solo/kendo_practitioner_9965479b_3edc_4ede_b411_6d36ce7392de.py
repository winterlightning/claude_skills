'Kendo Martial Artist.\n\nSymbol plan: Kendo helmet with horizontal face band, split long garment and diagonal practice sword. Head r8 centered (18,12); actual torso junction (18,28) is 8 centerline / 4 ink units below head.\nKeyshape: VRECT_L; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9965479b-3edc-4ede-b411-6d36ce7392de'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_24/kendo_9965479b-3edc-4ede-b411-6d36ce7392de.svg'
AUTHOR = 'gpt-6'

class KendoPractitioner(Solo48):
    icon_id = 'kendo-practitioner'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/reference'
    aliases = ()
    keywords = ('kendo', 'practitioner')

    def build(self):
        # Kendo helmet with horizontal face band, split long garment and diagonal practice sword. Head r8 centered (18,12); actual torso junction (18,28) is 8 centerline / 4 ink units below head.
        axis_x = 24
        p_8_44 = (8, 44)
        p_10_12 = (10, 12)
        p_11_32 = (11, 32)
        p_18_28 = (18, 28)
        p_18_30 = (18, 30)
        p_20_31 = (20, 31)
        p_22_36 = (22, 36)
        p_22_44 = (22, 44)
        p_24_32 = (24, 32)
        p_26_12 = (26, 12)
        p_29_33 = (29, 33)
        p_34_44 = (34, 44)
        p_40_16 = (40, 16)
        self.add_arc('head-1', p_10_12, p_26_12, radius_x=8, radius_y=8, sweep=True)
        self.add_arc('head-2', p_26_12, p_10_12, radius_x=8, radius_y=8, sweep=True)
        self.add_contour('head', 'head-1', 'head-2', closed=True)
        self.add_line('helmet-band-1', p_10_12, p_26_12)
        self.add_contour('helmet-band', 'helmet-band-1', closed=False)
        self.relate("connect", 'head', 'helmet-band')
        self.add_bezier('torso-1', p_18_28, (p_18_30, p_20_31, p_24_32))
        self.add_contour('torso', 'torso-1', closed=False)
        self.add_line('robe-1', p_24_32, p_29_33)
        self.add_line('robe-2', p_29_33, p_34_44)
        self.add_line('robe-3', p_34_44, p_8_44)
        self.add_line('robe-4', p_8_44, p_11_32)
        self.add_line('robe-5', p_11_32, p_18_28)
        self.add_contour('robe', 'robe-1', 'robe-2', 'robe-3', 'robe-4', 'robe-5', closed=False)
        self.relate("connect", 'robe', 'torso')
        self.add_line('robe-split-1', p_22_44, p_22_36)
        self.add_contour('robe-split', 'robe-split-1', closed=False)
        self.relate("connect", 'robe', 'robe-split')
        self.add_line('sword-1', p_24_32, p_40_16)
        self.add_contour('sword', 'sword-1', closed=False)
        self.relate("connect", 'sword', 'torso')
        self.relate("connect", 'sword', 'robe')
        self.mark_human_figure("person", head="head", torso="torso-1", torso_junction="start")
