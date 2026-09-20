'Passenger Sedan Car.\n\nSymbol plan: Car with a low cabin and two open circular wheels. Remove small enclosed window panels and separate bumpers.\nKeyshape: HRECT_M; authored on SOLO48, not scaled from source.\nLucide: car.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2ac64939-46bf-4dd1-9f96-1b8c0d3a2cd5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_25/limo_2ac64939-46bf-4dd1-9f96-1b8c0d3a2cd5.svg'
AUTHOR = 'gpt-6'

class Limousine(Solo48):
    icon_id = 'limousine'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/reference'
    aliases = ()
    keywords = ('limousine',)

    def build(self):
        # Car with a low cabin and two open circular wheels. Remove small enclosed window panels and separate bumpers.
        axis_x = 24
        p_4_18 = (4, 18)
        p_4_26 = (4, 26)
        p_11_18 = (11, 18)
        p_12_26 = (12, 26)
        p_12_38 = (12, 38)
        p_17_10 = (17, 10)
        p_18_32 = (18, 32)
        p_24_10 = (24, 10)
        p_24_20 = (24, 20)
        p_29_10 = (29, 10)
        p_30_32 = (2 * axis_x - p_18_32[0], p_18_32[1])
        p_36_18 = (36, 18)
        p_36_26 = (2 * axis_x - p_12_26[0], p_12_26[1])
        p_36_38 = (2 * axis_x - p_12_38[0], p_12_38[1])
        p_44_18 = (2 * axis_x - p_4_18[0], p_4_18[1])
        p_44_26 = (2 * axis_x - p_4_26[0], p_4_26[1])
        self.add_line('body-1', p_12_26, p_4_26)
        self.add_line('body-2', p_4_26, p_4_18)
        self.add_line('body-3', p_4_18, p_11_18)
        self.add_line('body-4', p_11_18, p_17_10)
        self.add_line('body-5', p_17_10, p_24_10)
        self.add_line('body-5-join-1', p_24_10, p_29_10)
        self.add_line('body-6', p_29_10, p_36_18)
        self.add_line('body-7', p_36_18, p_44_18)
        self.add_line('body-8', p_44_18, p_44_26)
        self.add_line('body-9', p_44_26, p_36_26)
        self.add_contour('body', 'body-1', 'body-2', 'body-3', 'body-4', 'body-5', 'body-5-join-1', 'body-6', 'body-7', 'body-8', 'body-9', closed=False)
        self.add_arc('wheel-left-1', p_12_26, p_12_38, radius_x=6, radius_y=6, sweep=True)
        self.add_arc('wheel-left-2', p_12_38, p_12_26, radius_x=6, radius_y=6, sweep=True)
        self.add_contour('wheel-left', 'wheel-left-1', 'wheel-left-2', closed=True)
        self.add_arc('wheel-right-1', p_36_26, p_36_38, radius_x=6, radius_y=6, sweep=True)
        self.add_arc('wheel-right-2', p_36_38, p_36_26, radius_x=6, radius_y=6, sweep=True)
        self.add_contour('wheel-right', 'wheel-right-1', 'wheel-right-2', closed=True)
        self.add_line('chassis-1', p_18_32, p_30_32)
        self.add_contour('chassis', 'chassis-1', closed=False)
        self.add_line('pillar-1', p_24_10, p_24_20)
        self.add_contour('pillar', 'pillar-1', closed=False)
        self.relate("connect", 'body', 'wheel-left')
        self.relate("connect", 'chassis', 'wheel-left')
        self.relate("connect", 'body', 'wheel-right')
        self.relate("connect", 'chassis', 'wheel-right')
        self.relate("connect", 'pillar', 'body')
