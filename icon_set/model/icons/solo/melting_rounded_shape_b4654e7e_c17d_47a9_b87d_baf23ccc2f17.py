'Melting Circle Shape.\n\nSymbol plan: Rounded upper dome melting into unequal soft drips; no face or added symbol.\nKeyshape: VRECT_L; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b4654e7e-c17d-47a9-b87d-baf23ccc2f17'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_17/face melting_b4654e7e-c17d-47a9-b87d-baf23ccc2f17.svg'
AUTHOR = 'gpt-6'

class MeltingRoundedShape(Solo48):
    icon_id = 'melting-rounded-shape'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/reference'
    aliases = ()
    keywords = ('melting', 'rounded', 'shape')

    def build(self):
        # Rounded upper dome melting into unequal soft drips; no face or added symbol.
        axis_x = 24
        p_8_20 = (8, 20)
        p_8_32 = (8, 32)
        p_12_32 = (12, 32)
        p_12_39 = (12, 39)
        p_22_32 = (22, 32)
        p_22_38 = (22, 38)
        p_22_39 = (22, 39)
        p_22_42 = (22, 42)
        p_24_44 = (24, 44)
        p_27_44 = (27, 44)
        p_30_44 = (30, 44)
        p_32_33 = (32, 33)
        p_32_38 = (32, 38)
        p_32_39 = (32, 39)
        p_32_42 = (32, 42)
        p_40_20 = (2 * axis_x - p_8_20[0], p_8_20[1])
        p_40_33 = (40, 33)
        p_40_39 = (40, 39)
        self.add_arc('melt-1', p_8_20, p_40_20, radius_x=16, radius_y=16, sweep=True)
        self.add_line('melt-2', p_40_20, p_40_33)
        self.add_bezier('melt-3', p_40_33, (p_40_39, p_32_39, p_32_33))
        self.add_line('melt-4', p_32_33, p_32_38)
        self.add_bezier('melt-5', p_32_38, (p_32_42, p_30_44, p_27_44))
        self.add_bezier('melt-6', p_27_44, (p_24_44, p_22_42, p_22_38))
        self.add_line('melt-7', p_22_38, p_22_32)
        self.add_bezier('melt-8', p_22_32, (p_22_39, p_12_39, p_12_32))
        self.add_line('melt-9', p_12_32, p_8_32)
        self.add_line('melt-10', p_8_32, p_8_20)
        self.add_contour('melt', 'melt-1', 'melt-2', 'melt-3', 'melt-4', 'melt-5', 'melt-6', 'melt-7', 'melt-8', 'melt-9', 'melt-10', closed=True)
