"""airbus.
Before review: The wings were blocky and the tail/nose proportion made the aircraft resemble a generic arrow.
Feedback: Manual fix request
Revision: Rebuilt slimmer swept wings, a longer fuselage and a rounded nose, preserving both wings and the rightward heading.
Construction: Lucide plane: coherent aircraft outline with swept wings.
Plan: coherent named contours; shared dimensions for mirrored or repeated parts.
SOLO48 HRECT_L; 4px stroke. Native visual review required before acceptance.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '3297cd8c-f784-4a07-8f3e-82b7e7146b94'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__airplane-right-facing-full-wings/20260928T164556Z-thuan-mac/reference/airbus_3297cd8c-f784-4a07-8f3e-82b7e7146b94.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = 'airplane-right-facing-full-wings'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('airbus',)
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

        path('plane',(4,18),[(7,18),(11,23),(20,23),(14,8),(18,8),(31,23),(39,23),((44,27),5,4,True),((39,31),5,4,True),(31,31),(18,40),(14,40),(20,31),(4,31),(6,25),(4,18)],True)
