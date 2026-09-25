'Mirrored chandelier arms and three holders; collars omitted.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape SQUARE uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '076c13f2-7525-47c3-b461-4fa44894212d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_11/chandelier_076c13f2-7525-47c3-b461-4fa44894212d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'bare-three-arm-chandelier'
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
            path(name,(l+rad,t),[(r-rad,t),((r,t+rad),rad,rad,True),(r,b-rad),((r-rad,b),rad,rad,True),(l+rad,b),((l,b-rad),rad,rad,True),(l,t+rad),((l+rad,t),rad,rad,True)],True)
        def line(name,a,b): self.add_line(name,a,b)
        def poly(name,*points): self.add_polyline(name,*points)
        def join(*names): self.relate('connect',*names)

        line('cap',(18,6),(30,6));line('stem',(24,6),(24,28));join('cap','stem')
        path('arms',(6,22),[(6,28),((24,28),9,14,False),((42,28),9,14,False),(42,22)]);join('stem','arms')
        for x in (6,42):line(f'holder{x}',(x,18),(x,22))
        join('holder6','arms');join('holder42','arms')
