'Avatar construction from human_ref/user.svg: circular head radius8 and circular shoulders radius16, head bottom20/body top24 gives touching ink. Retain forehead bandage and triangular sling; avatar rules apply.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape VRECT_L uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '483f0053-0d76-4f90-9c4a-d241bc144520'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_05/bandage shoulder head_483f0053-0d76-4f90-9c4a-d241bc144520.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'person-with-head-bandage-and-arm-sling'
    keyshape = Keyshape.VRECT_L
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    human_construction = "bust"
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

        circle('head',24,12,8)
        path('shoulders',(8,44),[(8,40),((40,40),16,16,True),(40,44)])
        join('head','shoulders')
        line('bandage',(16,12),(32,12));join('head','bandage')
        poly('sling',(24,28),(16,44),(32,44),(24,28))
        line('suspension',(24,24),(24,28));join('suspension','sling');join('suspension','shoulders')
        poly('arm',(8,40),(16,40),(16,44));join('arm','shoulders');join('arm','sling')
