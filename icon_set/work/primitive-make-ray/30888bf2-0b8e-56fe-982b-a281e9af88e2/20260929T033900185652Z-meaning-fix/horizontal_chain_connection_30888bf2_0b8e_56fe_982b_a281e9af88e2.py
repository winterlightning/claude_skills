from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '30888bf2-0b8e-56fe-982b-a281e9af88e2'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__horizontal-chain-connection/20260929T033507Z-thuan-mac/reference/hyperlink_30888bf2-0b8e-56fe-982b-a281e9af88e2.svg'
AUTHOR = 'gpt-6'
# Symbol plan: Restore two horizontally arranged open circular links and a longer joining bar through their mouths.
# Construction references: No useful exact Lucide match; constructed from the original reference with smooth geometric contours.
class Drawing(Solo48):
    icon_id = 'horizontal-chain-connection'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('hyperlink',)

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
        self.curve('left-link',(19,17),((6,4),(-3,23),(7,32)),((11,36),(16,35),(19,31)))
        self.curve('right-link',(29,17),((42,4),(51,23),(41,32)),((37,36),(32,35),(29,31)))
        self.add_line('connection',(15,24),(33,24))
