'Open front hooded cloak with symmetrical panels and hood opening.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape VRECT_L uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a31f3f41-e636-492d-ad83-a82ed5593583'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_11/cloak_a31f3f41-e636-492d-ad83-a82ed5593583.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'open-front-hooded-cloak'
    keyshape = Keyshape.VRECT_L
    category = "objects"
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

        path('hood',(12,28),[(8,24),(8,20),((40,20),16,16,True),(40,24),(36,28)])
        poly('cloak',(12,28),(8,44),(24,38),(40,44),(36,28));join('hood','cloak')
        self.add_bezier('opening',(24,25),((15,19),(17,12),(24,12)),((31,12),(33,19),(24,25)))
        line('front',(24,25),(24,38));join('front','opening');join('front','cloak')
