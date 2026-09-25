'Mallet Hitting Wall.\n\nSymbol plan: Mallet striking wall with one attached impact tick; simplify detached debris.\nKeyshape: SQUARE; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4768b788-3969-4ac9-87d9-8a48474e5556'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_22/home improvement 7_4768b788-3969-4ac9-87d9-8a48474e5556.svg'
AUTHOR = 'gpt-6'

class MalletStrikingWall(Solo48):
    icon_id = 'mallet-striking-wall'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('mallet', 'striking', 'wall')

    def build(self):
        # Mallet striking wall with one attached impact tick; simplify detached debris.
        axis_x = 24
        p_6_6 = (6, 6)
        p_6_29 = (6, 29)
        p_6_42 = (6, 42)
        p_13_26 = (13, 26)
        p_19_13 = (19, 13)
        p_27_6 = (27, 6)
        p_32_27 = (32, 27)
        p_40_20 = (40, 20)
        p_42_42 = (2 * axis_x - p_6_42[0], p_6_42[1])
        self.add_line('wall-1', p_6_6, p_6_42)
        self.add_contour('wall', 'wall-1', closed=False)
        self.add_line('mallet-1', p_19_13, p_27_6)
        self.add_line('mallet-2', p_27_6, p_40_20)
        self.add_line('mallet-3', p_40_20, p_32_27)
        self.add_line('mallet-4', p_32_27, p_19_13)
        self.add_contour('mallet', 'mallet-1', 'mallet-2', 'mallet-3', 'mallet-4', closed=True)
        self.add_line('handle-1', p_32_27, p_42_42)
        self.add_contour('handle', 'handle-1', closed=False)
        self.relate("connect", 'mallet', 'handle')
        self.add_line('impact-1', p_6_29, p_13_26)
        self.add_contour('impact', 'impact-1', closed=False)
        self.relate("connect", 'wall', 'impact')
