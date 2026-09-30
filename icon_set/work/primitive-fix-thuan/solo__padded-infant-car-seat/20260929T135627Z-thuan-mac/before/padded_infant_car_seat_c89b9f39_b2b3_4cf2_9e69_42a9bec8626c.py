'Deep padded infant seat with broad protective rim, two inner pads and central divider. No useful exact Lucide match.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape SQUARE uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c89b9f39-b2b3-4cf2-9e69-42a9bec8626c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_05/baby family baby seat car extention_c89b9f39-b2b3-4cf2-9e69-42a9bec8626c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'padded-infant-car-seat'
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
            if rad==0:
                self.add_polyline(name,(l,t),(r,t),(r,b),(l,b),(l,t)); return
            path(name,(l+rad,t),[(r-rad,t),((r,t+rad),rad,rad,True),(r,b-rad),((r-rad,b),rad,rad,True),(l+rad,b),((l,b-rad),rad,rad,True),(l,t+rad),((l+rad,t),rad,rad,True)],True)
        def line(name,a,b): self.add_line(name,a,b)
        def poly(name,*points): self.add_polyline(name,*points)
        def join(*names): self.relate('connect',*names)

        def bez(name,start,*segments): self.add_bezier(name,start,*segments)

        path('rim',(6,28),[(6,16),((16,6),10,10,True),(32,6),((42,16),10,10,True),(42,28),(42,32),((32,42),10,10,True),(16,42),((6,32),10,10,True),(6,28)],True)
        bez('padding',(16,16),((16,23),(15,32),(24,32)),((33,32),(32,23),(32,16)))
        line('divide',(24,24),(24,32));join('padding','divide')
