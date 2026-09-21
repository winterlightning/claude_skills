'Physical house carried on flatbed: one scene, not an applied modifier. Two wheels, left cab and gabled payload retained.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape HRECT_L uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5fda1d00-7833-4fcb-89e8-8b235809140b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_32/real estate truck house_5fda1d00-7833-4fcb-89e8-8b235809140b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'truck-carrying-a-house'
    keyshape = Keyshape.HRECT_L
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

        poly('cab',(4,36),(4,24),(8,20),(16,20))
        poly('house',(16,28),(16,20),(16,18),(30,8),(44,18),(44,28),(32,28),(24,28),(16,28))
        poly('chassis-left',(4,36),(8,36));line('chassis-middle',(16,36),(32,36));poly('chassis-right',(40,36),(44,36),(44,28))
        circle('wheel-left',12,36,4);circle('wheel-right',36,36,4)
        path('door',(24,28),[(24,24),((32,24),4,4,True),(32,28)])
        join('cab','house');join('door','house');join('cab','chassis-left');join('house','chassis-right')
        join('chassis-left','wheel-left');join('chassis-middle','wheel-left');join('chassis-middle','wheel-right');join('chassis-right','wheel-right')
