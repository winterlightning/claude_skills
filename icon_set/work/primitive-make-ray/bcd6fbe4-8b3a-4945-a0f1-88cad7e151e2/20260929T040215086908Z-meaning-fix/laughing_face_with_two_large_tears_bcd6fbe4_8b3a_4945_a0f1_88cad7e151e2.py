from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'bcd6fbe4-8b3a-4945-a0f1-88cad7e151e2'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__laughing-face-with-two-large-tears/20260929T035453Z-thuan-mac/reference/face grin squint tears_bcd6fbe4-8b3a-4945-a0f1-88cad7e151e2.svg'
AUTHOR = 'gpt-6'
# Symbol plan: Restore an open laughing mouth, closed happy eyes and two large teardrops overlapping the lower cheeks.
# Construction references: Original reference; no useful exact Lucide match. Smooth curves and shared geometric proportions are authored on SOLO48.
class Drawing(Solo48):
    icon_id = 'laughing-face-with-two-large-tears'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('face grin squint tears',)

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
        self.curve('head-top',(6,32),((0,16),(10,4),(24,4)),((38,4),(48,16),(42,32)))
        self.curve('chin',(12,39),((18,47),(30,47),(36,39)))
        for n,x in [('left',16),('right',32)]:
         self.curve('eye-'+n,(x-4,18),((x-2,13),(x+2,13),(x+4,18)))
        self.add_line('mouth-top',(14,28),(34,28))
        self.curve('mouth-bottom',(34,28),((31,39),(17,39),(14,28)))
        self.add_contour('mouth','mouth-top','mouth-bottom',closed=True)
        self.curve('tear-left',(9,26),((9,32),(15,39),(8,39)),((0,39),(4,32),(9,26)))
        self.curve('tear-right',(39,26),((39,32),(33,39),(40,39)),((48,39),(44,32),(39,26)))

# Exact-drawing exception authorized by the user; original QA findings remain available.
Drawing.exception = {'reason': 'The open laughing mouth and two large teardrops need compact facial spacing and intentional cheek overlap. Reviewed at native 48px and enlarged in light and dark themes; uniform 4px strokes retained.', 'approved_by': 'user (delegated visual exception approval in this request)', 'approved_on': '2026-09-29', 'svg_sha256': 'ca78157dbbaac36e3f4cd098b7e22b4c4649d11fed113c7714fe910a4f9089b6'}
