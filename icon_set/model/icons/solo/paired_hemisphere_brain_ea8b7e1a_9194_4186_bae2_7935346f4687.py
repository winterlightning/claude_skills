'Paired hemispheres with central seam and sparse folds. Lucide brain informs lobed contours and shared symmetry.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape SQUARE uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ea8b7e1a-9194-4186-bae2-7935346f4687'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_08/bran_ea8b7e1a-9194-4186-bae2-7935346f4687.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'paired-hemisphere-brain'
    keyshape = Keyshape.SQUARE
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
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

        for side in (-1,1):
            x=lambda v:24+side*v
            bez(f'lobe{side}',(24,12),((24,8),(x(3),6),(x(7),6)),((x(12),6),(x(13),10),(x(13),15)),((x(17),15),(x(18),19),(x(18),23)),((x(18),27),(x(16),29),(x(15),30)),((x(18),38),(x(13),42),(x(8),42)),((x(3),42),(24,40),(24,36)))
            bez(f'fold{side}',(24,22),((x(5),22),(x(8),22),(x(8),18)))
        line('seam',(24,12),(24,36));join('seam','lobe-1');join('seam','lobe1');join('seam','fold-1');join('seam','fold1');join('lobe-1','lobe1')
