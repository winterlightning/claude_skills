'Loop, neck wrap and two loose tails; two wraps reduced to one.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape VRECT_M uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '50547aae-7288-4718-8be9-77e390938600'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_33/rope_50547aae-7288-4718-8be9-77e390938600.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'looped-rope-with-two-wraps'
    keyshape = Keyshape.VRECT_M
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

        self.add_bezier('loop',(18,24),((14,21),(10,18),(10,14)),((10,7),(16,4),(24,4)),((32,4),(38,7),(38,14)),((38,18),(34,21),(30,24)))
        box('wrap',14,24,34,32,4);join('loop','wrap')
        self.add_bezier('tail1',(19,32),((19,36),(18,41),(16,44)))
        self.add_bezier('tail2',(29,32),((29,36),(28,41),(26,44)))
        join('wrap','tail1');join('wrap','tail2')
