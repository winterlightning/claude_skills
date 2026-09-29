from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'a46a65c8-4a95-55ac-8668-317d0b3a148f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hierarchy-arched-branches/20260929T033507Z-thuan-mac/reference/hierarchy_a46a65c8-4a95-55ac-8668-317d0b3a148f.svg'
AUTHOR = 'gpt-6'
# Symbol plan: Separate the parent square above a broad rounded branch with three equally sized child squares.
# Construction references: No useful exact Lucide match; constructed from the original reference with smooth geometric contours.
class Drawing(Solo48):
    icon_id = 'hierarchy-arched-branches'
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
        self.rect('parent',19,4,10,10)
        for x in (4,19,34):self.rect('child-'+str(x),x,34,10,10)
        self.add_line('trunk',(24,14),(24,34))
        self.curve('branch',(9,34),((9,24),(15,23),(24,23)),((33,23),(39,24),(39,34)))

# Exact-drawing exception authorized by the user; original QA findings remain available.
Drawing.exception = {'reason': 'The parent and three outlined child nodes require compact node spacing and connected arched branches. Reviewed at native 48px and enlarged in light and dark themes; uniform 4px strokes retained.', 'approved_by': 'user (delegated visual exception approval in this request)', 'approved_on': '2026-09-29', 'svg_sha256': '21a2fa13d7eff6b1a2342002cd79ceef4009bab9f50c12f25a38ca9160eea861'}
