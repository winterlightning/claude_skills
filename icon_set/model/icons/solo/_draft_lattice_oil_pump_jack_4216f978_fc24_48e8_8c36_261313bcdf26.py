'Oil pump jack with sloping beam, horsehead, tapered lattice support and two rods to ground. Preserve industrial identity.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape SQUARE uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4216f978-fc24-48e8-8c36-261313bcdf26'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_29/oil well_4216f978-fc24-48e8-8c36-261313bcdf26.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'lattice-oil-pump-jack'
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

        poly('ground',(6,42),(42,42))
        poly('tower',(16,42),(24,18),(32,42));join('tower','ground')
        line('beam',(12,10),(42,20));join('beam','tower')
        bez('horsehead',(6,22),((6,12),(11,6),(14,6)),((18,6),(14,20),(6,22)))
        line('rod-left',(6,22),(6,42));line('rod-right',(42,20),(42,42));join('rod-left','horsehead');join('rod-left','ground');join('rod-right','beam');join('rod-right','ground');join('beam','horsehead')
        line('brace',(20,30),(30,36));join('brace','tower')
