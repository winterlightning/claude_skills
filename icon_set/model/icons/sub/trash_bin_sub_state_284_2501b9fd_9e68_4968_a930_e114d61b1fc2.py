"""Trash Bin: An upright open-bodied bin has straight sides, rounded bottom corners, and a flat lid projecting beyond both sides. A short vertical handle rises from the lid's centre.

Construction: Straight-sided blank bin retains a short upright lid knob; source has no interior marks.
Keyshape: SQUARE; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '2501b9fd-9e68-4968-a930-e114d61b1fc2'
SOURCE_PATH = 'pictographic-primitives/state/trash_2501b9fd-9e68-4968-a930-e114d61b1fc2.svg'
AUTHOR = 'gpt-6'


class TrashBinSubState284(Sub32):
    icon_id = 'trash-bin-sub-state-284'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('trash', 'bin', 'upright', 'open', 'bodied', 'straight', 'sides', 'rounded')

    def build(self):
        self.add_line('lid',(2,8),(30,8))
        self.add_line('knob',(16,2),(16,8))
        self.add_line('left',(6,8),(6,26))
        self.add_arc('left-corner',(6,26),(10,30),radius_x=4,sweep=False)
        self.add_line('base',(10,30),(22,30))
        self.add_arc('right-corner',(22,30),(26,26),radius_x=4,sweep=False)
        self.add_line('right',(26,26),(26,8))
        self.add_contour('bin','left','left-corner','base','right-corner','right')
        self.relate('connect','lid','bin')
        self.relate('connect','lid','knob')
