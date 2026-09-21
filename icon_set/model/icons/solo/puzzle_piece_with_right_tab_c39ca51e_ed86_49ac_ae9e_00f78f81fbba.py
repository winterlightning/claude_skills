'Lucide puzzle informs rounded tabs and sockets. Preserve only right outward tab and lower inward socket; top and left remain plain.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape SQUARE uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c39ca51e-ed86-49ac-ae9e-00f78f81fbba'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_32/puzzle piece_c39ca51e-ed86-49ac-ae9e-00f78f81fbba.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'puzzle-piece-with-right-tab'
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
            if rad==0:
                self.add_polyline(name,(l,t),(r,t),(r,b),(l,b),(l,t)); return
            path(name,(l+rad,t),[(r-rad,t),((r,t+rad),rad,rad,True),(r,b-rad),((r-rad,b),rad,rad,True),(l+rad,b),((l,b-rad),rad,rad,True),(l,t+rad),((l+rad,t),rad,rad,True)],True)
        def line(name,a,b): self.add_line(name,a,b)
        def poly(name,*points): self.add_polyline(name,*points)
        def join(*names): self.relate('connect',*names)

        def bez(name,start,*segments): self.add_bezier(name,start,*segments)

        path('body',(10,6),[(28,6),((32,10),4,4,True),(32,18)])
        bez('tab',(32,18),((35,15),(42,16),(42,24)),((42,32),(35,33),(32,30)))
        path('lower',(32,30),[(32,38),((28,42),4,4,True),(23,42),(23,38),((15,38),4,4,False),(15,42),(10,42),((6,38),4,4,True),(6,10),((10,6),4,4,True)])
        join('body','tab');join('tab','lower');join('lower','body')
