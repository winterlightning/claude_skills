"""Leaf: A broad leaf points upper-left, with a bowed right edge and a rounded lower base. Its curved vein extends through the base into a stem descending lower-right.

Construction: An upper-left pointed leaf has a rounded lower-right body and one curved vein extending into its stem.
Keyshape: SQUARE; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '7268cdee-6014-437c-9511-21426dd1c77e'
SOURCE_PATH = 'pictographic-primitives/state/leaf left_7268cdee-6014-437c-9511-21426dd1c77e.svg'
AUTHOR = 'gpt-6'


class LeafState145(Sub32):
    icon_id = 'leaf-state-145'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives/shape'
    aliases = ()
    keywords = ('leaf', 'broad', 'points', 'upper', 'left', 'bowed', 'right', 'edge')

    def build(self):
        self.add_arc('upper',(2,2),(16,6),radius_x=22,radius_y=12,sweep=False)
        self.add_arc('right-upper',(16,6),(28,18),radius_x=12)
        self.add_arc('right-lower',(28,18),(16,28),radius_x=12,radius_y=10)
        self.add_arc('left-lower',(16,28),(2,14),radius_x=14)
        self.add_line('left-upper',(2,14),(2,2))
        self.add_contour('leaf','upper','right-upper','right-lower','left-lower','left-upper',closed=True)
        self.add_arc('vein',(14,14),(30,30),radius_x=32)
        self.relate('connect','leaf','vein')
