'Rounded stomach with open esophageal and intestinal tubes, continuous inner concavity. Two asymmetric coherent contours; no exact Lucide match.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape SQUARE uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9cee59c1-31ee-4d2a-8f19-7e1d41b267f8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_36/stomach_9cee59c1-31ee-4d2a-8f19-7e1d41b267f8.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'stomach-pouch-with-upright-esophagus'
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

        bez('outer',(19,6),((19,16),(22,12),(28,12)),((36,12),(42,18),(42,26)),((42,35),(36,40),(29,40)),((20,40),(15,33),(15,42)))
        bez('inner',(6,42),((6,31),(10,28),(17,28)),((24,28),(24,22),(17,21)),((10,20),(10,12),(10,6)))
