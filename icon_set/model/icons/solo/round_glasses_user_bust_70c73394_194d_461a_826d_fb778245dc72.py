'Person with glasses.\n\nSymbol plan: Round-glasses avatar. The spectacle lenses replace the occluded upper face line; circular lower jaw and touching shoulders remain.\nKeyshape: VRECT_L; authored on SOLO48, not scaled from source.\nLucide: glasses.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '70c73394-194d-461a-826d-fb778245dc72'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_17/expert_70c73394-194d-461a-826d-fb778245dc72.svg'
AUTHOR = 'gpt-6'

class RoundGlassesUserBust(Solo48):
    icon_id = 'round-glasses-user-bust'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('round', 'glasses', 'user', 'bust')

    def build(self):
        # Round-glasses avatar. The spectacle lenses replace the occluded upper face line; circular lower jaw and touching shoulders remain.
        axis_x = 24
        p_8_12 = (8, 12)
        p_8_20 = (8, 20)
        p_8_44 = (8, 44)
        p_24_12 = (24, 12)
        p_24_40 = (24, 40)
        p_40_12 = (2 * axis_x - p_8_12[0], p_8_12[1])
        p_40_20 = (2 * axis_x - p_8_20[0], p_8_20[1])
        p_40_44 = (2 * axis_x - p_8_44[0], p_8_44[1])
        self.add_arc('head-1', p_8_20, p_40_20, radius_x=16, radius_y=16, sweep=False)
        self.add_contour('head', 'head-1', closed=False)
        self.add_arc('body-1', p_8_44, p_24_40, radius_x=16, radius_y=4, sweep=True)
        self.add_arc('body-2', p_24_40, p_40_44, radius_x=16, radius_y=4, sweep=True)
        self.add_contour('body', 'body-1', 'body-2', closed=False)
        self.relate("connect", 'head', 'body')
        self.add_arc('left-lens-1', p_8_12, p_24_12, radius_x=8, radius_y=8, sweep=True)
        self.add_arc('left-lens-2', p_24_12, p_8_12, radius_x=8, radius_y=8, sweep=True)
        self.add_contour('left-lens', 'left-lens-1', 'left-lens-2', closed=True)
        self.add_arc('right-lens-1', p_24_12, p_40_12, radius_x=8, radius_y=8, sweep=True)
        self.add_arc('right-lens-2', p_40_12, p_24_12, radius_x=8, radius_y=8, sweep=True)
        self.add_contour('right-lens', 'right-lens-1', 'right-lens-2', closed=True)
        self.relate("connect", 'left-lens', 'right-lens')
        self.add_line('temple-left-1', p_8_12, p_8_20)
        self.add_contour('temple-left', 'temple-left-1', closed=False)
        self.add_line('temple-right-1', p_40_12, p_40_20)
        self.add_contour('temple-right', 'temple-right-1', closed=False)
        self.relate("connect", 'temple-left', 'head')
        self.relate("connect", 'temple-left', 'left-lens')
        self.relate("connect", 'temple-right', 'head')
        self.relate("connect", 'temple-right', 'right-lens')
