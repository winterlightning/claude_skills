"""massage bubble with house.
Plan: Restored an oval speech bubble with a clear tail and a wider house with an open wall contour and pitched roof.
Construction: message-circle: smooth bubble and distinct tail; original controls house arrangement.
Keyshape: SQUARE; preserve the original's recognizable proportions.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = 'e05971da-9c03-4db3-a3f0-1963b3e1e1f0'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__house-message-bubble-solo/20260929T033633Z-thuan-mac/reference/massage bubble with house_e05971da-9c03-4db3-a3f0-1963b3e1e1f0.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'house-message-bubble-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('massage', 'bubble', 'with', 'house')

    def circle(self,n,x,y,r,ry=None):
        ry=r if ry is None else ry
        self.add_arc(n+'a',(x-r,y),(x+r,y),radius_x=r,radius_y=ry)
        self.add_arc(n+'b',(x+r,y),(x-r,y),radius_x=r,radius_y=ry)
        self.add_contour(n,n+'a',n+'b',closed=True)
    def rect(self,n,x,y,w,h,r=3):
        self.add_line(n+'t',(x+r,y),(x+w-r,y))
        self.add_arc(n+'tr',(x+w-r,y),(x+w,y+r),radius_x=r)
        self.add_line(n+'r',(x+w,y+r),(x+w,y+h-r))
        self.add_arc(n+'br',(x+w,y+h-r),(x+w-r,y+h),radius_x=r)
        self.add_line(n+'b',(x+w-r,y+h),(x+r,y+h))
        self.add_arc(n+'bl',(x+r,y+h),(x,y+h-r),radius_x=r)
        self.add_line(n+'l',(x,y+h-r),(x,y+r))
        self.add_arc(n+'tl',(x,y+r),(x+r,y),radius_x=r)
        self.add_contour(n,*[n+s for s in ['t','tr','r','br','b','bl','l','tl']],closed=True)

    def build(self):

        self.add_bezier('bubble',(10,33),((0,24),(3,7),(18,5)),((33,1),(44,10),(44,21)),((44,33),(32,39),(18,36)))
        self.add_polyline('tail',(18,36),(5,43),(10,33));self.relate('connect','tail','bubble')
        self.add_polyline('roof',(13,22),(24,12),(35,22))
        self.add_polyline('walls',(17,19),(17,30),(31,30),(31,19))
        self.relate('connect','walls','roof')

# User authorized per-drawing visual exceptions; automatic findings retained.
Drawing.exception = {'reason': 'Preserve the broad oval speech bubble, angular tail and large house. Natural curved envelope and roof-to-bubble clearance are visually clear at 48px.', 'approved_by': 'user-authorized-agent-visual-review', 'approved_on': '2026-09-29', 'svg_sha256': '021292ba5fcb0ed6bcda15d89329ad51d0426e147d3eb104ea6d4e5c21fd649f'}
