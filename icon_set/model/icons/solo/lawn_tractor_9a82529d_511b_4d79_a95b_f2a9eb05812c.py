'Push Lawnmower.\n\nSymbol plan: Lawn tractor with two unequal wheels, steering bar and raised seat. Body contour joins the top of each wheel without overlap.\nKeyshape: HRECT_L; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9a82529d-511b-4d79-a95b-f2a9eb05812c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_25/lawn tractor_9a82529d-511b-4d79-a95b-f2a9eb05812c.svg'
AUTHOR = 'gpt-6'

class LawnTractor(Solo48):
    icon_id = 'lawn-tractor'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/reference'
    aliases = ()
    keywords = ('lawn', 'tractor')

    def build(self):
        # Lawn tractor with two unequal wheels, steering bar and raised seat. Body contour joins the top of each wheel without overlap.
        axis_x = 24
        p_4_8 = (4, 8)
        p_10_8 = (10, 8)
        p_12_24 = (12, 24)
        p_12_40 = (12, 40)
        p_17_24 = (17, 24)
        p_27_14 = (27, 14)
        p_27_24 = (27, 24)
        p_28_24 = (28, 24)
        p_33_24 = (33, 24)
        p_36_25 = (36, 25)
        p_37_14 = (37, 14)
        p_38_28 = (38, 28)
        p_38_40 = (38, 40)
        self.add_line('body-1', p_12_24, p_17_24)
        self.add_line('body-1-join-1', p_17_24, p_27_24)
        self.add_line('body-1-join-2', p_27_24, p_28_24)
        self.add_bezier('body-2', p_28_24, (p_33_24, p_36_25, p_38_28))
        self.add_contour('body', 'body-1', 'body-1-join-1', 'body-1-join-2', 'body-2', closed=False)
        self.add_arc('rear-wheel-1', p_12_24, p_12_40, radius_x=8, radius_y=8, sweep=True)
        self.add_arc('rear-wheel-2', p_12_40, p_12_24, radius_x=8, radius_y=8, sweep=True)
        self.add_contour('rear-wheel', 'rear-wheel-1', 'rear-wheel-2', closed=True)
        self.add_arc('front-wheel-1', p_38_28, p_38_40, radius_x=6, radius_y=6, sweep=True)
        self.add_arc('front-wheel-2', p_38_40, p_38_28, radius_x=6, radius_y=6, sweep=True)
        self.add_contour('front-wheel', 'front-wheel-1', 'front-wheel-2', closed=True)
        self.relate("connect", 'body', 'rear-wheel')
        self.relate("connect", 'body', 'front-wheel')
        self.add_line('steer-1', p_4_8, p_10_8)
        self.add_line('steer-2', p_10_8, p_17_24)
        self.add_contour('steer', 'steer-1', 'steer-2', closed=False)
        self.relate("connect", 'steer', 'body')
        self.add_line('seat-1', p_27_24, p_27_14)
        self.add_line('seat-2', p_27_14, p_37_14)
        self.add_contour('seat', 'seat-1', 'seat-2', closed=False)
        self.relate("connect", 'seat', 'body')
