"""Cauldron with Stirring Spoon.

Plan: Deep rounded cauldron with two feet and diagonal stirring spoon. Reduce mouth ellipse to one clear rim and spoon handle to one stroke. Lucide cooking-pot informs rounded vessel. Bounds (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4db0b253-8925-4f47-b4e9-fe7209dfb498'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/cauldron mix_4db0b253-8925-4f47-b4e9-fe7209dfb498.svg'
AUTHOR = 'gpt-6'

class CauldronWithStirringSpoon(Solo48):
    icon_id = 'cauldron-with-stirring-spoon'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'holidays'
    aliases = ()
    keywords = ('cauldron', 'with', 'stirring', 'spoon')

    def build(self):
        self.add_polyline('rim',(6,20),(30,20),(42,20),(42,28))
        self.add_arc('body-right',(42,28),(32,38),radius_x=10)
        self.add_line('bottom',(32,38),(16,38))
        self.add_arc('body-left',(16,38),(6,28),radius_x=10)
        self.add_line('left',(6,28),(6,20))
        self.add_contour('pot','rim-1','rim-2','rim-3','body-right','bottom','body-left','left',closed=True)
        self.contours=[c for c in self.contours if c.contour_id!='rim']
        for n,a,b in [('spoon',(30,20),(42,6)),('foot-left',(16,38),(12,42)),('foot-right',(32,38),(36,42))]:
         self.add_line(n,a,b);self.relate('connect','pot',n)
