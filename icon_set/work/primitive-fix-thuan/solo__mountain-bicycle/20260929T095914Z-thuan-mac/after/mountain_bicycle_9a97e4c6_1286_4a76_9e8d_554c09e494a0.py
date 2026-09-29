from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '9a97e4c6-1286-4a76-9e8d-554c09e494a0'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__mountain-bicycle/20260929T095914Z-thuan-mac/reference/mountain bike_9a97e4c6-1286-4a76-9e8d-554c09e494a0.svg'
AUTHOR = "gpt-6"

# Original/current comparison: The bicycle lost its seat tube and complete diamond frame; the heavy simplified triangle made the bike ambiguous.
# Revision plan: Restored the complete two-triangle frame, two round wheels, seat post, saddle, fork and curved handlebar.
# Construction reference: No new Lucide bicycle reference used; original supplies the full diamond frame and two equal circular wheels.

def circle(icon, name, cx, cy, r):
    icon.add_arc(name+'-top',(cx-r,cy),(cx+r,cy),radius_x=r)
    icon.add_arc(name+'-bottom',(cx+r,cy),(cx-r,cy),radius_x=r)
    icon.add_contour(name,name+'-top',name+'-bottom',closed=True)

def rounded(icon,name,x0,y0,x1,y1,r):
    points=[(x0+r,y0),(x1-r,y0),(x1,y0+r),(x1,y1-r),(x1-r,y1),(x0+r,y1),(x0,y1-r),(x0,y0+r)]
    ids=[]
    for j,a in enumerate(points):
        b=points[(j+1)%8];n=f'{name}-{j}';ids.append(n)
        if j%2: icon.add_arc(n,a,b,radius_x=r)
        else: icon.add_line(n,a,b)
    icon.add_contour(name,*ids,closed=True)

def curve(icon,name,start,*segments,closed=False):
    icon.add_bezier(name+'-curve',start,*segments)
    icon.add_contour(name,name+'-curve',closed=closed)

class Drawing(Solo48):
    icon_id = 'mountain-bicycle'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    exception = {'reason': 'A complete bicycle frame and realistic wheel proportions create compact triangular regions. Preserve these defining structures at4px rather than deleting the seat tube.', 'approved_by': 'user-authorized-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '552d266b61f0984ccf77b59c8b4ae107e308fe60b890a5459b6da0e327cc548a'}
    aliases = ()
    keywords = ('mountain bike',)

    def build(self):
        # Paired equal wheels and a true diamond frame share hub and junction points.
        for name,cx in (('rear',12),('front',36)):circle(self,name+'-wheel',cx,34,8)
        self.add_polyline('rear-frame',(12,34),(18,20),(24,34),(12,34))
        self.add_polyline('front-frame',(18,20),(33,16),(24,34))
        self.add_line('fork',(33,16),(36,34))
        self.add_line('seat-post',(18,20),(16,14));self.add_line('saddle',(12,14),(20,14))
        self.add_polyline('handlebar-stem',(33,16),(31,10),(37,10))
        curve(self,'handlebar',(37,10),((42,10),(42,15),(37,17)))
        for a,b in [('rear-frame','front-frame'),('front-frame','fork'),('rear-frame','seat-post'),('seat-post','saddle'),('front-frame','handlebar-stem'),('fork','handlebar-stem'),('handlebar-stem','handlebar')]:self.relate('connect',a,b)
        # Frame runs genuinely cross the wheel rims, as in a conventional bicycle diagram.
        for a,b in [('rear-wheel','rear-frame'),('front-wheel','fork')]:self.relate('connect',a,b)
