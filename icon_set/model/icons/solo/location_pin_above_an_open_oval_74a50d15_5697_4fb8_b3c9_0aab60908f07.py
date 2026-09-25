'Map pin with small round opening above a wide open ground oval. Lucide map-pin informs the pin; the source ground indicator is retained as part of this natural location symbol.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape SQUARE uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '74a50d15-5697-4fb8-b3c9-0aab60908f07'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_02/amazon pin location_74a50d15-5697-4fb8-b3c9-0aab60908f07.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'location-pin-above-an-open-oval'
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
            if rad==0:
                self.add_polyline(name,(l,t),(r,t),(r,b),(l,b),(l,t)); return
            path(name,(l+rad,t),[(r-rad,t),((r,t+rad),rad,rad,True),(r,b-rad),((r-rad,b),rad,rad,True),(l+rad,b),((l,b-rad),rad,rad,True),(l,t+rad),((l+rad,t),rad,rad,True)],True)
        def line(name,a,b): self.add_line(name,a,b)
        def poly(name,*points): self.add_polyline(name,*points)
        def join(*names): self.relate('connect',*names)

        def bez(name,start,*segments): self.add_bezier(name,start,*segments)

        bez('pin',(24,33),((16,27),(10,23),(10,17)),((10,10),(17,6),(24,6)),((31,6),(38,10),(38,17)),((38,23),(32,27),(24,33)))
        circle('hole',24,18,3)
        bez('ground',(12,35),((8,36),(6,37),(6,38)),((6,41),(16,42),(24,42)),((32,42),(42,41),(42,38)),((42,37),(40,36),(36,35)))
