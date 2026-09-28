'Electric Power Drill Machine.\nPlan and review: Retained electric drill, grip, bit and wall contact. Omitted small vents and separate chuck casing. Left-facing asymmetry follows the source.\nKeyshape: HRECT_L, exact SOLO48 envelope selected for this silhouette.\nConstruction reference: Lucide drill: rounded motor casing and angled grip; wall retained.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9555bc6b-77bb-4c22-bd68-52e282c33ecb'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_22/home improvement 8_9555bc6b-77bb-4c22-bd68-52e282c33ecb.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'drill-boring-into-wall'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('drill', 'boring', 'into', 'wall')

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

        self.add_line('wall',(4,8),(4,40));self.add_line('bit',(4,18),(16,18));self.relate('connect','wall','bit')
        path('drill',(20,10),[(40,10),((44,14),4,4,True),(44,22),((40,26),4,4,True),(40,40),(28,40),(28,26),(20,26),((16,22),4,4,True),(16,14),((20,10),4,4,True)],True)
        self.relate('connect','bit','drill')
