'Raised saddle seat ends, hanging panel and stirrup. Preserve equestrian identity; no useful exact Lucide match.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape SQUARE uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5aa2a9a8-1ae0-4989-b37b-383f5ec7682d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_33/saddle_5aa2a9a8-1ae0-4989-b37b-383f5ec7682d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'saddle-with-hanging-stirrup'
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

        bez('seat',(6,10),((6,7),(8,6),(10,6)),((14,6),(16,10),(24,10)),((32,10),(34,6),(38,6)),((40,6),(42,7),(42,10)),((42,16),(38,18),(32,18)),((27,18),(21,18),(16,18)),((10,18),(6,16),(6,10)))
        bez('flap',(16,18),((16,27),(17,27),(24,27)),((31,27),(32,27),(32,18)))
        join('seat','flap')
        path('stirrup',(18,42),[(18,38),((22,34),4,4,True),(26,34),((30,38),4,4,True),(30,42),(18,42)],True)
        line('strap',(24,27),(24,34));join('strap','flap');join('strap','stirrup')
