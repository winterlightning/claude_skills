'Construction Worker with Safety Helmet.\nPlan and review: Retained hard hat, circular jaw, curved shoulders and lower foreground panel. Interpreted the uncertain lower outline conservatively as a panel, without assigning it a specific job. Jaw radius10, center(24,16), bottom26; shoulder top30: zero ink gap.\nKeyshape: VRECT_L, exact SOLO48 envelope selected for this subject.\nConstruction reference: human_ref/user.svg: circular jaw and curved shoulders; Lucide hard-hat: dome and brim.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cc025368-b3c0-4db5-9628-aeeb0bb29471'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_17/engineer project superviser 2_cc025368-b3c0-4db5-9628-aeeb0bb29471.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'construction-worker-with-safety-helmet'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('construction', 'worker', 'with', 'safety', 'helmet')

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

        path('helmet',(14,16),[((34,16),10,10,True),(40,16)])
        self.add_line('brim-left',(8,16),(14,16));self.relate('connect','helmet','brim-left')
        self.add_arc('jaw',(14,16),(34,16),radius_x=10,sweep=False);self.relate('connect','helmet','jaw');self.relate('connect','brim-left','jaw')
        self.add_line('crown',(24,4),(24,6));self.relate('connect','crown','helmet')
        self.add_arc('body-left',(8,35),(20,30),radius_x=12,radius_y=5,sweep=True)
        self.add_line('body-top',(20,30),(28,30))
        self.add_arc('body-right',(28,30),(40,35),radius_x=12,radius_y=5,sweep=True)
        self.add_contour('body','body-left','body-top','body-right');self.relate('connect','jaw','body')
        self.add_line('panel',(8,44),(40,44))
