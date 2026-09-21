'Reader behind a broad open book with center spine and two hands. Shared human reference supplies round head; omit tiny facial marks and hair strands.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape SQUARE uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4bd21975-1eff-4289-97a9-69e25b0116fa'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_28/newspaper read man_4bd21975-1eff-4289-97a9-69e25b0116fa.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'reader-holding-open-book'
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

        path('head',(14,18),[(14,16),((34,16),10,10,True),(34,18)])
        poly('book',(13,27),(24,30),(35,27),(35,41),(24,42),(13,41),(13,27));line('spine',(24,30),(24,42));join('spine','book')
        path('left-hand',(13,27),[(((13,41)),7,7,False)]);path('right-hand',(35,27),[(((35,41)),7,7,True)]);join('left-hand','book');join('right-hand','book')
