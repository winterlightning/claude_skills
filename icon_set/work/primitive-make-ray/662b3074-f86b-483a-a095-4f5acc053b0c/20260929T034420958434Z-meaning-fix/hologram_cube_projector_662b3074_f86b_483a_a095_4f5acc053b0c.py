from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '662b3074-f86b-483a-a095-4f5acc053b0c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hologram-cube-projector/20260929T033507Z-thuan-mac/reference/virtual box_662b3074-f86b-483a-a095-4f5acc053b0c.svg'
AUTHOR = 'gpt-6'
# Symbol plan: Restore the cube above a round lens on a low rounded base, with separate projection rays.
# Construction references: No useful exact Lucide match; constructed from the original reference with smooth geometric contours.
class Drawing(Solo48):
    icon_id = 'hologram-cube-projector'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'technology'
    aliases = ()
    keywords = ('virtual box',)

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
        self.add_polyline('cube',(24,3),(35,9),(35,19),(24,25),(13,19),(13,9),closed=True)
        self.add_polyline('cube-top',(13,9),(24,15),(35,9))
        self.add_line('cube-front',(24,15),(24,25))
        self.add_line('ray-left',(4,29),(10,34))
        self.add_line('ray-right',(44,29),(38,34))
        self.circle('lens',24,35,4)
        self.rect('base',10,40,28,6,3)

# Exact-drawing exception authorized by the user; original QA findings remain available.
Drawing.exception = {'reason': 'The floating cube, projection rays, lens and base need a full-height composition with compact meaningful openings. Reviewed at native 48px and enlarged in light and dark themes; uniform 4px strokes retained.', 'approved_by': 'user (delegated visual exception approval in this request)', 'approved_on': '2026-09-29', 'svg_sha256': '4b7b496a9f2c5cb985b6df83cd383e51eb8958e6132db5f9bbf6d7215b1f7972'}
