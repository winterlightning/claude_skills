'Full-body girl doll with bob hair, blank circular face, dress, two arms and two legs. Use shared human reference vocabulary; detached head-to-own-dress gap4ink at headbottom20/bodytop28 required in final review.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape VRECT_L uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2f051532-a430-48a9-8c8d-3cd972e7789a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_15/doll_2f051532-a430-48a9-8c8d-3cd972e7789a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'girl-doll-with-bob-hair-and-dress'
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

        path('face',(16,12),[((32,12),8,8,False)])
        bez('hair',(12,20),((12,10),(14,4),(24,4)),((34,4),(36,10),(36,20)))
        bez('fringe',(16,12),((19,12),(21,10),(24,8)),((27,10),(29,12),(32,12)));join('face','fringe')
        bez('dress',(24,28),((20,28),(16,34),(16,36)),((20,39),(28,39),(32,36)),((32,34),(28,28),(24,28)))
        for side in (-1,1):
            x=lambda a:24+side*a
            line(f'arm{side}',(x(3),30),(x(16),34));line(f'leg{side}',(x(5),38),(x(5),44));join('dress',f'arm{side}');join('dress',f'leg{side}')
