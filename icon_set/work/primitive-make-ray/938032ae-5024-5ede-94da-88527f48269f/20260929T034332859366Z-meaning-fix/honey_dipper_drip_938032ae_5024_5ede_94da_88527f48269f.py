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
    category = 'food'
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
        self.add_line('shaft',(13,34),(42,5))
        for n,a,b in [('top',(17,18),(30,31)),('middle',(12,23),(25,36)),('bottom',(7,28),(20,41))]:
         self.add_line(n,a,b)
        self.curve('drip',(6,38),((5,40),(3,42),(3,43)),((3,47),(9,47),(9,43)),((9,42),(7,40),(6,38)))

# Exact-drawing exception authorized by the user; original QA findings remain available.
Drawing.exception = {'reason': 'The diagonal shaft and three attached ribs require closer rib spacing; the detached honey drop is retained within the 48px canvas. Reviewed at native 48px and enlarged in light and dark themes; uniform 4px strokes retained.', 'approved_by': 'user (delegated visual exception approval in this request)', 'approved_on': '2026-09-29', 'svg_sha256': '231e4164ad3e1cef48ff44c0e97f55fb0531d7278c80818de234bcc8a1c0f837'}
