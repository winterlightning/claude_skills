'Knotted neck bandana with two pointed ends and triangular lower cloth; mirrored ends and central knot.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape SQUARE uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'da69e025-ec35-4e8e-b0d5-492782d18d44'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_05/bandana_da69e025-ec35-4e8e-b0d5-492782d18d44.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'knotted-triangular-neck-bandana'
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

        circle('knot',24,14,4)
        bez('left-end',(20,12),((11,13),(8,8),(6,6)),((12,6),(18,7),(20,12)))
        bez('right-end',(28,12),((37,13),(40,8),(42,6)),((36,6),(30,7),(28,12)))
        join('left-end','knot');join('right-end','knot')
        bez('cloth',(24,18),((12,20),(6,25),(10,30)),((13,35),(19,39),(24,42)),((29,39),(35,35),(38,30)),((42,25),(36,20),(24,18)))
        bez('fold',(9,27),((16,31),(32,31),(39,27)));join('fold','cloth');join('cloth','knot')
