'Left-facing slender pike with forked tail and upper/lower fins. Lucide fish informs fin/body construction; preserve source direction and long body.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape HRECT_M uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '602f9a81-4306-4859-94c6-dc6f92e2061c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_30/pike_602f9a81-4306-4859-94c6-dc6f92e2061c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'slender-swimming-pike'
    keyshape = Keyshape.HRECT_M
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

        bez('head',(4,24),((12,18),(18,18),(23,18)))
        poly('top',(23,18),(24,10),(34,10),(34,20),(33,20),(44,12),(40,24),(44,36),(33,28),(34,28),(34,38),(24,38),(23,30));join('top','head')
        bez('belly',(23,30),((16,32),(10,30),(4,24)));join('belly','head');join('belly','top')
        bez('gill',(16,19),((17,23),(16,27),(14,30)));join('gill','head');join('gill','belly')
