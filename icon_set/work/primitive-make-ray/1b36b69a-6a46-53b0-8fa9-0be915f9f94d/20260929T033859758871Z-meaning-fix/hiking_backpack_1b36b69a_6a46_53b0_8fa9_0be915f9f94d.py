from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '1b36b69a-6a46-53b0-8fa9-0be915f9f94d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hiking-backpack/20260929T033507Z-thuan-mac/reference/outdoors backpack_1b36b69a-6a46-53b0-8fa9-0be915f9f94d.svg'
AUTHOR = 'gpt-6'
# Symbol plan: Restore the rounded tall body, overhanging top flap, central fastening tab and side pockets.
# Construction references: No useful exact Lucide match; constructed from the original reference with smooth geometric contours.
class Drawing(Solo48):
    icon_id = 'hiking-backpack'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('outdoors backpack',)

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
        self.rect('body',12,6,24,38,6)
        self.rect('top-flap',10,4,28,14,4)
        self.rect('tab',20,14,8,11,3)
        self.curve('left-pocket',(12,28),((3,27),(4,29),(4,34)),((4,39),(5,40),(12,40)))
        self.curve('right-pocket',(36,28),((45,27),(44,29),(44,34)),((44,39),(43,40),(36,40)))
        self.add_line('pocket-seam',(19,34),(29,34))
