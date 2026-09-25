'Three paired spinal processes repeated around shared central axis. Preserve central column and rounded joining vocabulary.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape VRECT_L uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '397b923f-981a-4d9d-b36e-93d6027a9a51'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_05/backbone_397b923f-981a-4d9d-b36e-93d6027a9a51.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'spinal-column-with-three-paired-processes'
    keyshape = Keyshape.VRECT_L
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

        points=[(40,4),(40,12),(28,12),(28,20),(40,20),(40,28),(28,28),(28,36),(40,36),(40,44),(8,44),(8,36),(20,36),(20,28),(8,28),(8,20),(20,20),(20,12),(8,12),(8,4)]
        radius=2
        corners=[]
        for index,p in enumerate(points):
            before=points[index-1];after=points[(index+1)%len(points)]
            def direction(a,b):
                return tuple(0 if y==x else (1 if y>x else -1) for x,y in zip(a,b))
            u=direction(p,before);v=direction(p,after)
            entry=tuple(p[j]+radius*u[j] for j in (0,1));leave=tuple(p[j]+radius*v[j] for j in (0,1))
            corners.append((entry,leave,u[0]*v[1]-u[1]*v[0]<0))
        steps=[]
        for entry,leave,sweep in corners:
            steps.extend([entry,(leave,radius,radius,sweep)])
        path('column',corners[-1][1],steps,True)
