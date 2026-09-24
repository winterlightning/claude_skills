'Simple Side View Locust Insect.\nPlan and review: Retained elongated locust body, oval right head, antenna, large folded hind leg and angular ground legs. Omitted tiny eye and secondary leg detail; rebuilt rear leg/body attachment to remove a narrow pocket.\nKeyshape: HRECT_L, exact SOLO48 envelope.\nConstruction reference: No useful exact Lucide match; source silhouette and geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5c07b2b0-22a5-4eba-a68b-9d0f0cf7fbd8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_25/locust_5c07b2b0-22a5-4eba-a68b-9d0f0cf7fbd8.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'locust'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('locust',)

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

        path('head',(32,22),[((44,22),6,8,True),((32,22),6,8,True)],True)
        self.add_line('antenna',(38,14),(30,8));self.relate('connect','antenna','head')
        curve('body',(32,22),((24,20),(12,24),(4,26)),((12,34),(20,38),(34,28)));self.relate('connect','body','head')
        path('hind-leg',(4,26),[(12,12),(22,26),(18,40)])
        self.add_line('rear-leg',(4,26),(4,40));self.relate('connect','rear-leg','body');self.relate('connect','rear-leg','hind-leg');self.relate('connect','hind-leg','body')
        path('front-leg',(36,30),[(40,34),(44,40)]);self.relate('connect','front-leg','head')
