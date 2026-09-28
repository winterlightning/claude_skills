'Raw Steak with Bone.\nPlan and review: Retained irregular steak, round bone and curved depth band. Rebuilt top and bottom extrema on the keyshape and reduced the bone diameter for clearance.\nKeyshape: SQUARE, exact SOLO48 envelope.\nConstruction reference: Lucide beef: irregular steak outline, round bone and visible thickness.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '62712aaf-47f3-4274-8b31-9041003108f9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_36/steak_62712aaf-47f3-4274-8b31-9041003108f9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'raw-steak-with-bone'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('raw', 'steak', 'with', 'bone')

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

        curve('top',(6,30),((6,20),(16,20),(18,12)),((20,8),(26,6),(30,6)),((38,6),(42,12),(42,20)),((42,34),(18,40),(6,30)))
        curve('side',(6,30),((6,40),(16,42),(24,42)),((34,42),(42,32),(42,20)))
        self.relate('connect','top','side');circle('bone',29,19,3)
