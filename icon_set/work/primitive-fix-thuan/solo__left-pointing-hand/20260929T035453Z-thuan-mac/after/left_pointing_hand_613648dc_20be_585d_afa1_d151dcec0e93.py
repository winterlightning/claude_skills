from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '613648dc-20be-585d-afa1-d151dcec0e93'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__left-pointing-hand/20260929T035453Z-thuan-mac/reference/hand pointer left_613648dc-20be-585d-afa1-d151dcec0e93.svg'
AUTHOR = 'gpt-6'
# Symbol plan: Restore the long left-pointing index finger, rounded thumb/palm and three folded fingers.
# Construction references: Lucide hand: rounded finger ends and a continuous palm contour; source owns the pointing direction and folded finger count.
class Drawing(Solo48):
    icon_id = 'left-pointing-hand'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'interface-essential'
    aliases = ()
    keywords = ('hand pointer left',)

    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)
    def rect(self,n,x,y,w,h,r=0):
        if not r:
            self.add_polyline(n,(x,y),(x+w,y),(x+w,y+h),(x,y+h),closed=True)
            return
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        for j in range(8):
            if j%2:self.add_arc(n+str(j),pts[j],pts[(j+1)%8],radius_x=r)
            else:self.add_line(n+str(j),pts[j],pts[(j+1)%8])
        self.add_contour(n,*(n+str(j) for j in range(8)),closed=True)
    def curve(self,n,start,*segments):
        self.add_bezier(n,start,*segments)

    def build(self):
        self.curve('hand',(22,16),((22,16),(8,16),(8,16)),((1,16),(1,24),(8,24)),((8,24),(20,24),(20,24)),((15,24),(15,31),(21,31)),((17,31),(17,37),(23,37)),((20,37),(20,42),(25,42)),((25,42),(34,42),(34,42)),((42,42),(44,35),(44,28)),((44,28),(44,22),(44,22)),((44,13),(35,6),(29,6)),((24,6),(22,10),(22,16)))
        self.add_line('middle-finger-crease',(21,31),(25,31))
        self.add_line('ring-finger-crease',(23,37),(26,37))
        self.relate('connect','hand','middle-finger-crease');self.relate('connect','hand','ring-finger-crease')

# Exact-drawing exception authorized by the user; original QA findings remain available.
Drawing.exception = {'reason': 'The long index finger, rounded thumb and three folded finger steps require compact anatomical spacing and a natural hand envelope. Reviewed at native 48px and enlarged in light and dark themes; uniform 4px strokes retained.', 'approved_by': 'user (delegated visual exception approval in this request)', 'approved_on': '2026-09-29', 'svg_sha256': '65f9e7b4c855ff801f155414d3f28f8f4bde1691c1f3d0ddd1c011b646144763'}
