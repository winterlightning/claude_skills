"""watch time.
Before review: The rejected clock omitted all four hour markers and used an overly short hand pair.
Feedback: Manual fix request
Revision: Restored four cardinal hour markers and a clear 10:08 hand pair inside a circular face.
Construction: Lucide clock: concentric face and joined hand pair.
Plan: coherent named contours; shared dimensions for mirrored or repeated parts.
SOLO48 CIRCLE; 4px stroke. Native visual review required before acceptance.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '02239e41-5c08-5c59-a65d-1a4042e45034'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__analog-clock/20260928T164556Z-thuan-mac/reference/watch time_02239e41-5c08-5c59-a65d-1a4042e45034.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = 'analog-clock'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('watch', 'time')
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

        circle('face',24,24,20)
        for name,a,b in [('north',(24,10),(24,12)),('east',(36,24),(38,24)),('south',(24,36),(24,38)),('west',(10,24),(12,24))]:line(name,a,b)
        poly('hands',(17,19),(24,24),(32,16))
