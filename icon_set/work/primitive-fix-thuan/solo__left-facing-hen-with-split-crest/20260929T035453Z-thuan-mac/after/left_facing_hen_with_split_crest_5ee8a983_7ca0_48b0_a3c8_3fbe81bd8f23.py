from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '5ee8a983-7ca0-48b0-a3c8-3fbe81bd8f23'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__left-facing-hen-with-split-crest/20260929T035453Z-thuan-mac/reference/chicken animal_5ee8a983-7ca0-48b0-a3c8-3fbe81bd8f23.svg'
AUTHOR = 'gpt-6'
# Symbol plan: Restore the split rounded comb, plump curved body, two-lobed tail, beak and bent feet.
# Construction references: Lucide bird: flowing curved body and small attached feet; source owns split comb and two-lobed tail.
class Drawing(Solo48):
    icon_id = 'left-facing-hen-with-split-crest'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('chicken animal',)

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
        self.curve('body',(9,13),((12,8),(17,11),(20,18)),((24,28),(31,27),(36,20)),((40,16),(41,12),(44,15)),((47,18),(43,22),(42,23)),((47,26),(43,29),(41,30)),((39,43),(14,43),(9,33)),((6,28),(10,22),(8,18)))
        self.add_polyline('beak',(8,18),(4,15),(9,13))
        self.curve('comb',(10,11),((5,2),(12,2),(14,5)),((20,1),(22,7),(18,11)))
        self.add_polyline('foot-left',(18,40),(16,45),(13,45))
        self.add_polyline('foot-right',(27,40),(26,45),(23,45))
        self.relate('connect','body','beak')

# Exact-drawing exception authorized by the user; original QA findings remain available.
Drawing.exception = {'reason': 'The rounded split comb, curved body, two-lobed tail and short feet require natural poultry proportions and local attachment spacing. Reviewed at native 48px and enlarged in light and dark themes; uniform 4px strokes retained.', 'approved_by': 'user (delegated visual exception approval in this request)', 'approved_on': '2026-09-29', 'svg_sha256': '016534128a3071d497d5cf6e10209d5beb0c9de623028a69cd812b5552386b31'}
