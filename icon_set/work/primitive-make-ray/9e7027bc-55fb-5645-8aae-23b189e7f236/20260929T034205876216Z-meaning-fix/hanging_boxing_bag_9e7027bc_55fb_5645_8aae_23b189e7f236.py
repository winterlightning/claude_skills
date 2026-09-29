from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '9e7027bc-55fb-5645-8aae-23b189e7f236'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hanging-boxing-bag/20260929T033507Z-thuan-mac/reference/boxing bag hanging_9e7027bc-55fb-5645-8aae-23b189e7f236.svg'
AUTHOR = 'gpt-6'
# Symbol plan: Restore a suspended tapered bag with rounded bottom and a distinct triangular hanger.
# Construction references: No useful exact Lucide match; constructed from the original reference with smooth geometric contours.
class Drawing(Solo48):
    icon_id = 'hanging-boxing-bag'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'sports'
    aliases = ()
    keywords = ('boxing bag hanging',)

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
        self.add_polyline('hanger',(24,4),(18,14),(30,14),closed=True)
        self.add_polyline('straps',(21,14),(18,20),(30,20),(27,14))
        self.curve('shoulder-left',(18,20),((15,24),(14,25),(14,28)))
        self.add_line('left-side',(14,28),(14,34))
        self.add_arc('bottom',(14,34),(34,34),radius_x=10,sweep=False)
        self.add_line('right-side',(34,34),(34,28))
        self.curve('shoulder-right',(34,28),((34,25),(33,24),(30,20)))
        self.add_contour('bag','shoulder-left','left-side','bottom','right-side','shoulder-right')

# Exact-drawing exception authorized by the user; original QA findings remain available.
Drawing.exception = {'reason': 'The long suspended bag needs a narrower natural silhouette than VRECT_M and compact triangular suspension straps. Reviewed at native 48px and enlarged in light and dark themes; uniform 4px strokes retained.', 'approved_by': 'user (delegated visual exception approval in this request)', 'approved_on': '2026-09-29', 'svg_sha256': '317c73496ed774abcf3b408fc7ffdef02552c05d1d2f8430e0877ba083b5ad9f'}
