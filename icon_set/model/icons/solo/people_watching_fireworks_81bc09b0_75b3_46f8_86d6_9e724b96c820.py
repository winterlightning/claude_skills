'People Watching Fireworks Display.\n\nSymbol plan: Three equal spectators beneath a large firework; compact circular heads and open shoulders retain the crowd. Exact detached gap is 4 units.\nKeyshape: SQUARE; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '81bc09b0-75b3-46f8-86d6-9e724b96c820'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_19/fireworks people watch_81bc09b0-75b3-46f8-86d6-9e724b96c820.svg'
AUTHOR = 'gpt-6'

class PeopleWatchingFireworks(Solo48):
    icon_id = 'people-watching-fireworks'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('people', 'watching', 'fireworks')

    def build(self):
        # Three equal spectators beneath a large firework; compact circular heads and open shoulders retain the crowd. Exact detached gap is 4 units.
        axis_x = 24
        p_6_28 = (6, 28)
        p_6_39 = (6, 39)
        p_6_42 = (6, 42)
        p_7_39 = (7, 39)
        p_9_39 = (9, 39)
        p_10_10 = (10, 10)
        p_11_39 = (11, 39)
        p_12_28 = (12, 28)
        p_12_39 = (12, 39)
        p_12_42 = (12, 42)
        p_15_16 = (15, 16)
        p_21_28 = (21, 28)
        p_21_39 = (21, 39)
        p_21_42 = (21, 42)
        p_22_39 = (22, 39)
        p_24_6 = (24, 6)
        p_24_14 = (24, 14)
        p_24_39 = (24, 39)
        p_26_39 = (2 * axis_x - p_22_39[0], p_22_39[1])
        p_27_28 = (2 * axis_x - p_21_28[0], p_21_28[1])
        p_27_39 = (2 * axis_x - p_21_39[0], p_21_39[1])
        p_27_42 = (2 * axis_x - p_21_42[0], p_21_42[1])
        p_33_16 = (2 * axis_x - p_15_16[0], p_15_16[1])
        p_36_28 = (2 * axis_x - p_12_28[0], p_12_28[1])
        p_36_39 = (2 * axis_x - p_12_39[0], p_12_39[1])
        p_36_42 = (2 * axis_x - p_12_42[0], p_12_42[1])
        p_37_39 = (2 * axis_x - p_11_39[0], p_11_39[1])
        p_38_10 = (2 * axis_x - p_10_10[0], p_10_10[1])
        p_39_39 = (2 * axis_x - p_9_39[0], p_9_39[1])
        p_41_39 = (2 * axis_x - p_7_39[0], p_7_39[1])
        p_42_28 = (2 * axis_x - p_6_28[0], p_6_28[1])
        p_42_39 = (2 * axis_x - p_6_39[0], p_6_39[1])
        p_42_42 = (2 * axis_x - p_6_42[0], p_6_42[1])
        self.add_arc('head9-1', p_6_28, p_12_28, radius_x=3, radius_y=3, sweep=True)
        self.add_arc('head9-2', p_12_28, p_6_28, radius_x=3, radius_y=3, sweep=True)
        self.add_contour('head9', 'head9-1', 'head9-2', closed=True)
        self.add_bezier('body9-1', p_6_42, (p_6_39, p_7_39, p_9_39))
        self.add_bezier('body9-2', p_9_39, (p_11_39, p_12_39, p_12_42))
        self.add_contour('body9', 'body9-1', 'body9-2', closed=False)
        self.add_arc('head24-1', p_21_28, p_27_28, radius_x=3, radius_y=3, sweep=True)
        self.add_arc('head24-2', p_27_28, p_21_28, radius_x=3, radius_y=3, sweep=True)
        self.add_contour('head24', 'head24-1', 'head24-2', closed=True)
        self.add_bezier('body24-1', p_21_42, (p_21_39, p_22_39, p_24_39))
        self.add_bezier('body24-2', p_24_39, (p_26_39, p_27_39, p_27_42))
        self.add_contour('body24', 'body24-1', 'body24-2', closed=False)
        self.add_arc('head39-1', p_36_28, p_42_28, radius_x=3, radius_y=3, sweep=True)
        self.add_arc('head39-2', p_42_28, p_36_28, radius_x=3, radius_y=3, sweep=True)
        self.add_contour('head39', 'head39-1', 'head39-2', closed=True)
        self.add_bezier('body39-1', p_36_42, (p_36_39, p_37_39, p_39_39))
        self.add_bezier('body39-2', p_39_39, (p_41_39, p_42_39, p_42_42))
        self.add_contour('body39', 'body39-1', 'body39-2', closed=False)
        self.add_line('burst-1', p_24_6, p_24_14)
        self.add_contour('burst', 'burst-1', closed=False)
        self.add_line('burst-l-1', p_10_10, p_15_16)
        self.add_contour('burst-l', 'burst-l-1', closed=False)
        self.add_line('burst-r-1', p_38_10, p_33_16)
        self.add_contour('burst-r', 'burst-r-1', closed=False)
