'Tapered lighthouse with roofed lantern, projecting gallery and exactly four light rays. Mirrored structure, source details kept.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape SQUARE uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '969cd7b7-18ae-4dc0-99ef-fbfd5047b13e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_26/lookout_969cd7b7-18ae-4dc0-99ef-fbfd5047b13e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'tapered-lighthouse-with-four-light-rays'
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

        poly('roof',(16,12),(24,6),(32,12))
        poly('lantern',(18,12),(18,22),(30,22),(30,12));join('roof','lantern')
        poly('tower',(18,22),(14,42),(34,42),(30,22));join('tower','lantern')
        poly('gallery',(16,22),(18,22),(30,22),(32,22));join('gallery','tower');join('gallery','lantern')
        line('ground-left',(6,42),(14,42));line('ground-right',(34,42),(42,42));join('ground-left','tower');join('ground-right','tower')
        for side in (-1,1):
            x=lambda a:24+side*a
            line(f'ray-up{side}',(x(16),12),(x(18),10));line(f'ray-low{side}',(x(16),22),(x(18),24))
