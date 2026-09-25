'Diagonal marker with exposed tip, cap behind its body and separate ink droplet. Retain all three identifying components.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape SQUARE uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '42b73bbf-7e8c-4f22-a7a2-81ccf67934d3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_12/content brush pen_42b73bbf-7e8c-4f22-a7a2-81ccf67934d3.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'uncapped-marker-with-ink-drop'
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

        poly('pen',(12,32),(34,10),(42,18),(20,40),(12,32))
        poly('tip',(12,32),(6,42),(20,40));join('tip','pen')
        poly('cap',(28,32),(36,40),(42,34),(34,26));join('cap','pen')
        bez('drop',(12,6),((10,10),(6,11),(6,14)),((6,18),(14,18),(14,14)),((14,10),(13,10),(12,6)))
