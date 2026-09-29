"""armchair modern.
Before review: The thin open back and arm stub removed the broad padded side profile of the original.
Feedback: Manual fix request
Revision: Reconstructed the high upholstered back, rounded arm and seat silhouette, with two splayed legs. Integrated the small front cushion into the outer contour to avoid an ink blob.
Construction: Lucide armchair: coherent padded outline and shared corner radii.
Plan: coherent named contours; shared dimensions for mirrored or repeated parts.
SOLO48 SQUARE; 4px stroke. Native visual review required before acceptance.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'b6056fc5-c043-545c-98cd-e53b7e9dbee5'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__armchair-side-view-high-back/20260928T164556Z-thuan-mac/reference/armchair modern_b6056fc5-c043-545c-98cd-e53b7e9dbee5.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = 'armchair-side-view-high-back'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('armchair', 'modern')
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

        path('shell',(6,34),[(8,24),('C',(14,20),(9,21),(11,20)),(25,20),((30,16),5,5,False),(34,8),('C',(37,6),(35,6),(36,6)),(42,6),(37,30),('C',(32,34),(36,33),(34,34)),(6,34)],True)
        line('front-leg',(14,34),(10,42));line('rear-leg',(31,34),(37,42));join('front-leg','shell');join('rear-leg','shell')
