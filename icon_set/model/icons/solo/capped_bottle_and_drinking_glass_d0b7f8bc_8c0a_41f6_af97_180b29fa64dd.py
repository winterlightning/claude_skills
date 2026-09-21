'Capped bottle and half-full drinking glass are one physical still life. Preserve cap, neck, shoulders and glass waterline.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape SQUARE uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd0b7f8bc-8c0a-41f6-af97-180b29fa64dd'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_08/brandy_d0b7f8bc-8c0a-41f6-af97-180b29fa64dd.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'capped-bottle-and-drinking-glass'
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

        path('bottle',(10,6),[(18,6),(18,14)])
        bez('shoulder-right',(18,14),((18,20),(23,20),(23,26)))
        path('base',(23,26),[(23,38),((19,42),4,4,True),(10,42),((6,38),4,4,True),(6,26)])
        bez('shoulder-left',(6,26),((6,20),(10,20),(10,14)))
        line('neck-left',(10,14),(10,6));line('cap',(10,14),(18,14))
        join('bottle','shoulder-right');join('shoulder-right','base');join('base','shoulder-left');join('shoulder-left','neck-left');join('neck-left','bottle');join('cap','shoulder-left');join('cap','shoulder-right');join('cap','bottle');join('cap','neck-left')
        path('glass',(32,24),[(42,24),(42,37),((37,42),5,5,True),((32,37),5,5,True),(32,24)],True)
        line('water',(32,32),(42,32));join('water','glass')
