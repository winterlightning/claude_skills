'Ocean Surf Wave.\n\nSymbol plan: Breaking wave curls right above two parallel surface lines. Smooth crest and hollow interior.\nKeyshape: HRECT_L; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4cda8818-22b4-41e5-a535-794d524fae3f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_37/tide_4cda8818-22b4-41e5-a535-794d524fae3f.svg'
AUTHOR = 'gpt-6'

class BreakingOceanWave(Solo48):
    icon_id = 'breaking-ocean-wave'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/reference'
    aliases = ()
    keywords = ('breaking', 'ocean', 'wave')

    def build(self):
        # Breaking wave curls right above two parallel surface lines. Smooth crest and hollow interior.
        axis_x = 24
        p_4_24 = (4, 24)
        p_4_32 = (4, 32)
        p_4_40 = (4, 40)
        p_12_24 = (12, 24)
        p_14_8 = (14, 8)
        p_22_24 = (22, 24)
        p_25_10 = (25, 10)
        p_26_8 = (26, 8)
        p_34_8 = (2 * axis_x - p_14_8[0], p_14_8[1])
        p_34_24 = (34, 24)
        p_38_12 = (38, 12)
        p_38_16 = (38, 16)
        p_44_24 = (2 * axis_x - p_4_24[0], p_4_24[1])
        p_44_32 = (2 * axis_x - p_4_32[0], p_4_32[1])
        p_44_40 = (2 * axis_x - p_4_40[0], p_4_40[1])
        self.add_bezier('wave-1', p_4_24, (p_12_24, p_14_8, p_26_8))
        self.add_bezier('wave-2', p_26_8, (p_34_8, p_38_12, p_38_16))
        self.add_bezier('wave-3', p_38_16, (p_25_10, p_22_24, p_34_24))
        self.add_line('wave-4', p_34_24, p_44_24)
        self.add_contour('wave', 'wave-1', 'wave-2', 'wave-3', 'wave-4', closed=False)
        self.add_line('water-middle-1', p_4_32, p_44_32)
        self.add_contour('water-middle', 'water-middle-1', closed=False)
        self.add_line('water-bottom-1', p_4_40, p_44_40)
        self.add_contour('water-bottom', 'water-bottom-1', closed=False)
