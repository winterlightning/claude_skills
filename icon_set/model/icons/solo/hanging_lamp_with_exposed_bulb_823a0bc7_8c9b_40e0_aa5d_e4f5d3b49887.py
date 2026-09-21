'Symmetric pendant lamp with exposed bulb. Fitting merged into shade; Lucide lamp informs trapezoid.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape SQUARE uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '823a0bc7-8c9b-40e0-aa5d-e4f5d3b49887'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_10/ceiling_823a0bc7-8c9b-40e0-aa5d-e4f5d3b49887.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hanging-lamp-with-exposed-bulb'
    keyshape = Keyshape.SQUARE
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
            path(name,(l+rad,t),[(r-rad,t),((r,t+rad),rad,rad,True),(r,b-rad),((r-rad,b),rad,rad,True),(l+rad,b),((l,b-rad),rad,rad,True),(l,t+rad),((l+rad,t),rad,rad,True)],True)
        def line(name,a,b): self.add_line(name,a,b)
        def poly(name,*points): self.add_polyline(name,*points)
        def join(*names): self.relate('connect',*names)

        line('ceiling',(6,6),(42,6));line('cord',(24,6),(24,18));join('ceiling','cord')
        poly('shade',(16,18),(32,18),(42,32),(6,32),(16,18));join('shade','cord')
        self.add_arc('bulb',(14,32),(34,32),radius_x=10,sweep=False);join('bulb','shade')
