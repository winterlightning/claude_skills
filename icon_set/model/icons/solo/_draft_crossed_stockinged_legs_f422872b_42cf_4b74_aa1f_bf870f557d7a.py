'Crossed stockinged legs with one bent knee and pointed raised foot; slender anatomical contours are retained for review.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape VRECT_M uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f422872b-42cf-4b74-aa1f-bf870f557d7a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_29/pantyhose_f422872b-42cf-4b74-aa1f-bf870f557d7a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'crossed-stockinged-legs'
    keyshape = Keyshape.VRECT_M
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

        bez('standing',(16,4),((10,7),(10,12),(16,16)),((21,20),(22,24),(20,30)),((18,36),(18,39),(18,42)),((20,44),(25,44),(28,44)))
        bez('rear',(26,4),((26,10),(26,12),(30,16)),((38,20),(38,24),(34,28)),((29,32),(23,34),(22,38)))
        bez('cross',(16,13),((23,16),(28,18),(30,22)),((23,26),(16,29),(16,34)))
        join('standing','cross')
