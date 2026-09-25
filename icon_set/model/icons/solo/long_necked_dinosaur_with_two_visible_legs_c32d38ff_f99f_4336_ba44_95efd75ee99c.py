'Long-neck dinosaur with right-facing small head, arched back, tail and exactly two block legs. Preserve source silhouette and direction.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape SQUARE uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c32d38ff-f99f-4336-ba44-95efd75ee99c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_15/dinosaur_c32d38ff-f99f-4336-ba44-95efd75ee99c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'long-necked-dinosaur-with-two-visible-legs'
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

        bez('dinosaur',(6,34),((13,28),(15,19),(23,20)),((26,21),(26,21),(26,18)),((26,11),(26,6),(34,6)),((38,6),(42,9),(42,12)),((42,16),(36,14),(36,18)),((36,23),(37,28),(34,32)))
        poly('legs',(34,32),(34,42),(26,42),(26,34),(18,34),(18,42),(10,42),(10,33),(6,34));join('dinosaur','legs')
