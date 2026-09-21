'Isolated head with a tilted beret, short stem and nose. Keep circular facial construction and asymmetric hat; omit ears, eyebrows and tiny eyes.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape SQUARE uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7cff9acb-b392-436c-938a-eb1253c0aa34'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_27/mime_7cff9acb-b392-436c-938a-eb1253c0aa34.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'front-facing-man-with-tilted-beret'
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

        path('jaw',(10,28),[((38,28),14,14,False)])
        line('temple-left',(10,22),(10,28));line('temple-right',(38,22),(38,28));join('jaw','temple-left');join('jaw','temple-right')
        bez('beret',(6,20),((6,14),(18,10),(24,10)),((28,10),(31,10),(34,10)),((40,10),(42,14),(42,18)),((42,22),(40,22),(38,22)),((30,22),(18,22),(10,22)),((8,22),(6,22),(6,20)))
        join('beret','temple-left');join('beret','temple-right')
        line('stem',(24,6),(24,10));join('stem','beret')
