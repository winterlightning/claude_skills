from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'e7eb9b49-84dd-4eea-9f75-a357ae86c92a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__layered-pinecone-stem/20260929T035453Z-thuan-mac/reference/pinecone_e7eb9b49-84dd-4eea-9f75-a357ae86c92a.svg'
AUTHOR = 'gpt-6'
# Symbol plan: Restore overlapping pointed scales, rounded lower lobes and the short stem.
# Construction references: Original reference; no useful exact Lucide match. Smooth curves and shared geometric proportions are authored on SOLO48.
class Drawing(Solo48):
    icon_id = 'layered-pinecone-stem'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('pinecone',)

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
        self.curve('top-scale',(15,13),((17,9),(20,6),(24,4)),((28,6),(31,9),(33,13)))
        self.curve('middle-left',(10,23),((10,19),(10,15),(15,11)),((20,13),(22,16),(24,19)))
        self.curve('middle-right',(38,23),((38,19),(38,15),(33,11)),((28,13),(26,16),(24,19)))
        self.add_polyline('center-scale',(17,26),(24,19),(31,26))
        self.curve('lower-outline',(7,22),((7,35),(12,40),(24,40)),((36,40),(41,35),(41,22)))
        self.curve('lower-scale-top',(7,22),((12,23),(20,28),(24,33)),((28,28),(36,23),(41,22)))
        self.add_line('stem',(24,33),(24,44))
        self.relate('connect','lower-outline','lower-scale-top');self.relate('connect','lower-scale-top','stem')

# Exact-drawing exception authorized by the user; original QA findings remain available.
Drawing.exception = {'reason': 'The overlapping pointed scales and rounded lower lobes need compact nested spacing and the pinecone silhouette. Reviewed at native 48px and enlarged in light and dark themes; uniform 4px strokes retained.', 'approved_by': 'user (delegated visual exception approval in this request)', 'approved_on': '2026-09-29', 'svg_sha256': 'b5c580ef488511b1b61f78a6e001a812a45687b797e4da6a21112a8470a3dacf'}
