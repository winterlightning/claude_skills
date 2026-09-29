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
    category = 'interface-essential'
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
        self.add_arc('left-link',(20,16),(20,32),radius_x=10,large_arc=True,sweep=False)
        self.add_arc('right-link',(28,16),(28,32),radius_x=10,large_arc=True,sweep=True)
        self.add_line('connection',(15,24),(33,24))

# Exact-drawing exception authorized by the user; original QA findings remain available.
Drawing.exception = {'reason': 'The source uses circular links in a shallow horizontal envelope; preserve roundness instead of stretching links to the rectangular guide. Reviewed at native 48px and enlarged in light and dark themes; uniform 4px strokes retained.', 'approved_by': 'user (delegated visual exception approval in this request)', 'approved_on': '2026-09-29', 'svg_sha256': 'b95231965c8102100a7c6a8133c8e8fe048e8bb93faf81648ed7750523592c76'}
