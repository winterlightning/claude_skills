'Coughing Person Profile.\nPlan and review: Retained right-facing head, mouth opening and three cough marks; omitted inner ear. Profile asymmetry follows the reference.\nKeyshape: VRECT_L, exact SOLO48 envelope selected for this subject.\nConstruction reference: human_ref/user.svg guides round cranium; source profile, mouth and cough rays retained.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '70068075-fcbd-43f7-8047-bd45057d5d00'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_22/head side cough_70068075-fcbd-43f7-8047-bd45057d5d00.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'coughing-person-profile'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('coughing', 'person', 'profile')

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

        path('back',(8,44),[(8,36)])
        curve('head',(8,36),((14,30),(8,28),(8,18)),((8,10),(12,4),(20,4)),((28,4),(30,10),(28,18)))
        self.relate('connect','back','head')
        path('face',(28,18),[(32,24),(24,24),(24,30),(20,30),(20,44)]);self.relate('connect','head','face')
        for n,(a,b) in enumerate((((40,22),(40,24)),((36,32),(40,32)),((34,40),(36,42)))):self.add_line(f'cough-{n}',a,b)
