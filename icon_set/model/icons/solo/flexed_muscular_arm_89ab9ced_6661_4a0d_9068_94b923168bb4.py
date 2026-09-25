'Flexed Biceps Muscle.\nPlan and review: Retained flexed arm, fist and pronounced biceps bulge. Widened the forearm/fist-to-biceps clearance; preserved natural asymmetric anatomy.\nKeyshape: SQUARE, exact SOLO48 envelope selected for this silhouette.\nConstruction reference: Lucide biceps-flexed: coherent arm outline, rounded fist and biceps curve.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '89ab9ced-6661-4a0d-9068-94b923168bb4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_23/jerk_89ab9ced-6661-4a0d-9068-94b923168bb4.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'flexed-muscular-arm'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('flexed', 'muscular', 'arm')

    def build(self):

        def path(name, start, steps, closed=False):
            members=[]; point=start
            for index, step in enumerate(steps):
                member=f"{name}-{index}"
                if len(step)==2:
                    self.add_line(member,point,step); point=step
                else:
                    end,rx,ry,sweep=step
                    self.add_arc(member,point,end,radius_x=rx,radius_y=ry,sweep=sweep); point=end
                members.append(member)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[((x+r,y),r,r,True),((x-r,y),r,r,True)],True)
        def box(name,l,t,r,b,rad):
            path(name,(l+rad,t),[(r-rad,t),((r,t+rad),rad,rad,True),(r,b-rad),((r-rad,b),rad,rad,True),(l+rad,b),((l,b-rad),rad,rad,True),(l,t+rad),((l+rad,t),rad,rad,True)],True)
        def curve(name,start,*segments):
            self.add_bezier(name,start,*segments)

        curve('arm',(42,36),((34,44),(14,44),(6,36)),((6,28),(8,14),(14,6)),((28,6),(32,16),(22,16)),((24,20),(22,24),(20,30)),((26,23),(38,23),(42,28)))
