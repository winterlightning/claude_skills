'Brush beside a six-well palette (two columns, three rows). Lucide paintbrush informs bristles and ferrule. Wells reduced to six small marks while preserving their count and arrangement.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape SQUARE uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3778c097-0bd8-40c7-9e69-1cc141e803e8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_26/make up brush set_3778c097-0bd8-40c7-9e69-1cc141e803e8.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'makeup-brush-beside-six-well-palette'
    keyshape = Keyshape.HRECT_L
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
            if rad==0:
                self.add_polyline(name,(l,t),(r,t),(r,b),(l,b),(l,t)); return
            path(name,(l+rad,t),[(r-rad,t),((r,t+rad),rad,rad,True),(r,b-rad),((r-rad,b),rad,rad,True),(l+rad,b),((l,b-rad),rad,rad,True),(l,t+rad),((l+rad,t),rad,rad,True)],True)
        def line(name,a,b): self.add_line(name,a,b)
        def poly(name,*points): self.add_polyline(name,*points)
        def join(*names): self.relate('connect',*names)

        def bez(name,start,*segments): self.add_bezier(name,start,*segments)

        path('bristles',(4,20),[(4,12),((12,12),4,4,True),(12,20),(4,20)],True)
        path('brush',(4,20),[(4,36),((12,36),4,4,False),(12,20)]);join('brush','bristles')
        box('palette',20,8,44,40,0)
        for y in (16,24,32):
            for x in (28,36):self.add_dot(f'well{x}-{y}',(x,y))
