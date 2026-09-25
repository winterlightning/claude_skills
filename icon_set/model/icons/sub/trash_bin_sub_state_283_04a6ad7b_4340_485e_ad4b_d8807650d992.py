"""Trash Bin: A slightly tapered bin has rounded lower corners and a wide flat lid topped by an arched handle. One short vertical groove appears in the centre of the body.

Construction: Tapered bin retains arched lid handle and one central vertical interior mark.
Keyshape: SQUARE; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '04a6ad7b-4340-485e-ad4b-d8807650d992'
SOURCE_PATH = 'pictographic-primitives/state/trash_04a6ad7b-4340-485e-ad4b-d8807650d992.svg'
AUTHOR = 'gpt-6'


class TrashBinSubState283(Sub32):
    icon_id = 'trash-bin-sub-state-283'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('trash', 'bin', 'slightly', 'tapered', 'rounded', 'lower', 'corners', 'wide')

    def build(self):
        self.add_line('lid',(2,10),(30,10))
        self.add_polyline('bin',(4,10),(6,30),(26,30),(28,10))
        self.add_arc('handle',(8,10),(24,10),radius_x=8)
        self.add_line('mark',(16,18),(16,24))
        self.relate('connect','lid','bin')
        self.relate('connect','lid','handle')
