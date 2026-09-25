'Soap bottle with narrow collar and tall pump. Plain body and curved dispenser tips preserved.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape VRECT_L uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cf55fe94-21cd-4122-a6e1-2d0acb27fc81'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_26/lotion_cf55fe94-21cd-4122-a6e1-2d0acb27fc81.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'soap-bottle-with-tall-pump-stem'
    keyshape = Keyshape.VRECT_L
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
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

        box('body',8,24,40,44,6)
        poly('collar',(18,24),(18,16),(30,16),(30,24));join('body','collar')
        line('stem',(24,4),(24,16));join('stem','collar')
        bez('pump',(12,7),((12,4),(16,4),(24,4)),((32,4),(36,4),(36,7)));join('pump','stem')
