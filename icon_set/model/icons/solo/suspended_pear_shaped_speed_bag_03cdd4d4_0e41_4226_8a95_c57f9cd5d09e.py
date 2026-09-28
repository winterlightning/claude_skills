'Pear bag, mount and central seam. Other seam omitted.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape VRECT_M uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '03cdd4d4-0e41-4226-8a95-c57f9cd5d09e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_07/boxing bag small_03cdd4d4-0e41-4226-8a95-c57f9cd5d09e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'suspended-pear-shaped-speed-bag'
    keyshape = Keyshape.VRECT_M
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
            path(name,(l+rad,t),[(r-rad,t),((r,t+rad),rad,rad,True),(r,b-rad),((r-rad,b),rad,rad,True),(l+rad,b),((l,b-rad),rad,rad,True),(l,t+rad),((l+rad,t),rad,rad,True)],True)
        def line(name,a,b): self.add_line(name,a,b)
        def poly(name,*points): self.add_polyline(name,*points)
        def join(*names): self.relate('connect',*names)

        line('mount',(10,4),(38,4));line('neck',(24,4),(24,14));join('mount','neck')
        self.add_bezier('bag',(24,14),((20,14),(10,26),(10,32)),((10,48),(38,48),(38,32)),((38,26),(28,14),(24,14)))
        join('neck','bag');line('seam',(24,26),(24,35))
