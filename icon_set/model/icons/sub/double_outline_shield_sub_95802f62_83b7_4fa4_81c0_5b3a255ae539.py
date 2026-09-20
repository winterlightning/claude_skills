"""A pointed shield with a second smaller concentric shield outline, both sharing the same pointed-top/curved-side construction. Keep both complete outlines.

Plan: Two complete nested shields, each with a pointed crown and smooth sides. Bounds (4,2)-(28,30).
Construction reference: Lucide shield: joined crown and smooth sidewalls; preserve both source outlines."""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '95802f62-83b7-4fa4-81c0-5b3a255ae539'
SOURCE_PATH = 'pictographic-primitives/state/shield 2_95802f62-83b7-4fa4-81c0-5b3a255ae539.svg'
SOURCE_ICON_IDS = ('95802f62-83b7-4fa4-81c0-5b3a255ae539',)
AUTHOR = 'gpt-6'

class DoubleOutlineShieldSub(Sub32):
    icon_id = 'double-outline-shield-sub'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('double', 'outline', 'shield', 'sub')

    def build(self) -> None:
        for name,left,right,top,shoulder,bottom in (('outer',4,28,2,6,30),('inner',11,21,10,12,22)):
            axis=16
            self.add_polyline(name+'-crown',(left,shoulder),(axis,top),(right,shoulder))
            self.add_bezier(name+'-right',(right,shoulder),((right,bottom-8),(right-2,bottom-4),(axis,bottom)))
            self.add_bezier(name+'-left',(axis,bottom),((left+2,bottom-4),(left,bottom-8),(left,shoulder)))
            self.add_contour(name,name+'-crown-1',name+'-crown-2',name+'-right',name+'-left',closed=True)
            self.contours=[c for c in self.contours if c.contour_id!=name+'-crown']
