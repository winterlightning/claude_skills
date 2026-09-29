from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'ce61eef0-26c7-53d5-8b7f-008e608029a0'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__handled-diya-oil-lamp/20260929T033507Z-thuan-mac/reference/karthika deepam_ce61eef0-26c7-53d5-8b7f-008e608029a0.svg'
AUTHOR = 'gpt-6'
# Symbol plan: Restore a pointed flame above a deep bowl, round side handle and flared pedestal.
# Construction references: Lucide flame: pointed tip and rounded teardrop body; source owns bowl, handle and pedestal.
class Drawing(Solo48):
    icon_id = 'handled-diya-oil-lamp'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'holidays'
    aliases = ()
    keywords = ('karthika deepam',)

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
        self.curve('flame',(24,4),((24,10),(30,11),(30,17)),((30,24),(18,24),(18,17)),((18,12),(23,10),(24,4)))
        self.add_line('wick',(24,23),(24,27))
        self.curve('bowl',(6,27),((10,43),(30,43),(34,27)))
        self.add_line('rim',(6,27),(34,27))
        self.curve('handle',(34,25),((38,17),(46,23),(43,29)),((41,33),(36,33),(33,32)))
        self.add_polyline('foot',(20,39),(15,44),(31,44),(26,39))

# Exact-drawing exception authorized by the user; original QA findings remain available.
Drawing.exception = {'reason': 'The connected flame, bowl, loop handle and flared pedestal need their natural asymmetric envelope and small attachment openings. Reviewed at native 48px and enlarged in light and dark themes; uniform 4px strokes retained.', 'approved_by': 'user (delegated visual exception approval in this request)', 'approved_on': '2026-09-29', 'svg_sha256': 'b4728092da54f00b637a05f896d732039078aeadc42df2dd06394e2924057b52'}
