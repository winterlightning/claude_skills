'Seated right-facing marten with small ear, muzzle, rounded haunch and long tail along the ground. Omit eye and minor paw separations.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape HRECT_L uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e04399dd-8c7b-4564-82c6-c7d46f62fb42'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_26/marten_e04399dd-8c7b-4564-82c6-c7d46f62fb42.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'seated-marten-with-long-sweeping-tail'
    keyshape = Keyshape.HRECT_L
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
            if rad==0:
                self.add_polyline(name,(l,t),(r,t),(r,b),(l,b),(l,t)); return
            path(name,(l+rad,t),[(r-rad,t),((r,t+rad),rad,rad,True),(r,b-rad),((r-rad,b),rad,rad,True),(l+rad,b),((l,b-rad),rad,rad,True),(l,t+rad),((l+rad,t),rad,rad,True)],True)
        def line(name,a,b): self.add_line(name,a,b)
        def poly(name,*points): self.add_polyline(name,*points)
        def join(*names): self.relate('connect',*names)

        def bez(name,start,*segments): self.add_bezier(name,start,*segments)

        bez('animal',(4,32),((5,22),(10,18),(20,18)),((27,18),(27,14),(28,10)),((28,8),(28,8),(30,8)),((32,8),(34,10),(34,12)),((39,12),(40,14),(44,16)),((40,21),(37,19),(36,20)),((36,27),(31,29),(36,32)))
        line('feet',(24,32),(40,32));join('feet','animal')
        path('tail',(4,32),[(((12,40)),8,8,False),(30,40)]);join('tail','animal')
