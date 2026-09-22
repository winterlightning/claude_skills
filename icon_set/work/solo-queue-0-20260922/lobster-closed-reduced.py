'Lobster with paired claws, antennae, three legs per side and fan tail. Source claw type and segmentation must be retained at native review; no generic insect substitution.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape VRECT_L uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f4812ef0-fce6-4380-9124-384916ee103d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_13/crawdad_f4812ef0-fce6-4380-9124-384916ee103d.svg'
AUTHOR = 'gpt-6-astra'

class Drawing(Solo48):
    icon_id = 'lobster-with-pointed-closed-claws'
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

        # Whole bilateral layout is owned by the body and arm attachment nodes.
        path('body',(20,24),[(20,16),((28,16),4,4,True),(28,24),(28,32),(28,36),((20,36),4,4,True),(20,32),(20,24)],True)
        for side in (-1,1):
            x=lambda a:24+side*a
            bez(f'claw{side}',(x(12),20),((x(20),18),(x(20),12),(x(16),8)),((x(12),12),(x(12),16),(x(12),20)))
            line(f'arm{side}',(x(4),24),(x(12),20));join(f'arm{side}','body');join(f'arm{side}',f'claw{side}')
            poly(f'leg{side}',(x(4),32),(x(14),30),(x(20),34));join(f'leg{side}','body')
        line('segment',(20,32),(28,32));join('segment','body')
