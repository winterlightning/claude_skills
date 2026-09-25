'Partly Sunny Snow Thunderstorm.\n\nSymbol plan: Snow thunderstorm with exposed sun and an open cloud base around the lightning; preserve both snow dots.\nKeyshape: SQUARE; authored on SOLO48, not scaled from source.\nLucide: cloud-sun.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd3f2158b-1711-402f-9758-99a2682ee0d0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_40/weather snow thunder_d3f2158b-1711-402f-9758-99a2682ee0d0.svg'
AUTHOR = 'gpt-6'

class SunSnowThunderstorm(Solo48):
    icon_id = 'sun-snow-thunderstorm'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('sun', 'snow', 'thunderstorm')

    def build(self):
        # Snow thunderstorm with exposed sun and an open cloud base around the lightning; preserve both snow dots.
        axis_x = 24
        p_6_6 = (6, 6)
        p_6_14 = (6, 14)
        p_6_16 = (6, 16)
        p_6_20 = (6, 20)
        p_6_24 = (6, 24)
        p_6_27 = (6, 27)
        p_7_41 = (7, 41)
        p_10_14 = (10, 14)
        p_10_27 = (10, 27)
        p_14_4 = (14, 4)
        p_14_14 = (14, 14)
        p_15_6 = (15, 6)
        p_18_33 = (18, 33)
        p_23_42 = (23, 42)
        p_27_23 = (27, 23)
        p_31_33 = (31, 33)
        p_34_4 = (2 * axis_x - p_14_4[0], p_14_4[1])
        p_34_15 = (34, 15)
        p_41_41 = (2 * axis_x - p_7_41[0], p_7_41[1])
        p_42_15 = (42, 15)
        p_42_22 = (42, 22)
        p_42_26 = (42, 26)
        self.add_bezier('cloud-1', p_10_27, (p_6_27, p_6_24, p_6_20))
        self.add_bezier('cloud-2', p_6_20, (p_6_16, p_10_14, p_14_14))
        self.add_bezier('cloud-3', p_14_14, (p_14_4, p_34_4, p_34_15))
        self.add_bezier('cloud-4', p_34_15, (p_42_15, p_42_22, p_42_26))
        self.add_contour('cloud', 'cloud-1', 'cloud-2', 'cloud-3', 'cloud-4', closed=False)
        self.add_bezier('sun-1', p_14_14, (p_6_14, p_6_6, p_15_6))
        self.add_contour('sun', 'sun-1', closed=False)
        self.relate("connect", 'sun', 'cloud')
        self.add_line('bolt-1', p_27_23, p_18_33)
        self.add_line('bolt-2', p_18_33, p_31_33)
        self.add_line('bolt-3', p_31_33, p_23_42)
        self.add_contour('bolt', 'bolt-1', 'bolt-2', 'bolt-3', closed=False)
        self.add_line('snow-left-1', p_7_41, p_7_41)
        self.add_contour('snow-left', 'snow-left-1', closed=False)
        self.add_line('snow-right-1', p_41_41, p_41_41)
        self.add_contour('snow-right', 'snow-right-1', closed=False)
