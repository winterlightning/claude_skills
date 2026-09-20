'Mining Cart with Ore.\n\nSymbol plan: Loaded mine cart with jagged ore, two wheels and ground; omit thin double rim.\nKeyshape: HRECT_L; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '41925122-34bb-414f-a8cc-0203f8b37715'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_25/lode_41925122-34bb-414f-a8cc-0203f8b37715.svg'
AUTHOR = 'gpt-6'

class MineCart(Solo48):
    icon_id = 'mine-cart'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/reference'
    aliases = ()
    keywords = ('mine', 'cart')

    def build(self):
        # Loaded mine cart with jagged ore, two wheels and ground; omit thin double rim.
        axis_x = 24
        p_4_18 = (4, 18)
        p_6_18 = (6, 18)
        p_9_30 = (9, 30)
        p_13_30 = (13, 30)
        p_13_40 = (13, 40)
        p_14_9 = (14, 9)
        p_20_10 = (20, 10)
        p_26_8 = (26, 8)
        p_33_10 = (33, 10)
        p_35_30 = (2 * axis_x - p_13_30[0], p_13_30[1])
        p_35_40 = (2 * axis_x - p_13_40[0], p_13_40[1])
        p_38_9 = (38, 9)
        p_39_30 = (2 * axis_x - p_9_30[0], p_9_30[1])
        p_42_18 = (2 * axis_x - p_6_18[0], p_6_18[1])
        p_44_18 = (2 * axis_x - p_4_18[0], p_4_18[1])
        self.add_line('bin-1', p_4_18, p_44_18)
        self.add_line('bin-2', p_44_18, p_39_30)
        self.add_line('bin-3', p_39_30, p_35_30)
        self.add_line('bin-4', p_35_30, p_13_30)
        self.add_line('bin-5', p_13_30, p_9_30)
        self.add_line('bin-6', p_9_30, p_4_18)
        self.add_contour('bin', 'bin-1', 'bin-2', 'bin-3', 'bin-4', 'bin-5', 'bin-6', closed=True)
        self.add_line('ore-1', p_6_18, p_14_9)
        self.add_line('ore-2', p_14_9, p_20_10)
        self.add_line('ore-3', p_20_10, p_26_8)
        self.add_line('ore-4', p_26_8, p_33_10)
        self.add_line('ore-5', p_33_10, p_38_9)
        self.add_line('ore-6', p_38_9, p_42_18)
        self.add_contour('ore', 'ore-1', 'ore-2', 'ore-3', 'ore-4', 'ore-5', 'ore-6', closed=False)
        self.relate("connect", 'bin', 'ore')
        self.add_arc('wheel-left-1', p_13_30, p_13_40, radius_x=5, radius_y=5, sweep=True)
        self.add_arc('wheel-left-2', p_13_40, p_13_30, radius_x=5, radius_y=5, sweep=True)
        self.add_contour('wheel-left', 'wheel-left-1', 'wheel-left-2', closed=True)
        self.relate("connect", 'bin', 'wheel-left')
        self.add_arc('wheel-right-1', p_35_30, p_35_40, radius_x=5, radius_y=5, sweep=True)
        self.add_arc('wheel-right-2', p_35_40, p_35_30, radius_x=5, radius_y=5, sweep=True)
        self.add_contour('wheel-right', 'wheel-right-1', 'wheel-right-2', closed=True)
        self.relate("connect", 'bin', 'wheel-right')
        self.add_line('ground-1', p_13_40, p_35_40)
        self.add_contour('ground', 'ground-1', closed=False)
        self.relate("connect", 'ground', 'wheel-left')
        self.relate("connect", 'ground', 'wheel-right')
