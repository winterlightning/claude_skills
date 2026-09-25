'Man Holding the World Globe.\n\nSymbol plan: Atlas carries a broad globe above his head with both arms raised. Lower globe outline is occluded by the figure; one meridian distinguishes the globe. Circular head bottom30 and neck38 give exact4 ink clearance.\nKeyshape: VRECT_L; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a2d887a3-f33d-43fa-982a-56705e54bb1a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_21/greek god atlas_a2d887a3-f33d-43fa-982a-56705e54bb1a.svg'
AUTHOR = 'gpt-6'

class AtlasHoldingGlobeOverhead(Solo48):
    icon_id = 'atlas-holding-globe-overhead'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('atlas', 'holding', 'globe', 'overhead')

    def build(self):
        # Atlas carries a broad globe above his head with both arms raised. Lower globe outline is occluded by the figure; one meridian distinguishes the globe. Circular head bottom30 and neck38 give exact4 ink clearance.
        axis_x = 24
        p_8_20 = (8, 20)
        p_8_30 = (8, 30)
        p_8_36 = (8, 36)
        p_10_38 = (10, 38)
        p_12_16 = (12, 16)
        p_16_38 = (16, 38)
        p_20_26 = (20, 26)
        p_24_4 = (24, 4)
        p_24_12 = (24, 12)
        p_24_38 = (24, 38)
        p_24_44 = (24, 44)
        p_28_26 = (2 * axis_x - p_20_26[0], p_20_26[1])
        p_32_38 = (2 * axis_x - p_16_38[0], p_16_38[1])
        p_36_16 = (2 * axis_x - p_12_16[0], p_12_16[1])
        p_38_38 = (2 * axis_x - p_10_38[0], p_10_38[1])
        p_40_20 = (2 * axis_x - p_8_20[0], p_8_20[1])
        p_40_30 = (2 * axis_x - p_8_30[0], p_8_30[1])
        p_40_36 = (2 * axis_x - p_8_36[0], p_8_36[1])
        self.add_arc('head-1', p_20_26, p_28_26, radius_x=4, radius_y=4, sweep=True)
        self.add_arc('head-2', p_28_26, p_20_26, radius_x=4, radius_y=4, sweep=True)
        self.add_contour('head', 'head-1', 'head-2', closed=True)
        self.add_arc('globe-1', p_12_16, p_24_4, radius_x=12, radius_y=12, sweep=True)
        self.add_arc('globe-2', p_24_4, p_36_16, radius_x=12, radius_y=12, sweep=True)
        self.add_contour('globe', 'globe-1', 'globe-2', closed=False)
        self.add_line('meridian-1', p_24_4, p_24_12)
        self.add_contour('meridian', 'meridian-1', closed=False)
        self.relate("connect", 'globe', 'meridian')
        self.add_line('left-body-1', p_12_16, p_8_20)
        self.add_line('left-body-2', p_8_20, p_8_30)
        self.add_bezier('left-body-3', p_8_30, (p_8_36, p_10_38, p_16_38))
        self.add_line('left-body-4', p_16_38, p_24_38)
        self.add_line('left-body-5', p_24_38, p_24_44)
        self.add_contour('left-body', 'left-body-1', 'left-body-2', 'left-body-3', 'left-body-4', 'left-body-5', closed=False)
        self.relate("connect", 'globe', 'left-body')
        self.add_line('right-arm-1', p_24_38, p_32_38)
        self.add_bezier('right-arm-2', p_32_38, (p_38_38, p_40_36, p_40_30))
        self.add_line('right-arm-3', p_40_30, p_40_20)
        self.add_line('right-arm-4', p_40_20, p_36_16)
        self.add_contour('right-arm', 'right-arm-1', 'right-arm-2', 'right-arm-3', 'right-arm-4', closed=False)
        self.relate("connect", 'left-body', 'right-arm')
        self.relate("connect", 'globe', 'right-arm')
        self.mark_human_figure("atlas", head="head", torso="left-body-5", torso_junction="start")
