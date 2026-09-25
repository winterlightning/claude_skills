'Broad low loaf with exactly three scoring curves. Preserve loaf rather than generic oval; repeated scoring uses shared shape.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape HRECT_M uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'aee9af45-4408-44bc-855b-a22fd716f1e5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_05/bakery_aee9af45-4408-44bc-855b-a22fd716f1e5.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'low-oval-bread-loaf'
    keyshape = Keyshape.HRECT_M
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

        path('loaf',(4,22),[((16,10),12,12,True),(32,10),((44,22),12,12,True),(44,28),((34,38),10,10,True),(14,38),((4,28),10,10,True),(4,22)],True)
        for x in (16,24,32):
            line(f'score{x}',(x,10),(x,22));join('loaf',f'score{x}')
