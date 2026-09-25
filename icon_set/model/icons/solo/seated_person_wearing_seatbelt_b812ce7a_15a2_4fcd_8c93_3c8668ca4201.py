'Person Wearing Seatbelt.\n\nSymbol plan: Seated person with a wide diagonal belt and two legs. Belt stops at the shoulder and hip; omit redundant upper torso line under it.\nKeyshape: VRECT_L; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b812ce7a-15a2-4fcd-8c93-3c8668ca4201'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_18/fasten seal belt_b812ce7a-15a2-4fcd-8c93-3c8668ca4201.svg'
AUTHOR = 'gpt-6'

class SeatedPersonWearingSeatbelt(Solo48):
    icon_id = 'seated-person-wearing-seatbelt'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('seated', 'person', 'wearing', 'seatbelt')

    def build(self):
        # Seated person with a wide diagonal belt and two legs. Belt stops at the shoulder and hip; omit redundant upper torso line under it.
        axis_x = 24
        p_8_36 = (8, 36)
        p_12_22 = (12, 22)
        p_12_36 = (12, 36)
        p_12_38 = (12, 38)
        p_12_44 = (12, 44)
        p_19_9 = (19, 9)
        p_20_44 = (20, 44)
        p_24_22 = (24, 22)
        p_28_44 = (2 * axis_x - p_20_44[0], p_20_44[1])
        p_29_9 = (2 * axis_x - p_19_9[0], p_19_9[1])
        p_36_22 = (2 * axis_x - p_12_22[0], p_12_22[1])
        p_36_36 = (2 * axis_x - p_12_36[0], p_12_36[1])
        p_36_44 = (2 * axis_x - p_12_44[0], p_12_44[1])
        p_40_36 = (2 * axis_x - p_8_36[0], p_8_36[1])
        self.add_arc('head-1', p_19_9, p_29_9, radius_x=5, radius_y=5, sweep=True)
        self.add_arc('head-2', p_29_9, p_19_9, radius_x=5, radius_y=5, sweep=True)
        self.add_contour('head', 'head-1', 'head-2', closed=True)
        self.add_line('torso-1', p_24_22, p_12_22)
        self.add_line('torso-2', p_12_22, p_12_36)
        self.add_contour('torso', 'torso-1', 'torso-2', closed=False)
        self.add_line('right-1', p_24_22, p_36_22)
        self.add_line('right-2', p_36_22, p_36_36)
        self.add_contour('right', 'right-1', 'right-2', closed=False)
        self.relate("connect", 'torso', 'right')
        self.add_line('belt-1', p_36_22, p_12_38)
        self.add_contour('belt', 'belt-1', closed=False)
        self.relate("connect", 'belt', 'right')
        self.add_line('left-leg-1', p_12_36, p_12_38)
        self.add_line('left-leg-1-join-1', p_12_38, p_12_44)
        self.add_line('left-leg-2', p_12_44, p_20_44)
        self.add_contour('left-leg', 'left-leg-1', 'left-leg-1-join-1', 'left-leg-2', closed=False)
        self.add_line('right-leg-1', p_36_36, p_36_44)
        self.add_line('right-leg-2', p_36_44, p_28_44)
        self.add_contour('right-leg', 'right-leg-1', 'right-leg-2', closed=False)
        self.relate("connect", 'left-leg', 'torso')
        self.relate("connect", 'right-leg', 'right')
        self.relate("connect", 'belt', 'left-leg')
        self.add_line('seat-left-1', p_8_36, p_12_36)
        self.add_contour('seat-left', 'seat-left-1', closed=False)
        self.add_line('seat-right-1', p_36_36, p_40_36)
        self.add_contour('seat-right', 'seat-right-1', closed=False)
        self.relate("connect", 'seat-left', 'torso')
        self.relate("connect", 'seat-right', 'right')
