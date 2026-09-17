"""Geometric Paw: Three detached circular toe pads surround the upper half of an upright triangular main pad. The top circle is centred, with lower circles placed evenly to the left and right.

Construction: Three circular toe pads above an upright triangular pad, arranged around x16.
Keyshape: SQUARE; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '70306aa2-f188-495b-bfeb-fcee199061f9'
SOURCE_PATH = 'pictographic-primitives/state/paw_70306aa2-f188-495b-bfeb-fcee199061f9.svg'
AUTHOR = 'gpt-6'


class GeometricPaw(Sub32):
    icon_id = 'geometric-paw'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives/shape'
    aliases = ()
    keywords = ('geometric', 'paw', 'detached', 'circular', 'toe', 'pads', 'surround', 'upper')

    def build(self):
        def circle(name,cx,cy,radius):
            self.add_arc(name+"-top",(cx-radius,cy),(cx+radius,cy),radius_x=radius)
            self.add_arc(name+"-bottom",(cx+radius,cy),(cx-radius,cy),radius_x=radius)
            self.add_contour(name,name+"-top",name+"-bottom",closed=True)
        circle("toe-top",16,5,3)
        circle("toe-left",5,13,3)
        circle("toe-right",27,13,3)
        self.add_polyline("pad",(16,20),(26,30),(6,30),closed=True)
