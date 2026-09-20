'Minimalist Rounded Seat Stool.\n\nSymbol plan: Rounded capsule seat on two splayed legs and a single horizontal brace.\nKeyshape: HRECT_L; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '62a706b6-8a7c-48d7-a60b-2cac9a19049d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_36/stool_62a706b6-8a7c-48d7-a60b-2cac9a19049d.svg'
AUTHOR = 'gpt-6'

class Stool(Solo48):
    icon_id = 'stool'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/reference'
    aliases = ()
    keywords = ('stool',)

    def build(self):
        # Rounded capsule seat on two splayed legs and a single horizontal brace.
        axis_x = 24
        p_4_13 = (4, 13)
        p_8_40 = (8, 40)
        p_9_8 = (9, 8)
        p_9_18 = (9, 18)
        p_10_29 = (10, 29)
        p_12_18 = (12, 18)
        p_36_18 = (2 * axis_x - p_12_18[0], p_12_18[1])
        p_38_29 = (2 * axis_x - p_10_29[0], p_10_29[1])
        p_39_8 = (2 * axis_x - p_9_8[0], p_9_8[1])
        p_39_18 = (2 * axis_x - p_9_18[0], p_9_18[1])
        p_40_40 = (2 * axis_x - p_8_40[0], p_8_40[1])
        p_44_13 = (2 * axis_x - p_4_13[0], p_4_13[1])
        self.add_line('seat-1', p_9_8, p_39_8)
        self.add_arc('seat-2', p_39_8, p_44_13, radius_x=5, radius_y=5, sweep=True)
        self.add_line('seat-3', p_44_13, p_44_13)
        self.add_arc('seat-4', p_44_13, p_39_18, radius_x=5, radius_y=5, sweep=True)
        self.add_line('seat-5', p_39_18, p_9_18)
        self.add_arc('seat-6', p_9_18, p_4_13, radius_x=5, radius_y=5, sweep=True)
        self.add_line('seat-7', p_4_13, p_4_13)
        self.add_arc('seat-8', p_4_13, p_9_8, radius_x=5, radius_y=5, sweep=True)
        self.add_contour('seat', 'seat-1', 'seat-2', 'seat-3', 'seat-4', 'seat-5', 'seat-6', 'seat-7', 'seat-8', closed=True)
        self.add_line('left-leg-1', p_12_18, p_8_40)
        self.add_contour('left-leg', 'left-leg-1', closed=False)
        self.relate("connect", 'seat', 'left-leg')
        self.add_line('right-leg-1', p_36_18, p_40_40)
        self.add_contour('right-leg', 'right-leg-1', closed=False)
        self.relate("connect", 'seat', 'right-leg')
        self.add_line('brace-1', p_10_29, p_38_29)
        self.add_contour('brace', 'brace-1', closed=False)
        self.relate("connect", 'brace', 'left-leg')
        self.relate("connect", 'brace', 'right-leg')
