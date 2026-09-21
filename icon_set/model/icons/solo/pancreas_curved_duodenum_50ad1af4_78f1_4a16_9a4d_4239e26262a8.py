'Pancreas tapered to the right with curved duodenum around its left head. Anatomical adjacency retained; no useful exact Lucide match.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape HRECT_M uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '50ad1af4-78f1-4a16-9a4d-4239e26262a8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_29/pancreas_50ad1af4-78f1-4a16-9a4d-4239e26262a8.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'pancreas-curved-duodenum'
    keyshape = Keyshape.HRECT_M
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

        bez('organ',(4,25),((4,12),(12,10),(20,13)),((28,14),(38,10),(42,10)),((44,10),(44,12),(44,14)),((44,19),(35,24),(28,26)),((21,27),(20,30),(22,34)),((20,38),(17,38),(14,38)),((7,38),(4,32),(4,25)))
        bez('inner',(15,21),((10,27),(16,32),(22,34)))
        join('inner','organ')
