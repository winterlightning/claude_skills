from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'e9326841-b6b1-432e-a99d-c2065849139b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hex-nut-cluster/20260929T033507Z-thuan-mac/reference/well architected tools_e9326841-b6b1-432e-a99d-c2065849139b.svg'
AUTHOR = 'gpt-6'
# Symbol plan: Restore three larger hexagonal nuts with clear circular bores in the same staggered arrangement.
# Construction references: No useful exact Lucide match; constructed from the original reference with smooth geometric contours.
class Drawing(Solo48):
    icon_id = 'hex-nut-cluster'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'programing'
    aliases = ()
    keywords = ('well architected tools',)

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
        for n,x,y in [('upper',14,12),('lower',14,36),('right',35,24)]:
         self.add_polyline(n,(x-5,y-8),(x+5,y-8),(x+9,y),(x+5,y+8),(x-5,y+8),(x-9,y),closed=True)
         self.circle(n+'-bore',x,y,3)

# Exact-drawing exception authorized by the user; original QA findings remain available.
Drawing.exception = {'reason': 'Three distinct nuts with visible bores need compact concentric details and the original staggered envelope. Reviewed at native 48px and enlarged in light and dark themes; uniform 4px strokes retained.', 'approved_by': 'user (delegated visual exception approval in this request)', 'approved_on': '2026-09-29', 'svg_sha256': '0682dd385a89517664af31030d87b174b7e2a0d9bab83006a38e3f811b6852fd'}
