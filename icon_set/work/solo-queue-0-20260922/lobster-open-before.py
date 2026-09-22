'Lobster with paired claws, antennae, three legs per side and fan tail. Source claw type and segmentation must be retained at native review; no generic insect substitution.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape VRECT_L uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '813ecb4a-07a5-40d2-a4dc-2d3842c2a9f0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_13/crayfish_813ecb4a-07a5-40d2-a4dc-2d3842c2a9f0.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'lobster-with-broad-open-pincers'
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

        box('body',19,18,29,34,5)
        for side in (-1,1):
            x=lambda a:24+side*a
            bez(f'antenna{side}',(x(4),18),((x(4),10),(x(5),6),(x(10),4)));join('body',f'antenna{side}')
            bez(f'claw{side}',(x(12),24),((x(16),20),(x(16),13),(x(14),10)),((x(11),15),(x(12),18),(x(12),18)))
            line(f'arm{side}',(x(5),27),(x(12),24));join('arm'+str(side),'body');join('arm'+str(side),'claw'+str(side))
            for j,y in enumerate((24,32,40)):
                poly(f'leg{side}-{j}',(x(5),20+j*8),(x(12),y),(x(16),y+2));join(f'leg{side}-{j}','body')
        bez('tail',(19,34),((20,37),(16,41),(20,44)),((22,44),(23,42),(24,42)),((25,42),(26,44),(28,44)),((32,41),(28,37),(29,34)));join('tail','body')
