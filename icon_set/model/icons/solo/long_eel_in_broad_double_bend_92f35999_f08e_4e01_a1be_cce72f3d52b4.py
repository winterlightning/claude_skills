'Long left-facing eel with two broad bends and rounded thick tail. Omit tiny eye; preserve the winding silhouette and head direction.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape SQUARE uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '92f35999-f08e-4e01-a1be-cce72f3d52b4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_16/elver_92f35999-f08e-4e01-a1be-cce72f3d52b4.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'long-eel-in-broad-double-bend'
    keyshape = Keyshape.VRECT_L
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

        path('eel',(8,8),[(16,4),(28,4),((40,16),12,12,True),((28,28),12,12,True),(20,28),((20,36),4,4,False),(36,36),((36,44),4,4,True),(20,44),((8,32),12,12,True),((20,20),12,12,True),(28,20),((28,12),4,4,False),(16,12),(8,8)],True)
