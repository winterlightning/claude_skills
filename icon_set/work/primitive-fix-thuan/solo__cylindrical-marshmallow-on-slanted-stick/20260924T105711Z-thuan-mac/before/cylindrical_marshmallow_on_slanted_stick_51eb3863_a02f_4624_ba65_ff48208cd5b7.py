'Tilted cylindrical marshmallow with elliptical top and roasting stick extending lower-left; preserve cylindrical reading rather than a plain square.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape SQUARE uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '51eb3863-a02f-4624-ba65-ff48208cd5b7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_26/marshmallow_51eb3863-a02f-4624-ba65-ff48208cd5b7.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'cylindrical-marshmallow-on-slanted-stick'
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

        bez('top',(20,10),((20,8),(24,6),(28,6)),((36,6),(42,12),(42,18)),((42,24),(36,25),(30,22)),((24,19),(20,14),(20,10)))
        bez('body',(20,10),((17,16),(13,23),(12,28)),((12,35),(23,40),(28,36)),((34,32),(42,24),(42,18)));join('body','top')
        line('stick',(6,42),(12,28));join('stick','body')
