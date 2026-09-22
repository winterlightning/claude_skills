"""Move List Item Upward. Two equal empty list cells on the left; an upward arrow on the right. Shared cell dimensions; arrowhead mirrors x=34. Lucide list-start contributes an open arrowhead and aligned list rows. Square bounds 6 to 42."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = 'd2ad2f5a-c96d-41a2-ba22-217f6b8a8dfa'
SOURCE_PATH = 'pictographic-primitives/design/reorder up_d2ad2f5a-c96d-41a2-ba22-217f6b8a8dfa.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = 'move-list-item-upward'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'design'
    aliases = ('Move List Item Upward',)
    keywords = ('move', 'list', 'item', 'upward')
    def build(self):
        x,y,w,h,r = 6,6,11,13,3
        self.add_line("upper-top",(x+r,y),(x+w-r,y))
        self.add_arc("upper-tr",(x+w-r,y),(x+w,y+r),radius_x=r)
        self.add_line("upper-right",(x+w,y+r),(x+w,y+h-r))
        self.add_arc("upper-br",(x+w,y+h-r),(x+w-r,y+h),radius_x=r)
        self.add_line("upper-bottom",(x+w-r,y+h),(x+r,y+h))
        self.add_arc("upper-bl",(x+r,y+h),(x,y+h-r),radius_x=r)
        self.add_line("upper-left",(x,y+h-r),(x,y+r))
        self.add_arc("upper-tl",(x,y+r),(x+r,y),radius_x=r)
        self.add_contour("upper", *["upper-"+s for s in ("top","tr","right","br","bottom","bl","left","tl")],closed=True)
        x,y,w,h,r = 6,29,11,13,3
        self.add_line("lower-top",(x+r,y),(x+w-r,y))
        self.add_arc("lower-tr",(x+w-r,y),(x+w,y+r),radius_x=r)
        self.add_line("lower-right",(x+w,y+r),(x+w,y+h-r))
        self.add_arc("lower-br",(x+w,y+h-r),(x+w-r,y+h),radius_x=r)
        self.add_line("lower-bottom",(x+w-r,y+h),(x+r,y+h))
        self.add_arc("lower-bl",(x+r,y+h),(x,y+h-r),radius_x=r)
        self.add_line("lower-left",(x,y+h-r),(x,y+r))
        self.add_arc("lower-tl",(x,y+r),(x+r,y),radius_x=r)
        self.add_contour("lower", *["lower-"+s for s in ("top","tr","right","br","bottom","bl","left","tl")],closed=True)
        self.add_polyline('arrowhead',(26,14),(34,6),(42,14))
        self.add_line('shaft',(34,6),(34,42))
        self.relate('connect','arrowhead','shaft')
