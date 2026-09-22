'Anatomical head and brain, preserving independent internal lobes. Must retain source direction and folds in final review.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape VRECT_L uses exact SOLO48 contract bounds. Lucide brain contributes lobed contour principle; human_ref/user inspected for head vocabulary. Anatomical brain is an intrinsic organ. Whole brain offset owns clearance repair; no internal folds can fit. Unresolved visual review: reduced brain loses recognizable lobes and stem, so retain draft without export.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6e501462-4458-4ee8-918b-3b9b1c8dded4'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_28/neurobiologist_6e501462-4458-4ee8-918b-3b9b1c8dded4.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'left-profile-brain'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "Uncategorized"
    aliases = ["Human Head with Brain"]
    keywords = ["head", "brain", "anatomy", "profile", "neurology", "human"]
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

        bez('skull',(32,44),((30,39),(31,35),(36,31)),((40,28),(40,24),(40,19)),((40,10),(33,4),(25,4)),((16,4),(12,10),(12,18)))
        poly('face',(12,18),(8,25),(14,26),(14,34),(22,34),(22,44));join('skull','face')
        brain_x = 1
        shift = lambda p: (p[0]+brain_x,p[1])
        segments=[((19,22),(19,16),(22,15)),((25,11),(29,14),(29,17)),((32,21),(28,24),(26,22)),((24,23),(23,22),(22,22))]
        bez('brain',shift((22,22)),*[tuple(shift(p) for p in seg) for seg in segments])
