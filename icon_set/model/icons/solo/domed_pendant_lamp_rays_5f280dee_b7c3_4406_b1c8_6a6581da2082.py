'Illuminated Pendant Ceiling Lamp.\n\nSymbol plan: Pendant cap, domed shade, exposed bulb and three rays; shared shade junctions retain physical attachment. Simplify mounting cap to a short suspension stem.\nKeyshape: SQUARE; authored on SOLO48, not scaled from source.\nLucide: lamp-ceiling.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5f280dee-b7c3-4406-b1c8-6a6581da2082'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_37/sunlamp_5f280dee-b7c3-4406-b1c8-6a6581da2082.svg'
AUTHOR = 'gpt-6'

class DomedPendantLampRays(Solo48):
    icon_id = 'domed-pendant-lamp-rays'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/reference'
    aliases = ()
    keywords = ('domed', 'pendant', 'lamp', 'rays')

    def build(self):
        # Pendant cap, domed shade, exposed bulb and three rays; shared shade junctions retain physical attachment. Simplify mounting cap to a short suspension stem.
        axis_x = 24
        p_6_26 = (6, 26)
        p_6_37 = (6, 37)
        p_8_35 = (8, 35)
        p_16_26 = (16, 26)
        p_24_6 = (24, 6)
        p_24_12 = (24, 12)
        p_24_42 = (24, 42)
        p_32_26 = (2 * axis_x - p_16_26[0], p_16_26[1])
        p_40_35 = (2 * axis_x - p_8_35[0], p_8_35[1])
        p_42_26 = (2 * axis_x - p_6_26[0], p_6_26[1])
        p_42_37 = (2 * axis_x - p_6_37[0], p_6_37[1])
        self.add_arc('shade-1', p_6_26, p_24_12, radius_x=18, radius_y=14, sweep=True)
        self.add_arc('shade-2', p_24_12, p_42_26, radius_x=18, radius_y=14, sweep=True)
        self.add_line('shade-3', p_42_26, p_32_26)
        self.add_line('shade-4', p_32_26, p_16_26)
        self.add_line('shade-5', p_16_26, p_6_26)
        self.add_contour('shade', 'shade-1', 'shade-2', 'shade-3', 'shade-4', 'shade-5', closed=True)
        self.add_line('suspension-1', p_24_6, p_24_12)
        self.add_contour('suspension', 'suspension-1', closed=False)
        self.relate("connect", 'shade', 'suspension')
        self.add_arc('bulb-1', p_32_26, p_16_26, radius_x=8, radius_y=8, sweep=True)
        self.add_contour('bulb', 'bulb-1', closed=False)
        self.relate("connect", 'shade', 'bulb')
        self.add_line('ray-mid-1', p_24_42, p_24_42)
        self.add_contour('ray-mid', 'ray-mid-1', closed=False)
        self.add_line('ray-left-1', p_6_37, p_8_35)
        self.add_contour('ray-left', 'ray-left-1', closed=False)
        self.add_line('ray-right-1', p_40_35, p_42_37)
        self.add_contour('ray-right', 'ray-right-1', closed=False)
