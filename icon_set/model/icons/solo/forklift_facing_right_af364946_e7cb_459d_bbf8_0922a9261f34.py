'Industrial Warehouse Forklift Truck.\n\nSymbol plan: Right-facing forklift with paired circular wheels, cab guard and forward fork; omit minor body steps.\nKeyshape: HRECT_L; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'af364946-e7cb-459d-bbf8-0922a9261f34'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_19/forklift_af364946-e7cb-459d-bbf8-0922a9261f34.svg'
AUTHOR = 'gpt-6'

class ForkliftFacingRight(Solo48):
    icon_id = 'forklift-facing-right'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/reference'
    aliases = ()
    keywords = ('forklift', 'facing', 'right')

    def build(self):
        # Right-facing forklift with paired circular wheels, cab guard and forward fork; omit minor body steps.
        axis_x = 24
        p_4_20 = (4, 20)
        p_4_35 = (4, 35)
        p_10_8 = (10, 8)
        p_10_20 = (10, 20)
        p_14_35 = (14, 35)
        p_19_20 = (19, 20)
        p_22_35 = (22, 35)
        p_23_8 = (23, 8)
        p_23_21 = (23, 21)
        p_32_21 = (32, 21)
        p_32_35 = (32, 35)
        p_40_16 = (40, 16)
        p_40_35 = (40, 35)
        p_44_35 = (2 * axis_x - p_4_35[0], p_4_35[1])
        self.add_arc('rear-wheel-1', p_4_35, p_14_35, radius_x=5, radius_y=5, sweep=True)
        self.add_arc('rear-wheel-2', p_14_35, p_4_35, radius_x=5, radius_y=5, sweep=True)
        self.add_contour('rear-wheel', 'rear-wheel-1', 'rear-wheel-2', closed=True)
        self.add_arc('front-wheel-1', p_22_35, p_32_35, radius_x=5, radius_y=5, sweep=True)
        self.add_arc('front-wheel-2', p_32_35, p_22_35, radius_x=5, radius_y=5, sweep=True)
        self.add_contour('front-wheel', 'front-wheel-1', 'front-wheel-2', closed=True)
        self.add_line('body-1', p_4_35, p_4_20)
        self.add_line('body-2', p_4_20, p_19_20)
        self.add_line('body-3', p_19_20, p_23_21)
        self.add_line('body-4', p_23_21, p_32_21)
        self.add_line('body-5', p_32_21, p_32_35)
        self.add_contour('body', 'body-1', 'body-2', 'body-3', 'body-4', 'body-5', closed=False)
        self.relate("connect", 'rear-wheel', 'body')
        self.relate("connect", 'front-wheel', 'body')
        self.add_line('cab-1', p_10_20, p_10_8)
        self.add_line('cab-2', p_10_8, p_23_8)
        self.add_line('cab-3', p_23_8, p_32_21)
        self.add_contour('cab', 'cab-1', 'cab-2', 'cab-3', closed=False)
        self.relate("connect", 'cab', 'body')
        self.add_line('fork-1', p_40_16, p_40_35)
        self.add_line('fork-2', p_40_35, p_44_35)
        self.add_contour('fork', 'fork-1', 'fork-2', closed=False)
