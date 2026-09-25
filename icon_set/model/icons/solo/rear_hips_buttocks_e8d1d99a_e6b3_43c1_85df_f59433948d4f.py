'Rear hips with cropped waist, paired buttock folds and central crease. Mirrored anatomy, no detached human head.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape SQUARE uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e8d1d99a-e6b3-43c1-85df-f59433948d4f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_31/posterior_e8d1d99a-e6b3-43c1-85df-f59433948d4f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'rear-hips-buttocks'
    keyshape = Keyshape.SQUARE
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

        poly('waist',(12,6),(36,6))
        for side in (-1,1):
            x=lambda v:24+side*v
            bez(f'hip{side}',(x(12),6),((x(10),19),(x(18),20),(x(18),30)),((x(18),36),(x(15),39),(x(14),42)))
            bez(f'fold{side}',(24,30),((x(1),35),(x(6),35),(x(8),34)))
            join('waist',f'hip{side}')
        line('crease',(24,22),(24,42));join('crease','fold-1');join('crease','fold1');join('fold-1','fold1')
