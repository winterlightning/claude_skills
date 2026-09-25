"""Trash Bin: A tapered bin with rounded bottom corners sits beneath a wide projecting lid. A rounded rectangular handle rises centrally above the lid, and the body remains blank.

Construction: Blank tapered bin retains a rounded rectangular top handle and wide lid.
Keyshape: SQUARE; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '5e0c6d19-547e-46f0-8ec6-c837972fb3f0'
SOURCE_PATH = 'pictographic-primitives/state/trash_5e0c6d19-547e-46f0-8ec6-c837972fb3f0.svg'
AUTHOR = 'gpt-6'


class TrashBinSubState285(Sub32):
    icon_id = 'trash-bin-sub-state-285'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('trash', 'bin', 'tapered', 'rounded', 'bottom', 'corners', 'sits', 'beneath')

    def build(self):
        self.add_line('lid',(2,10),(30,10))
        self.add_polyline('bin',(4,10),(6,30),(26,30),(28,10))
        self.add_line('handle-left',(10,10),(10,6))
        self.add_arc('handle-top',(10,6),(22,6),radius_x=6,radius_y=4)
        self.add_line('handle-right',(22,6),(22,10))
        self.add_contour('handle','handle-left','handle-top','handle-right')
        self.relate('connect','lid','bin')
        self.relate('connect','lid','handle')
