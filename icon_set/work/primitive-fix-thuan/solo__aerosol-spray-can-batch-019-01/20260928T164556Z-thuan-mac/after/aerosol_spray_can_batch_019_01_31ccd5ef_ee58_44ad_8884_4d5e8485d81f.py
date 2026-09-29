"""spray can.
Before review: The can was squat and the spray marks were uneven, unlike the tall reference can.
Feedback: Manual fix request
Revision: Lengthened the can, rounded its shoulder and nozzle, and made two balanced outward spray rays.
Construction: Lucide spray-can: distinct nozzle, body and spray hierarchy.
Plan: coherent named contours; shared dimensions for mirrored or repeated parts.
SOLO48 VRECT_L; 4px stroke. Native visual review required before acceptance.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '31ccd5ef-ee58-44ad-8884-4d5e8485d81f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__aerosol-spray-can-batch-019-01/20260928T164556Z-thuan-mac/reference/spray can_31ccd5ef-ee58-44ad-8884-4d5e8485d81f.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = 'aerosol-spray-can-batch-019-01'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('spray', 'can')
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

        rounded('can',8,14,28,44,5)
        path('nozzle',(14,14),[(14,6),((16,4),2,2,True),(20,4),((22,6),2,2,True),(22,14)])
        join('can','nozzle')
        line('spray-upper',(32,9),(40,5))
        line('spray-lower',(36,17),(40,20))
