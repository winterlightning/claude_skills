'Octopus Tentacle with Suction Cups.\n\nSymbol plan: Hooked S-curved tentacle with one enlarged lower suction cup. Reduce small upper cups to preserve required interior space.\nKeyshape: VRECT_L; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '018d0241-c9aa-4b9f-9a26-4d7323b9cbc6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_37/tentacle_018d0241-c9aa-4b9f-9a26-4d7323b9cbc6.svg'
AUTHOR = 'gpt-6'

class OctopusTentacle(Solo48):
    icon_id = 'octopus-tentacle'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('octopus', 'tentacle')

    def build(self):
        # Hooked S-curved tentacle with one enlarged lower suction cup. Reduce small upper cups to preserve required interior space.
        axis_x = 24
        p_8_24 = (8, 24)
        p_8_38 = (8, 38)
        p_8_44 = (8, 44)
        p_17_39 = (17, 39)
        p_23_39 = (23, 39)
        p_26_4 = (26, 4)
        p_28_6 = (28, 6)
        p_29_8 = (29, 8)
        p_29_13 = (29, 13)
        p_29_25 = (29, 25)
        p_32_32 = (32, 32)
        p_32_38 = (32, 38)
        p_32_44 = (32, 44)
        p_35_4 = (35, 4)
        p_40_10 = (40, 10)
        p_40_18 = (40, 18)
        p_40_28 = (40, 28)
        self.add_line('tentacle-1', p_8_44, p_8_38)
        self.add_bezier('tentacle-2', p_8_38, (p_8_24, p_29_25, p_29_13))
        self.add_bezier('tentacle-3', p_29_13, (p_29_8, p_28_6, p_26_4))
        self.add_bezier('tentacle-4', p_26_4, (p_35_4, p_40_10, p_40_18))
        self.add_bezier('tentacle-5', p_40_18, (p_40_28, p_32_32, p_32_38))
        self.add_line('tentacle-6', p_32_38, p_32_44)
        self.add_contour('tentacle', 'tentacle-1', 'tentacle-2', 'tentacle-3', 'tentacle-4', 'tentacle-5', 'tentacle-6', closed=False)
        self.add_arc('cup-1', p_17_39, p_23_39, radius_x=3, radius_y=3, sweep=True)
        self.add_arc('cup-2', p_23_39, p_17_39, radius_x=3, radius_y=3, sweep=True)
        self.add_contour('cup', 'cup-1', 'cup-2', closed=True)
