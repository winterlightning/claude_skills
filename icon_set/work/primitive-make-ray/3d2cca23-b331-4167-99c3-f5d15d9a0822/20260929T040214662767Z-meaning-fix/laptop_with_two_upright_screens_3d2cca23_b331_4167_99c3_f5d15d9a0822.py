from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '3d2cca23-b331-4167-99c3-f5d15d9a0822'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__laptop-with-two-upright-screens/20260929T035453Z-thuan-mac/reference/responsive design laptop_3d2cca23-b331-4167-99c3-f5d15d9a0822.svg'
AUTHOR = 'gpt-6'
# Symbol plan: Restore two tall rounded screens above a linked laptop body and curved lower base.
# Construction references: Lucide laptop and smartphone: consistent screen radii; source owns the two tall panels and lower connecting body.
class Drawing(Solo48):
    icon_id = 'laptop-with-two-upright-screens'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'websites'
    aliases = ()
    keywords = ('responsive design laptop',)

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
        for x in (4,30):self.rect('upright-'+str(x),x,4,14,27,3)
        self.add_line('screen-bridge',(18,18),(30,18))
        self.add_line('body-left',(11,31),(11,39))
        self.add_line('body-right',(37,31),(37,39))
        self.add_line('deck',(5,39),(43,39))
        self.curve('base',(5,39),((5,44),(9,44),(13,44)),((13,44),(35,44),(35,44)),((39,44),(43,44),(43,39)))
        self.relate('connect','deck','base')

# Exact-drawing exception authorized by the user; original QA findings remain available.
Drawing.exception = {'reason': 'The two tall screens and connecting laptop body need their source proportions and a shallow curved base. Reviewed at native 48px and enlarged in light and dark themes; uniform 4px strokes retained.', 'approved_by': 'user (delegated visual exception approval in this request)', 'approved_on': '2026-09-29', 'svg_sha256': '86718f31decdcfabc46c3624e6afd107c66f6ff4bcdd3cdf02d9a4d1fae6f8fb'}
