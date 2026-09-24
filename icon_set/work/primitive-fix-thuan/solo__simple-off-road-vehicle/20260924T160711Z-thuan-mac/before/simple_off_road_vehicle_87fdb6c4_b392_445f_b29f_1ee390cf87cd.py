'Off-Road Vehicle.\n\nSymbol plan: Side-view off-road vehicle with raised trapezoid cab and two oversized wheels; omit small hubs.\nKeyshape: HRECT_L; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '87fdb6c4-b392-445f-b29f-1ee390cf87cd'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_23/jeep_87fdb6c4-b392-445f-b29f-1ee390cf87cd.svg'
AUTHOR = 'gpt-6'

class SimpleOffRoadVehicle(Solo48):
    icon_id = 'simple-off-road-vehicle'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/reference'
    aliases = ()
    keywords = ('simple', 'off', 'road', 'vehicle')

    def build(self):
        # Side-view off-road vehicle with raised trapezoid cab and two oversized wheels; omit small hubs.
        axis_x = 24
        p_4_20 = (4, 20)
        p_4_34 = (4, 34)
        p_15_20 = (15, 20)
        p_16_34 = (16, 34)
        p_18_8 = (18, 8)
        p_32_34 = (2 * axis_x - p_16_34[0], p_16_34[1])
        p_34_8 = (34, 8)
        p_34_20 = (34, 20)
        p_44_20 = (2 * axis_x - p_4_20[0], p_4_20[1])
        p_44_34 = (2 * axis_x - p_4_34[0], p_4_34[1])
        self.add_arc('rear-wheel-1', p_4_34, p_16_34, radius_x=6, radius_y=6, sweep=True)
        self.add_arc('rear-wheel-2', p_16_34, p_4_34, radius_x=6, radius_y=6, sweep=True)
        self.add_contour('rear-wheel', 'rear-wheel-1', 'rear-wheel-2', closed=True)
        self.add_arc('front-wheel-1', p_32_34, p_44_34, radius_x=6, radius_y=6, sweep=True)
        self.add_arc('front-wheel-2', p_44_34, p_32_34, radius_x=6, radius_y=6, sweep=True)
        self.add_contour('front-wheel', 'front-wheel-1', 'front-wheel-2', closed=True)
        self.add_line('body-1', p_4_34, p_4_20)
        self.add_line('body-2', p_4_20, p_44_20)
        self.add_line('body-3', p_44_20, p_44_34)
        self.add_contour('body', 'body-1', 'body-2', 'body-3', closed=False)
        self.relate("connect", 'body', 'rear-wheel')
        self.relate("connect", 'body', 'front-wheel')
        self.add_line('cab-1', p_15_20, p_18_8)
        self.add_line('cab-2', p_18_8, p_34_8)
        self.add_line('cab-3', p_34_8, p_34_20)
        self.add_contour('cab', 'cab-1', 'cab-2', 'cab-3', closed=False)
        self.relate("connect", 'body', 'cab')
