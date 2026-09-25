'Cab, separate wheels, articulated boom and bucket; hydraulics omitted.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape SQUARE uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9807802c-4263-4ed0-9917-9adc44389799'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_15/digger_9807802c-4263-4ed0-9917-9adc44389799.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'wheeled-excavator-with-raised-jointed-boom'
    keyshape = Keyshape.SQUARE
    category = "primitives-generate"
    def build(self):

        def path(name,start,steps,closed=False):
            members=[]; point=start
            for j,step in enumerate(steps):
                member=f'{name}-{j}'
                if len(step)==2:
                    self.add_line(member,point,step); point=step
                else:
                    end,rx,ry,sweep=step
                    self.add_arc(member,point,end,radius_x=rx,radius_y=ry,sweep=sweep); point=end
                members.append(member)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[((x+r,y),r,r,True),((x-r,y),r,r,True)],True)
        def box(name,l,t,r,b,rad=4):
            path(name,(l+rad,t),[(r-rad,t),((r,t+rad),rad,rad,True),(r,b-rad),((r-rad,b),rad,rad,True),(l+rad,b),((l,b-rad),rad,rad,True),(l,t+rad),((l+rad,t),rad,rad,True)],True)
        def line(name,a,b): self.add_line(name,a,b)
        def poly(name,*points): self.add_polyline(name,*points)
        def join(*names): self.relate('connect',*names)

        circle('wheel1',10,39,3);circle('wheel2',27,39,3);box('body',6,20,30,28,3)
        poly('cab',(10,20),(10,12),(21,12),(25,20));join('cab','body')
        poly('boom',(30,20),(39,6),(42,24));join('boom','body')
        path('bucket',(42,24),[(42,28),((34,28),4,4,True)]);join('bucket','boom')
