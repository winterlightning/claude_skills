'Pair of Handcuffs.\n\nSymbol plan: Two cuffs hang from a shared upper ring; narrow connectors and doubled cuff walls simplified to single structural strokes.\nKeyshape: SQUARE; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7c088e36-de93-4207-ba03-087b8bb9a1a3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_18/fantasy medieval bounty hunter 2_7c088e36-de93-4207-ba03-087b8bb9a1a3.svg'
AUTHOR = 'gpt-6'

class LinkedCircularHandcuffs(Solo48):
    icon_id = 'linked-circular-handcuffs'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/reference'
    aliases = ()
    keywords = ('linked', 'circular', 'handcuffs')

    def build(self):
        # Two cuffs hang from a shared upper ring; narrow connectors and doubled cuff walls simplified to single structural strokes.
        axis_x = 24
        p_6_35 = (6, 35)
        p_13_28 = (13, 28)
        p_20_10 = (20, 10)
        p_20_35 = (20, 35)
        p_28_10 = (2 * axis_x - p_20_10[0], p_20_10[1])
        p_28_35 = (2 * axis_x - p_20_35[0], p_20_35[1])
        p_35_28 = (2 * axis_x - p_13_28[0], p_13_28[1])
        p_42_35 = (2 * axis_x - p_6_35[0], p_6_35[1])
        self.add_arc('link-1', p_20_10, p_28_10, radius_x=4, radius_y=4, sweep=True)
        self.add_arc('link-2', p_28_10, p_20_10, radius_x=4, radius_y=4, sweep=True)
        self.add_contour('link', 'link-1', 'link-2', closed=True)
        self.add_arc('left-cuff-1', p_6_35, p_20_35, radius_x=7, radius_y=7, sweep=True)
        self.add_arc('left-cuff-2', p_20_35, p_6_35, radius_x=7, radius_y=7, sweep=True)
        self.add_contour('left-cuff', 'left-cuff-1', 'left-cuff-2', closed=True)
        self.add_arc('right-cuff-1', p_28_35, p_42_35, radius_x=7, radius_y=7, sweep=True)
        self.add_arc('right-cuff-2', p_42_35, p_28_35, radius_x=7, radius_y=7, sweep=True)
        self.add_contour('right-cuff', 'right-cuff-1', 'right-cuff-2', closed=True)
        self.add_line('chain-left-1', p_20_10, p_13_28)
        self.add_contour('chain-left', 'chain-left-1', closed=False)
        self.relate("connect", 'chain-left', 'link')
        self.relate("connect", 'chain-left', 'left-cuff')
        self.add_line('chain-right-1', p_28_10, p_35_28)
        self.add_contour('chain-right', 'chain-right-1', closed=False)
        self.relate("connect", 'chain-right', 'link')
        self.relate("connect", 'chain-right', 'right-cuff')
