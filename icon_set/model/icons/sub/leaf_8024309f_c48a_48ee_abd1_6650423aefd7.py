"""Leaf: A broad leaf lies horizontally with a rounded left base and pointed right tip. A curved central vein enters from the lower left and stops inside the blade.

Construction: One asymmetric leaf outline with a rounded base and pointed right tip; vein attaches at the base.
Keyshape: HRECT_XL; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '8024309f-c48a-48ee-abd1-6650423aefd7'
SOURCE_PATH = 'pictographic-primitives/state/leaf horizontal_8024309f-c48a-48ee-abd1-6650423aefd7.svg'
AUTHOR = 'gpt-6'


class Leaf(Sub32):
    icon_id = 'leaf'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives/shape'
    aliases = ()
    keywords = ('leaf', 'broad', 'lies', 'horizontally', 'rounded', 'left', 'base', 'pointed')

    def build(self):
        self.add_arc("upper-base",(4,18),(14,4),radius_x=10,radius_y=14)
        self.add_arc("upper-tip",(14,4),(30,8),radius_x=20,radius_y=12,sweep=False)
        self.add_arc("lower-tip",(30,8),(14,28),radius_x=22,radius_y=22)
        self.add_arc("lower-base",(14,28),(4,18),radius_x=10)
        self.add_contour("leaf","upper-base","upper-tip","lower-tip","lower-base",closed=True)
        self.add_line("vein",(2,22),(20,14))
        self.relate("connect","leaf","vein")
