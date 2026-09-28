'Exposed brain above opened rear head. Anatomical depiction, not container-plus-symbol. Preserve lobes and neck.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape VRECT_L uses exact SOLO48 contract bounds. Lucide brain contributes scalloped lobes and an attached fold. Human user.svg inspected; this is a rear anatomical head section, not a detached head-and-torso figure.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '057618af-fa4d-4d15-af45-d4d6842883c1'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_07/brain open skill_057618af-fa4d-4d15-af45-d4d6842883c1.svg'
AUTHOR = 'gpt-6-astra'

class Drawing(Solo48):
    icon_id = 'exposed-brain-above-open-head'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'Uncategorized'
    aliases = ['Human Brain in Open Head']
    keywords = ['brain','head','anatomy','mind','open','skull','human']
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

        bez('brain',(8,24),((8,18),(8,14),(14,14)),((12,5),(17,4),(20,4)),((23,4),(23,5),(24,6)),((25,5),(28,4),(30,4)),((35,4),(35,9),(34,14)),((40,14),(40,18),(40,24)))
        bez('head',(8,24),((8,32),(16,32),(16,36)),((16,39),(16,41),(16,44)))
        bez('head-right',(40,24),((40,32),(32,32),(32,36)),((32,39),(32,41),(32,44)))
        line('opening',(8,24),(40,24));join('opening','brain');join('opening','head');join('opening','head-right');join('brain','head');join('brain','head-right')

        bez('fold',(24,6),((28,10),(26,14),(20,14)))
        join('fold','brain')
