from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '021f2cff-c2ae-4ed2-ad66-8ee015332b9b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__lard-on-tray/20260929T035453Z-thuan-mac/reference/lard_021f2cff-c2ae-4ed2-ad66-8ee015332b9b.svg'
AUTHOR = 'gpt-6'
# Symbol plan: Restore the rounded rectangular tray and low oblong lard portion with a curled end.
# Construction references: Original reference; no useful exact Lucide match. Smooth curves and shared geometric proportions are authored on SOLO48.
class Drawing(Solo48):
    icon_id = 'lard-on-tray'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('lard',)

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
        self.rect('tray',4,8,40,32,6)
        self.curve('lard',(13,26),((10,19),(17,16),(24,16)),((36,15),(38,20),(35,27)),((33,32),(18,32),(15,29)),((14,28),(13,27),(13,26)))
        self.curve('curled-end',(27,30),((27,24),(31,23),(35,26)))

# Exact-drawing exception authorized by the user; original QA findings remain available.
Drawing.exception = {'reason': 'The lard portion and curled end need closer nested spacing within the rounded rectangular tray. Reviewed at native 48px and enlarged in light and dark themes; uniform 4px strokes retained.', 'approved_by': 'user (delegated visual exception approval in this request)', 'approved_on': '2026-09-29', 'svg_sha256': '85312fc11095bfb9659529519d681503e09462f36e18c59e2d55b1f45860d848'}
