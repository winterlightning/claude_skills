from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'e5d36fda-d12e-4a2d-a970-b3258b3fc57c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__head-wrapped-in-bandage/20260929T033507Z-thuan-mac/reference/face head bandage_e5d36fda-d12e-4a2d-a970-b3258b3fc57c.svg'
AUTHOR = 'gpt-6'
# Symbol plan: Move the bandage to the upper head and restore its folded return, leaving the lower face open.
# Construction references: No useful exact Lucide match; constructed from the original reference with smooth geometric contours.
class Drawing(Solo48):
    icon_id = 'head-wrapped-in-bandage'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('face head bandage',)

    def circle(self, n, x, y, r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)
    def rect(self,n,x,y,w,h,r=0):
        if not r:
            self.add_polyline(n,(x,y),(x+w,y),(x+w,y+h),(x,y+h),closed=True)
            return
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        for j in range(8):
            a,b=pts[j],pts[(j+1)%8]
            if j%2:self.add_arc(n+str(j),a,b,radius_x=r)
            else:self.add_line(n+str(j),a,b)
        self.add_contour(n,*(n+str(j) for j in range(8)),closed=True)
    def curve(self,n,start,*segments):
        self.add_bezier(n,start,*segments)

    def build(self):
        self.circle('head',24,24,20)
        self.add_line('wrap-upper',(6,16),(33,6))
        self.add_polyline('wrap-lower',(4,25),(23,18),(23,21),(44,21))
