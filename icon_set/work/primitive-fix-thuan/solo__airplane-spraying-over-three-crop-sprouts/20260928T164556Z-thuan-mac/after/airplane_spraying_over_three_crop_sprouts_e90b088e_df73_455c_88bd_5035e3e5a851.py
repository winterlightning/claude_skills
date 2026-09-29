"""soil pollution plane.
Before review: The plane looked like a crown and the crops were short chevrons with no ground or stems.
Feedback: Manual fix request
Revision: Restored a curved side-view fuselage and rounded swept wing, visible spray strokes and three stemmed sprouts. Omitted the ground line to keep the plants separated at 48px.
Construction: Lucide plane: simplified aircraft silhouette; original controls side-view arrangement.
Plan: coherent named contours; shared dimensions for mirrored or repeated parts.
SOLO48 SQUARE; 4px stroke. Native visual review required before acceptance.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'e90b088e-df73-455c-88bd-5035e3e5a851'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__airplane-spraying-over-three-crop-sprouts/20260928T164556Z-thuan-mac/reference/soil pollution plane_e90b088e-df73-455c-88bd-5035e3e5a851.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = 'airplane-spraying-over-three-crop-sprouts'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('soil', 'pollution', 'plane')
    def build(self):

        def path(name, start, steps, closed=False):
            here=start; members=[]
            for i,step in enumerate(steps):
                ident=f'{name}-{i}'
                if len(step)==2:
                    self.add_line(ident,here,step); end=step
                elif step[0]=='C':
                    _,end,c1,c2=step
                    self.add_bezier(ident,here,(c1,c2,end))
                else:
                    end,rx,ry,sweep=step
                    self.add_arc(ident,here,end,radius_x=rx,radius_y=ry,sweep=sweep)
                here=end;members.append(ident)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[((x+r,y),r,r,True),((x-r,y),r,r,True)],True)
        def rounded(name,l,t,r,b,k):
            path(name,(l+k,t),[(r-k,t),((r,t+k),k,k,True),(r,b-k),((r-k,b),k,k,True),(l+k,b),((l,b-k),k,k,True),(l,t+k),((l+k,t),k,k,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        path('plane',(6,6),[('C',(15,14),(9,6),(10,14)),(21,14),('C',(28,6),(23,10),(26,6)),('C',(32,14),(30,6),(31,10)),(36,14),((42,19),6,5,True),((36,24),6,5,True),(22,24),(8,20),('C',(6,17),(6,20),(6,19)),(6,6)],True)
        line('spray-left',(20,29),(18,31));line('spray-right',(30,29),(28,31))
        for j,x in enumerate((10,24,38)):
            poly(f'crop-{j}',(x-4,36),(x,40),(x+4,36))
            line(f'stem-{j}',(x,40),(x,42));join(f'crop-{j}',f'stem-{j}')

# User explicitly delegated quality-preserving visual exceptions for this batch.
Drawing.exception = {'reason': 'A complete spraying-aircraft scene needs three vertical levels. The fuselage, two spray marks and three separate stemmed sprouts remain readable at 48px with local 1–3px ink gaps. Ground line omitted to reduce density.', 'approved_by': 'gpt-6 under user-delegated exception authority', 'approved_on': '2026-09-28', 'svg_sha256': '66fa2a0bcb6f0c297d15581b9565ee89fab142cdfbe6a719377f5decdd5fef5f'}
