'Broad poncho and hood with circular face curve; no invented facial detail.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape SQUARE uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b55bffa3-4279-4235-9ba3-a7ca76021d61'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_31/poncho_b55bffa3-4279-4235-9ba3-a7ca76021d61.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'figure-broad-rain-poncho'
    keyshape = Keyshape.SQUARE
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

        self.add_bezier('hood',(16,20),((16,12),(18,6),(24,6)),((30,6),(32,12),(32,20)))
        poly('poncho',(16,20),(6,34),(24,42),(42,34),(32,20));join('hood','poncho')
        self.add_arc('face',(16,20),(32,20),radius_x=8,sweep=False);join('hood','face');join('poncho','face')
