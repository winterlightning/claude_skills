"""seat.
Before review: The open single-stroke back and short seat lost the upholstered shell and armrest of the reference.
Feedback: Manual fix request
Revision: Restored an outlined swept back and rounded seat, a separate armrest, and slim splayed legs.
Construction: Lucide armchair: rounded upholstery and leg hierarchy; source controls side view.
Plan: coherent named contours; shared dimensions for mirrored or repeated parts.
SOLO48 VRECT_L; 4px stroke. Native visual review required before acceptance.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '9b1829ef-5061-46d7-b449-7b512faf7f77'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__armchair-side-profile-swept-back/20260928T164556Z-thuan-mac/reference/seat_9b1829ef-5061-46d7-b449-7b512faf7f77.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = 'armchair-side-profile-swept-back'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('seat',)
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

        path('shell',(8,7),[((14,6),4,4,True),(21,29),((25,32),4,4,False),(36,32),((40,36),4,4,True),((36,40),4,4,True),(22,40),((14,33),9,9,True),(8,7)],True)
        path('arm',(18,21),[(29,21),((35,27),6,6,True),(36,32)]);join('arm','shell')
        line('leg-front',(22,40),(20,44));line('leg-rear',(35,40),(37,44))
        join('leg-front','shell');join('leg-rear','shell')
