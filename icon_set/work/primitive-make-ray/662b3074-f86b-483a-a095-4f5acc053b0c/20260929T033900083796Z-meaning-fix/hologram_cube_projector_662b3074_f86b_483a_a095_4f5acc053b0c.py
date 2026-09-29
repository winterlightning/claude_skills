from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '662b3074-f86b-483a-a095-4f5acc053b0c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hologram-cube-projector/20260929T033507Z-thuan-mac/reference/virtual box_662b3074-f86b-483a-a095-4f5acc053b0c.svg'
AUTHOR = 'gpt-6'
# Symbol plan: Restore the cube above a round lens on a low rounded base, with separate projection rays.
# Construction references: No useful exact Lucide match; constructed from the original reference with smooth geometric contours.
class Drawing(Solo48):
    icon_id = 'hologram-cube-projector'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('virtual box',)

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
        self.add_polyline('cube',(24,4),(37,11),(37,24),(24,31),(11,24),(11,11),closed=True)
        self.add_polyline('cube-top',(11,11),(24,18),(37,11))
        self.add_line('cube-front',(24,18),(24,31))
        self.add_line('ray-left',(4,28),(11,35))
        self.add_line('ray-right',(44,28),(37,35))
        self.circle('lens',24,38,5)
        self.rect('base',10,42,28,4,2)
