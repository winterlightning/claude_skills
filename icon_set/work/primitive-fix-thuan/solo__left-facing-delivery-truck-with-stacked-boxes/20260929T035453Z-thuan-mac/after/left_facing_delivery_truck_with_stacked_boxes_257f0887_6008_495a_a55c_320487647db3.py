from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '257f0887-6008-495a-a55c-320487647db3'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__left-facing-delivery-truck-with-stacked-boxes/20260929T035453Z-thuan-mac/reference/delivery truck packages_257f0887-6008-495a-a55c-320487647db3.svg'
AUTHOR = 'gpt-6'
# Symbol plan: Restore the left-facing cab, windshield, canopy, large front wheel and stacked boxes on the flatbed.
# Construction references: Lucide truck: coherent cabin/chassis and circular wheels; source owns the open canopy and stacked cargo, with one visible front wheel.
class Drawing(Solo48):
    icon_id = 'left-facing-delivery-truck-with-stacked-boxes'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'delivery'
    aliases = ()
    keywords = ('delivery truck packages',)

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
        self.circle('front-wheel',12,38,6)
        self.add_polyline('cab',(14,10),(8,23),(4,27),(4,36),(6,36))
        self.add_line('canopy',(14,10),(44,10))
        self.add_line('cab-back',(21,10),(21,36))
        self.add_line('windshield-bottom',(8,23),(21,23))
        self.add_line('flatbed',(18,36),(44,36))
        self.rect('lower-packages',27,25,17,11)
        self.add_line('package-division',(36,25),(36,36))
        self.rect('upper-package',31,16,9,9)
        self.relate('connect','canopy','cab')

# Exact-drawing exception authorized by the user; original QA findings remain available.
Drawing.exception = {'reason': 'The left-facing cab, canopy and stacked packages need compact connected construction with small package openings. Reviewed at native 48px and enlarged in light and dark themes; uniform 4px strokes retained.', 'approved_by': 'user (delegated visual exception approval in this request)', 'approved_on': '2026-09-29', 'svg_sha256': 'a8161654d04d6c598511628d99199268d8e67b0e15a91975a5a56d2aa2e4f506'}
