'Partly Cloudy Weather Icon.\n\nSymbol plan: Low cloud and separated exposed sun arc. Reduce rays to one clean mark; preserve the partly cloudy reading.\nKeyshape: SQUARE; authored on SOLO48, not scaled from source.\nLucide: cloud-sun.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '20eefefc-3f3c-4bb4-97c0-4d668355ba60'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_36/sun cloud_20eefefc-3f3c-4bb4-97c0-4d668355ba60.svg'
AUTHOR = 'gpt-6'

class SunBehindCloud(Solo48):
    icon_id = 'sun-behind-cloud'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/reference'
    aliases = ()
    keywords = ('sun', 'behind', 'cloud')

    def build(self):
        # Low cloud and separated exposed sun arc. Reduce rays to one clean mark; preserve the partly cloudy reading.
        axis_x = 24
        p_6_14 = (6, 14)
        p_14_26 = (14, 26)
        p_14_42 = (14, 42)
        p_17_22 = (17, 22)
        p_22_14 = (22, 14)
        p_31_22 = (2 * axis_x - p_17_22[0], p_17_22[1])
        p_34_8 = (34, 8)
        p_34_26 = (2 * axis_x - p_14_26[0], p_14_26[1])
        p_34_42 = (2 * axis_x - p_14_42[0], p_14_42[1])
        self.add_arc('cloud-1', p_14_42, p_14_26, radius_x=8, radius_y=8, sweep=True)
        self.add_bezier('cloud-2', p_14_26, (p_17_22, p_31_22, p_34_26))
        self.add_arc('cloud-3', p_34_26, p_34_42, radius_x=8, radius_y=8, sweep=True)
        self.add_line('cloud-4', p_34_42, p_14_42)
        self.add_contour('cloud', 'cloud-1', 'cloud-2', 'cloud-3', 'cloud-4', closed=True)
        self.add_arc('sun-1', p_6_14, p_22_14, radius_x=8, radius_y=8, sweep=True)
        self.add_contour('sun', 'sun-1', closed=False)
        self.add_line('ray-1', p_34_8, p_34_8)
        self.add_contour('ray', 'ray-1', closed=False)
