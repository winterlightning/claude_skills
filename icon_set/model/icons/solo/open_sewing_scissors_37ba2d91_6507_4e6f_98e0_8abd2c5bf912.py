'Open Sewing Scissors.\n\nSymbol plan: Open scissors with two spaced circular finger loops, crossing blades and asymmetric blade tips. Reduce doubled blade outlines to single strokes.\nKeyshape: SQUARE; authored on SOLO48, not scaled from source.\nLucide: scissors.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '37ba2d91-6507-4e6f-98e0-8abd2c5bf912'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_37/thread cutter_37ba2d91-6507-4e6f-98e0-8abd2c5bf912.svg'
AUTHOR = 'gpt-6'

class OpenSewingScissors(Solo48):
    icon_id = 'open-sewing-scissors'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/reference'
    aliases = ()
    keywords = ('open', 'sewing', 'scissors')

    def build(self):
        # Open scissors with two spaced circular finger loops, crossing blades and asymmetric blade tips. Reduce doubled blade outlines to single strokes.
        axis_x = 24
        p_6_20 = (6, 20)
        p_18_20 = (18, 20)
        p_20_36 = (20, 36)
        p_26_22 = (26, 22)
        p_26_30 = (26, 30)
        p_32_36 = (32, 36)
        p_35_6 = (35, 6)
        p_42_12 = (42, 12)
        self.add_arc('loop-left-1', p_6_20, p_18_20, radius_x=6, radius_y=6, sweep=True)
        self.add_arc('loop-left-2', p_18_20, p_6_20, radius_x=6, radius_y=6, sweep=True)
        self.add_contour('loop-left', 'loop-left-1', 'loop-left-2', closed=True)
        self.add_arc('loop-bottom-1', p_20_36, p_32_36, radius_x=6, radius_y=6, sweep=True)
        self.add_arc('loop-bottom-2', p_32_36, p_20_36, radius_x=6, radius_y=6, sweep=True)
        self.add_contour('loop-bottom', 'loop-bottom-1', 'loop-bottom-2', closed=True)
        self.add_line('blade-up-1', p_18_20, p_26_22)
        self.add_line('blade-up-2', p_26_22, p_35_6)
        self.add_contour('blade-up', 'blade-up-1', 'blade-up-2', closed=False)
        self.relate("connect", 'blade-up', 'loop-left')
        self.add_line('blade-right-1', p_26_30, p_26_22)
        self.add_line('blade-right-2', p_26_22, p_42_12)
        self.add_contour('blade-right', 'blade-right-1', 'blade-right-2', closed=False)
        self.relate("connect", 'blade-right', 'loop-bottom')
        self.relate("connect", 'blade-up', 'blade-right')
