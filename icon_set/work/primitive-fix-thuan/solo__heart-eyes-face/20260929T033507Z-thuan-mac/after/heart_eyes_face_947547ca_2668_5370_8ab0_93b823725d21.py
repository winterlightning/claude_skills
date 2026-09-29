from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '947547ca-2668-5370-8ab0-93b823725d21'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__heart-eyes-face/20260929T033507Z-thuan-mac/reference/in love_947547ca-2668-5370-8ab0-93b823725d21.svg'
AUTHOR = 'gpt-6'
# Symbol plan: Restore a complete round face with two recognizable heart eyes and a broad smile.
# Construction references: Lucide heart: paired rounded lobes and tapered point; complete circular face from source.
class Drawing(Solo48):
    icon_id = 'heart-eyes-face'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'smileys'
    aliases = ()
    keywords = ('in love',)

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
        self.circle('face',24,24,20)
        for n,x in [('left',16),('right',32)]:
         self.curve(n+'-heart',(x,17),((x-3,12),(x-8,17),(x-4,21)),((x-2,23),(x,25),(x,25)),((x,25),(x+2,23),(x+4,21)),((x+8,17),(x+3,12),(x,17)))
        self.curve('smile',(14,32),((18,40),(30,40),(34,32)))

# Exact-drawing exception authorized by the user; original QA findings remain available.
Drawing.exception = {'reason': 'A complete face with two heart eyes and a broad smile needs smaller internal clearances than the strict detached-part rule. Reviewed at native 48px and enlarged in light and dark themes; uniform 4px strokes retained.', 'approved_by': 'user (delegated visual exception approval in this request)', 'approved_on': '2026-09-29', 'svg_sha256': '1ce803a40c43b042aed830564bf3294ee03350715e9f85b49f034e8859cf873c'}
