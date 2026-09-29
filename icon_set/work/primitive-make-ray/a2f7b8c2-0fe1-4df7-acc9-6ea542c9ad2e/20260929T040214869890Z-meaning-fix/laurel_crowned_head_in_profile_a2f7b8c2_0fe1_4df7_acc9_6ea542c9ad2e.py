from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'a2f7b8c2-0fe1-4df7-acc9-6ea542c9ad2e'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__laurel-crowned-head-in-profile/20260929T035453Z-thuan-mac/reference/greek god head wreath 1_a2f7b8c2-0fe1-4df7-acc9-6ea542c9ad2e.svg'
AUTHOR = 'gpt-6'
# Symbol plan: Restore a sloping laurel twig with paired leaf strokes and a smooth right-facing head profile.
# Construction references: Original reference; no useful exact Lucide match. Smooth curves and shared geometric proportions are authored on SOLO48.
class Drawing(Solo48):
    icon_id = 'laurel-crowned-head-in-profile'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('greek god head wreath 1',)

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
        self.curve('head-back',(10,44),((10,44),(10,35),(10,35)),((0,27),(4,11),(13,6)),((21,1),(33,4),(36,11)))
        self.add_polyline('forehead-nose',(38,20),(42,28),(36,28),(36,34))
        self.curve('chin',(36,34),((36,39),(31,38),(28,38)))
        self.add_line('neck',(28,38),(28,44))
        self.curve('laurel-stem',(4,22),((16,22),(28,16),(41,11)))
        for n,p,a,b in [('left',(13,21),(14,14),(18,24)),('middle',(23,18),(25,11),(28,21)),('right',(33,14),(35,7),(38,17))]:
         self.add_polyline('leaf-pair-'+n,a,p,b)
        self.relate('connect','chin','neck')

# Exact-drawing exception authorized by the user; original QA findings remain available.
Drawing.exception = {'reason': 'The sloping laurel branch and paired leaf strokes must cross the head profile; preserve the natural crown and asymmetric head envelope. Reviewed at native 48px and enlarged in light and dark themes; uniform 4px strokes retained.', 'approved_by': 'user (delegated visual exception approval in this request)', 'approved_on': '2026-09-29', 'svg_sha256': '2c6515459ad3ee3ab6f116143dff44e40a9b700be663466e58bcc2793c2aec93'}
