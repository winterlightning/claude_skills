from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '938032ae-5024-5ede-94da-88527f48269f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__honey-dipper-drip/20260929T033507Z-thuan-mac/reference/honey_938032ae-5024-5ede-94da-88527f48269f.svg'
AUTHOR = 'gpt-6'
# Symbol plan: Restore three rounded diagonal dipper ridges, a straight rising handle and a pointed falling drop.
# Construction references: No useful exact Lucide match; constructed from the original reference with smooth geometric contours.
class Drawing(Solo48):
    icon_id = 'honey-dipper-drip'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('honey',)

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
        # One diagonal shaft and three rounded ribs normal to it.
        self.add_polyline('shaft',(24,23),(41,6),(44,9),(27,26))
        for n,dx,dy in [('top',0,0),('middle',-4,4),('bottom',-8,8)]:
         self.curve(n,(18+dx,20+dy),((14+dx,16+dy),(10+dx,20+dy),(14+dx,24+dy)),((14+dx,24+dy),(21+dx,31+dy),(21+dx,31+dy)),((25+dx,35+dy),(29+dx,31+dy),(25+dx,27+dy)),((25+dx,27+dy),(18+dx,20+dy),(18+dx,20+dy)))
        self.curve('drop',(9,36),((7,39),(5,40),(5,42)),((5,47),(13,47),(13,42)),((13,40),(11,39),(9,36)))
