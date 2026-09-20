'Modern Residential Building.\n\nSymbol plan: Two tall rectangular volumes behind a sloping front roof and centered door; separate roof heights by eight units.\nKeyshape: SQUARE; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f838033b-f187-47d4-a716-74d08a735e33'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_25/loft_f838033b-f187-47d4-a716-74d08a735e33.svg'
AUTHOR = 'gpt-6'

class LoftBuilding(Solo48):
    icon_id = 'loft-building'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/reference'
    aliases = ()
    keywords = ('loft', 'building')

    def build(self):
        # Two tall rectangular volumes behind a sloping front roof and centered door; separate roof heights by eight units.
        axis_x = 24
        p_6_32 = (6, 32)
        p_6_42 = (6, 42)
        p_10_6 = (10, 6)
        p_10_29 = (10, 29)
        p_20_24 = (20, 24)
        p_22_33 = (22, 33)
        p_22_42 = (22, 42)
        p_28_6 = (28, 6)
        p_28_16 = (28, 16)
        p_28_24 = (2 * axis_x - p_20_24[0], p_20_24[1])
        p_32_33 = (32, 33)
        p_32_42 = (32, 42)
        p_42_16 = (42, 16)
        p_42_24 = (42, 24)
        p_42_42 = (2 * axis_x - p_6_42[0], p_6_42[1])
        self.add_line('front-1', p_6_32, p_20_24)
        self.add_line('front-2', p_20_24, p_42_24)
        self.add_line('front-3', p_42_24, p_42_42)
        self.add_line('front-4', p_42_42, p_6_42)
        self.add_line('front-5', p_6_42, p_6_32)
        self.add_contour('front', 'front-1', 'front-2', 'front-3', 'front-4', 'front-5', closed=True)
        self.add_line('rear-left-1', p_10_29, p_10_6)
        self.add_line('rear-left-2', p_10_6, p_28_6)
        self.add_line('rear-left-3', p_28_6, p_28_24)
        self.add_contour('rear-left', 'rear-left-1', 'rear-left-2', 'rear-left-3', closed=False)
        self.relate("connect", 'front', 'rear-left')
        self.add_line('rear-right-1', p_28_16, p_42_16)
        self.add_line('rear-right-2', p_42_16, p_42_24)
        self.add_contour('rear-right', 'rear-right-1', 'rear-right-2', closed=False)
        self.relate("connect", 'rear-right', 'rear-left')
        self.relate("connect", 'rear-right', 'front')
        self.add_line('door-1', p_22_42, p_22_33)
        self.add_line('door-2', p_22_33, p_32_33)
        self.add_line('door-3', p_32_33, p_32_42)
        self.add_contour('door', 'door-1', 'door-2', 'door-3', closed=False)
        self.relate("connect", 'front', 'door')
