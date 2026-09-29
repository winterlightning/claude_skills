from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'f9e55377-8da9-5927-845b-403bea7db251'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__layered-crescent-croissant/20260929T035453Z-thuan-mac/reference/breakfast croissant_f9e55377-8da9-5927-845b-403bea7db251.svg'
AUTHOR = 'gpt-6'
# Symbol plan: Restore the plump diagonal pastry, curled tapered ends and curved seams dividing the rolled sections.
# Construction references: Lucide croissant: plump rolled central body and rounded tapered ends; source owns the diagonal direction and full pastry mass.
class Drawing(Solo48):
    icon_id = 'layered-crescent-croissant'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'food'
    aliases = ()
    keywords = ('breakfast croissant',)

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
        self.curve('pastry',(12,27),((6,21),(2,23),(4,29)),((6,34),(11,39),(22,41)),((29,43),(36,37),(40,31)),((45,25),(46,13),(40,5)),((37,1),(36,8),(35,12)),((33,12),(31,13),(31,16)),((24,12),(15,17),(17,21)),((15,22),(13,23),(12,27)))
        self.curve('left-tip-seam',(12,27),((10,32),(11,36),(14,39)))
        self.curve('left-roll',(17,21),((17,29),(19,35),(22,41)))
        self.curve('right-roll',(31,16),((36,20),(39,25),(40,31)))
        self.curve('right-tip-seam',(35,12),((40,11),(43,15),(44,20)))

# Exact-drawing exception authorized by the user; original QA findings remain available.
Drawing.exception = {'reason': 'The plump diagonal croissant needs its natural curved envelope and compact rolled seams rather than a forced rectangular fit. Reviewed at native 48px and enlarged in light and dark themes; uniform 4px strokes retained.', 'approved_by': 'user (delegated visual exception approval in this request)', 'approved_on': '2026-09-29', 'svg_sha256': 'bd1f93b07089526097b04c445ddd8faf1e24e00286fbb8a3a92f07475ece1f3f'}
