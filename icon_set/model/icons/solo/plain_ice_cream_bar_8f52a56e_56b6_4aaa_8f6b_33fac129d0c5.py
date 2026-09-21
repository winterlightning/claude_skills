'Plain domed ice cream bar with centered rounded stick. Lucide popsicle informs coherent rounded body; preserve upright source orientation.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape VRECT_M uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8f52a56e-56b6-4aaa-8f6b-33fac129d0c5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_29/paddle_8f52a56e-56b6-4aaa-8f6b-33fac129d0c5.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'plain-ice-cream-bar'
    keyshape = Keyshape.VRECT_M
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

        path('ice',(10,18),[((38,18),14,14,True),(38,28),((32,34),6,6,True),(16,34),((10,28),6,6,True),(10,18)],True)
        path('stick',(20,34),[(20,40),((28,40),4,4,False),(28,34)])
        join('ice','stick')
