from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '43492aa9-0df0-44b7-9d64-1b9b1628b0de'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__leggings-batch-071/20260929T035453Z-thuan-mac/reference/tights_43492aa9-0df0-44b7-9d64-1b9b1628b0de.svg'
AUTHOR = 'gpt-6'
# Symbol plan: Restore the high crotch, long narrow tapered legs and smooth waist-to-ankle contour.
# Construction references: Original reference; no useful exact Lucide match. Smooth curves and shared geometric proportions are authored on SOLO48.
class Drawing(Solo48):
    icon_id = 'leggings-batch-071'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('tights',)

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
        self.add_line('waist',(14,4),(34,4))
        self.curve('right-leg',(34,4),((36,15),(34,31),(34,44)))
        self.add_polyline('inner-legs',(34,44),(28,44),(24,15),(20,44),(14,44))
        self.curve('left-leg',(14,44),((14,31),(12,15),(14,4)))
        self.relate('connect','waist','right-leg');self.relate('connect','right-leg','inner-legs');self.relate('connect','inner-legs','left-leg');self.relate('connect','left-leg','waist')

# Exact-drawing exception authorized by the user; original QA findings remain available.
Drawing.exception = {'reason': 'The tall narrow leggings need their source proportions, high crotch and slim ankles rather than widening them into generic trousers. Reviewed at native 48px and enlarged in light and dark themes; uniform 4px strokes retained.', 'approved_by': 'user (delegated visual exception approval in this request)', 'approved_on': '2026-09-29', 'svg_sha256': 'a787c899a18bfad9f5e427bb590fb6b12bd1dbfe978e6135a21060b8521f4dc5'}
