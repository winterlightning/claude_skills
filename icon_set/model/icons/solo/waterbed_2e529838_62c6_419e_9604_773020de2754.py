'Mattress with Water Waves.\n\nSymbol plan: Rounded waterbed with one smooth waterline through the middle.\nKeyshape: HRECT_L; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2e529838-62c6-419e-9604-773020de2754'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_40/waterbed_2e529838-62c6-419e-9604-773020de2754.svg'
AUTHOR = 'gpt-6'

class Waterbed(Solo48):
    icon_id = 'waterbed'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('waterbed',)

    def build(self):
        # Rounded waterbed with one smooth waterline through the middle.
        axis_x = 24
        p_4_16 = (4, 16)
        p_4_24 = (4, 24)
        p_4_32 = (4, 32)
        p_11_17 = (11, 17)
        p_12_8 = (12, 8)
        p_12_40 = (12, 40)
        p_17_31 = (17, 31)
        p_24_24 = (24, 24)
        p_31_17 = (31, 17)
        p_36_8 = (2 * axis_x - p_12_8[0], p_12_8[1])
        p_36_40 = (2 * axis_x - p_12_40[0], p_12_40[1])
        p_37_31 = (37, 31)
        p_44_16 = (2 * axis_x - p_4_16[0], p_4_16[1])
        p_44_24 = (2 * axis_x - p_4_24[0], p_4_24[1])
        p_44_32 = (2 * axis_x - p_4_32[0], p_4_32[1])
        self.add_line('bed-1', p_12_8, p_36_8)
        self.add_arc('bed-2', p_36_8, p_44_16, radius_x=8, radius_y=8, sweep=True)
        self.add_line('bed-3', p_44_16, p_44_32)
        self.add_arc('bed-4', p_44_32, p_36_40, radius_x=8, radius_y=8, sweep=True)
        self.add_line('bed-5', p_36_40, p_12_40)
        self.add_arc('bed-6', p_12_40, p_4_32, radius_x=8, radius_y=8, sweep=True)
        self.add_line('bed-7', p_4_32, p_4_16)
        self.add_arc('bed-8', p_4_16, p_12_8, radius_x=8, radius_y=8, sweep=True)
        self.add_contour('bed', 'bed-1', 'bed-2', 'bed-3', 'bed-4', 'bed-5', 'bed-6', 'bed-7', 'bed-8', closed=True)
        self.add_bezier('water-1', p_4_24, (p_11_17, p_17_31, p_24_24))
        self.add_bezier('water-2', p_24_24, (p_31_17, p_37_31, p_44_24))
        self.add_contour('water', 'water-1', 'water-2', closed=False)
        self.relate("connect", 'bed', 'water')
