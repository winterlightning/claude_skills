'Simple Baby Face.\nPlan and review: Retained blank rounded baby head, both side ears and left-turning hair curl. Integrated ears into a smooth outline to avoid trapped side pockets. Human references and Lucide baby informed construction; no body or facial marks added.\nKeyshape: HRECT_L, exact SOLO48 envelope.\nConstruction reference: human_ref/user.svg circular head vocabulary; Lucide baby integrated curl and side ears. No face marks added.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '00cb164f-b36d-4ff3-a847-c9dbc18a9239'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_24/kid period_00cb164f-b36d-4ff3-a847-c9dbc18a9239.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'baby-head-curl'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('baby', 'head', 'curl')

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

        curve('head',(24,8),((16,8),(10,12),(9,20)),((6,20),(4,22),(4,24)),((4,26),(6,28),(9,28)),((10,36),(16,40),(24,40)),((32,40),(38,36),(39,28)),((42,28),(44,26),(44,24)),((44,22),(42,20),(39,20)),((38,12),(32,8),(24,8)))
        path('curl',(24,8),[(24,20),((18,20),3,3,True)]);self.relate('connect','head','curl')
