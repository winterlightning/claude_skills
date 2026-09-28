'Marketplace Storefront with Awning.\n\nSymbol plan: Storefront with three scalloped awning segments and central door.\nKeyshape: SQUARE; authored on SOLO48, not scaled from source.\nLucide: store.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8a142829-c797-44e6-bde7-efc15341b72d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_36/store_8a142829-c797-44e6-bde7-efc15341b72d.svg'
AUTHOR = 'gpt-6'

class Storefront(Solo48):
    icon_id = 'storefront'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/reference'
    aliases = ()
    keywords = ('storefront',)

    def build(self):
        # Storefront with three scalloped awning segments and central door.
        axis_x = 24
        p_6_18 = (6, 18)
        p_8_24 = (8, 24)
        p_8_42 = (8, 42)
        p_12_6 = (12, 6)
        p_18_18 = (18, 18)
        p_19_32 = (19, 32)
        p_19_42 = (19, 42)
        p_29_32 = (2 * axis_x - p_19_32[0], p_19_32[1])
        p_29_42 = (2 * axis_x - p_19_42[0], p_19_42[1])
        p_30_18 = (2 * axis_x - p_18_18[0], p_18_18[1])
        p_36_6 = (2 * axis_x - p_12_6[0], p_12_6[1])
        p_40_24 = (2 * axis_x - p_8_24[0], p_8_24[1])
        p_40_42 = (2 * axis_x - p_8_42[0], p_8_42[1])
        p_42_18 = (2 * axis_x - p_6_18[0], p_6_18[1])
        self.add_line('awning-1', p_6_18, p_12_6)
        self.add_line('awning-2', p_12_6, p_36_6)
        self.add_line('awning-3', p_36_6, p_42_18)
        self.add_arc('awning-4', p_42_18, p_30_18, radius_x=6, radius_y=6, sweep=True)
        self.add_arc('awning-5', p_30_18, p_18_18, radius_x=6, radius_y=6, sweep=True)
        self.add_arc('awning-6', p_18_18, p_6_18, radius_x=6, radius_y=6, sweep=True)
        self.add_contour('awning', 'awning-1', 'awning-2', 'awning-3', 'awning-4', 'awning-5', 'awning-6', closed=True)
        self.add_line('shop-1', p_8_24, p_8_42)
        self.add_line('shop-2', p_8_42, p_40_42)
        self.add_line('shop-3', p_40_42, p_40_24)
        self.add_contour('shop', 'shop-1', 'shop-2', 'shop-3', closed=False)
        self.relate("connect", 'shop', 'awning')
        self.add_line('door-1', p_19_42, p_19_32)
        self.add_line('door-2', p_19_32, p_29_32)
        self.add_line('door-3', p_29_32, p_29_42)
        self.add_contour('door', 'door-1', 'door-2', 'door-3', closed=False)
        self.relate("connect", 'shop', 'door')
