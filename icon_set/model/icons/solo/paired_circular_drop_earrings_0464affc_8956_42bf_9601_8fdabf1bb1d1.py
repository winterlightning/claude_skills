'Pair of Circular Drop Earrings.\n\nSymbol plan: Paired circular drop earrings with simple hooks; connector loops reduced to short stems.\nKeyshape: HRECT_L; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0464affc-8956-42bf-9601-8fdabf1bb1d1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_01/accessories earrings_0464affc-8956-42bf-9601-8fdabf1bb1d1.svg'
AUTHOR = 'gpt-6'

class PairedCircularDropEarrings(Solo48):
    icon_id = 'paired-circular-drop-earrings'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('paired', 'circular', 'drop', 'earrings')

    def build(self):
        # Paired circular drop earrings with simple hooks; connector loops reduced to short stems.
        axis_x = 24
        p_4_30 = (4, 30)
        p_6_8 = (6, 8)
        p_6_13 = (6, 13)
        p_14_8 = (14, 8)
        p_14_15 = (14, 15)
        p_14_20 = (14, 20)
        p_24_30 = (24, 30)
        p_26_8 = (26, 8)
        p_26_13 = (26, 13)
        p_34_8 = (2 * axis_x - p_14_8[0], p_14_8[1])
        p_34_15 = (2 * axis_x - p_14_15[0], p_14_15[1])
        p_34_20 = (2 * axis_x - p_14_20[0], p_14_20[1])
        p_44_30 = (2 * axis_x - p_4_30[0], p_4_30[1])
        self.add_arc('left-drop-1', p_4_30, p_24_30, radius_x=10, radius_y=10, sweep=True)
        self.add_arc('left-drop-2', p_24_30, p_4_30, radius_x=10, radius_y=10, sweep=True)
        self.add_contour('left-drop', 'left-drop-1', 'left-drop-2', closed=True)
        self.add_arc('right-drop-1', p_24_30, p_44_30, radius_x=10, radius_y=10, sweep=True)
        self.add_arc('right-drop-2', p_44_30, p_24_30, radius_x=10, radius_y=10, sweep=True)
        self.add_contour('right-drop', 'right-drop-1', 'right-drop-2', closed=True)
        self.relate("connect", 'left-drop', 'right-drop')
        self.add_line('hook-14-1', p_14_20, p_14_15)
        self.add_bezier('hook-14-2', p_14_15, (p_6_13, p_6_8, p_14_8))
        self.add_contour('hook-14', 'hook-14-1', 'hook-14-2', closed=False)
        self.add_line('hook-34-1', p_34_20, p_34_15)
        self.add_bezier('hook-34-2', p_34_15, (p_26_13, p_26_8, p_34_8))
        self.add_contour('hook-34', 'hook-34-1', 'hook-34-2', closed=False)
        self.relate("connect", 'left-drop', 'hook-14')
        self.relate("connect", 'right-drop', 'hook-34')
