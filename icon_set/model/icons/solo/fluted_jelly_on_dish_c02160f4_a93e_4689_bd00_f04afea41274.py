'Molded Gelatin Jelly Dessert.\n\nSymbol plan: Fluted jelly with three rounded top lobes and two vertical ribs on a shallow serving dish.\nKeyshape: HRECT_L; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c02160f4-a93e-4689-bd00-f04afea41274'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_23/jelly_c02160f4-a93e-4689-bd00-f04afea41274.svg'
AUTHOR = 'gpt-6'

class FlutedJellyOnDish(Solo48):
    icon_id = 'fluted-jelly-on-dish'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/reference'
    aliases = ()
    keywords = ('fluted', 'jelly', 'on', 'dish')

    def build(self):
        # Fluted jelly with three rounded top lobes and two vertical ribs on a shallow serving dish.
        axis_x = 24
        p_4_30 = (4, 30)
        p_4_40 = (4, 40)
        p_7_30 = (7, 30)
        p_10_15 = (10, 15)
        p_11_6 = (11, 6)
        p_12_40 = (12, 40)
        p_18_30 = (18, 30)
        p_19_8 = (19, 8)
        p_20_11 = (20, 11)
        p_21_7 = (21, 7)
        p_24_40 = (24, 40)
        p_27_7 = (2 * axis_x - p_21_7[0], p_21_7[1])
        p_28_11 = (2 * axis_x - p_20_11[0], p_20_11[1])
        p_29_8 = (2 * axis_x - p_19_8[0], p_19_8[1])
        p_30_30 = (2 * axis_x - p_18_30[0], p_18_30[1])
        p_36_40 = (2 * axis_x - p_12_40[0], p_12_40[1])
        p_37_6 = (2 * axis_x - p_11_6[0], p_11_6[1])
        p_38_15 = (2 * axis_x - p_10_15[0], p_10_15[1])
        p_41_30 = (2 * axis_x - p_7_30[0], p_7_30[1])
        p_44_30 = (2 * axis_x - p_4_30[0], p_4_30[1])
        p_44_40 = (2 * axis_x - p_4_40[0], p_4_40[1])
        self.add_line('jelly-1', p_7_30, p_10_15)
        self.add_bezier('jelly-2', p_10_15, (p_11_6, p_19_8, p_20_11))
        self.add_bezier('jelly-3', p_20_11, (p_21_7, p_27_7, p_28_11))
        self.add_bezier('jelly-4', p_28_11, (p_29_8, p_37_6, p_38_15))
        self.add_line('jelly-5', p_38_15, p_41_30)
        self.add_contour('jelly', 'jelly-1', 'jelly-2', 'jelly-3', 'jelly-4', 'jelly-5', closed=False)
        self.add_line('dish-1', p_4_30, p_44_30)
        self.add_bezier('dish-2', p_44_30, (p_44_40, p_36_40, p_24_40))
        self.add_bezier('dish-3', p_24_40, (p_12_40, p_4_40, p_4_30))
        self.add_contour('dish', 'dish-1', 'dish-2', 'dish-3', closed=True)
        self.relate("connect", 'jelly', 'dish')
        self.add_line('rib-left-1', p_20_11, p_18_30)
        self.add_contour('rib-left', 'rib-left-1', closed=False)
        self.relate("connect", 'rib-left', 'jelly')
        self.relate("connect", 'rib-left', 'dish')
        self.add_line('rib-right-1', p_28_11, p_30_30)
        self.add_contour('rib-right', 'rib-right-1', closed=False)
        self.relate("connect", 'rib-right', 'jelly')
        self.relate("connect", 'rib-right', 'dish')
