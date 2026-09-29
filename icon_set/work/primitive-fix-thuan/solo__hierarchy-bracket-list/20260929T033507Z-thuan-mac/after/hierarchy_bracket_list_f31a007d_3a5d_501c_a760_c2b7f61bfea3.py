from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'f31a007d-3a5d-501c-a760-c2b7f61bfea3'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hierarchy-bracket-list/20260929T033507Z-thuan-mac/reference/hierarchy_f31a007d-3a5d-501c-a760-c2b7f61bfea3.svg'
AUTHOR = 'gpt-6'
# Symbol plan: Restore three outlined rectangular nodes connected to a right-hand bracket.
# Construction references: No useful exact Lucide match; constructed from the original reference with smooth geometric contours.
class Drawing(Solo48):
    icon_id = 'hierarchy-bracket-list'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'programing'
    aliases = ()
    keywords = ('hierarchy',)

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
        for y in (6,20,34):
         self.rect('node-'+str(y),6,y,23,8)
         self.add_line('link-'+str(y),(29,y+4),(42,y+4))
        self.add_polyline('bracket',(42,4),(42,38))

# Exact-drawing exception authorized by the user; original QA findings remain available.
Drawing.exception = {'reason': 'Three outlined list boxes and a right bracket require compact vertical spacing and short actual connector joins. Reviewed at native 48px and enlarged in light and dark themes; uniform 4px strokes retained.', 'approved_by': 'user (delegated visual exception approval in this request)', 'approved_on': '2026-09-29', 'svg_sha256': '76d5a5074be9eabe58dcf2acf4110954a9c0e1915ca80915f8ded0ccd77e68d1'}
