'Open lower face and continuous neck curving into shoulders. Human anatomy without detached head, no complete face invented.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape HRECT_L uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd0c187a1-979e-457e-b5a4-f17efbd65195'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_28/neck_d0c187a1-979e-457e-b5a4-f17efbd65195.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'neck-shoulder-outline'
    keyshape = Keyshape.HRECT_L
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
            if rad==0:
                self.add_polyline(name,(l,t),(r,t),(r,b),(l,b),(l,t)); return
            path(name,(l+rad,t),[(r-rad,t),((r,t+rad),rad,rad,True),(r,b-rad),((r-rad,b),rad,rad,True),(l+rad,b),((l,b-rad),rad,rad,True),(l,t+rad),((l+rad,t),rad,rad,True)],True)
        def line(name,a,b): self.add_line(name,a,b)
        def poly(name,*points): self.add_polyline(name,*points)
        def join(*names): self.relate('connect',*names)

        def bez(name,start,*segments): self.add_bezier(name,start,*segments)

        bez('jaw',(12,8),((12,16),(12,18),(16,20)),((20,22),(28,22),(32,20)),((36,18),(36,16),(36,8)))
        for side in (-1,1):
            x=lambda a:24+side*a
            bez(f'neck{side}',(x(8),20),((x(8),28),(x(8),31),(x(14),32)),((x(18),33),(x(20),36),(x(20),40)))
            join('jaw',f'neck{side}')
