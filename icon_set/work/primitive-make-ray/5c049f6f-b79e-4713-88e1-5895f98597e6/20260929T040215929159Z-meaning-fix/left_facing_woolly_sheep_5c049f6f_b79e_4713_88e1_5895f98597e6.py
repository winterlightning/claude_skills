from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '5c049f6f-b79e-4713-88e1-5895f98597e6'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__left-facing-woolly-sheep/20260929T035453Z-thuan-mac/reference/mouton_5c049f6f-b79e-4713-88e1-5895f98597e6.svg'
AUTHOR = 'gpt-6'
# Symbol plan: Restore a woolly scalloped outline, long left-facing head, drooping ear and short legs.
# Construction references: Original reference; no useful exact Lucide match. Smooth curves and shared geometric proportions are authored on SOLO48.
class Drawing(Solo48):
    icon_id = 'left-facing-woolly-sheep'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('mouton',)

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
        self.curve('woolly-body',(8,14),((10,4),(20,4),(22,12)),((28,12),(30,19),(24,19)),((20,19),(19,16),(18,15)))
        self.curve('back',(28,15),((32,11),(35,13),(36,15)),((45,13),(45,23),(43,26)),((45,29),(43,34),(41,35)))
        self.add_polyline('rear-leg',(41,35),(42,44),(36,44),(35,37))
        self.curve('belly',(35,37),((32,40),(26,38),(24,36)),((21,39),(19,38),(17,38)))
        self.add_polyline('front-leg',(17,38),(16,44),(11,44),(11,36))
        self.curve('chest-face',(11,36),((6,33),(6,28),(7,24)),((0,25),(1,17),(8,14)))
        self.relate('connect','back','rear-leg');self.relate('connect','rear-leg','belly');self.relate('connect','belly','front-leg');self.relate('connect','front-leg','chest-face');self.relate('connect','chest-face','woolly-body')

# Exact-drawing exception authorized by the user; original QA findings remain available.
Drawing.exception = {'reason': 'The woolly outline, drooping ear, muzzle and short legs need their natural animal envelope and compact attachment spaces. Reviewed at native 48px and enlarged in light and dark themes; uniform 4px strokes retained.', 'approved_by': 'user (delegated visual exception approval in this request)', 'approved_on': '2026-09-29', 'svg_sha256': 'da695cb777c209f420021518707b492b6d13dc87b54baab33b42ce48772c8784'}
