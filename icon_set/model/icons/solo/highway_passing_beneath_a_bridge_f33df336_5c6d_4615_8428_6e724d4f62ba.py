'Overpass interrupts road and center lane; double stripe becomes one.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape SQUARE uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f33df336-5c6d-4615-8428-6e724d4f62ba'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_33/route highway_f33df336-5c6d-4615-8428-6e724d4f62ba.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'highway-passing-beneath-a-bridge'
    keyshape = Keyshape.SQUARE
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

        line('bridge-top',(6,18),(42,18));line('bridge-bottom',(6,26),(42,26))
        for side in (-1,1):
            line(f'roadtop{side}',(24+side*8,6),(24+side*10,18));join('bridge-top',f'roadtop{side}')
            line(f'roadbottom{side}',(24+side*11,26),(24+side*17,42));join('bridge-bottom',f'roadbottom{side}')
        line('lane-top',(24,6),(24,18));join('lane-top','bridge-top');line('lane-bottom',(24,26),(24,42));join('lane-bottom','bridge-bottom')
