'Heavy C-clamp with broad upper handle and lower screw. Source mechanical arrangement retained, no generic wrench substitution.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape VRECT_L uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2cfa5d85-df72-45ce-be9f-4e4595f8f055'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_11/clamp_2cfa5d85-df72-45ce-be9f-4e4595f8f055.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'heavy-c-clamp-with-top-handle'
    keyshape = Keyshape.VRECT_L
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

        poly('handle',(8,4),(24,4),(40,4))
        path('clamp',(36,12),[(24,12),(16,12),((8,20),8,8,False),(8,28),((16,36),8,8,False),(28,36),(36,36)])
        line('top-post',(24,4),(24,12));join('top-post','clamp');join('top-post','handle')
        poly('screw',(28,24),(28,36),(28,44));join('screw','clamp')
        poly('pressure',(20,24),(28,24),(36,24));join('pressure','screw')
        poly('turn',(20,44),(28,44),(40,44));join('turn','screw')
