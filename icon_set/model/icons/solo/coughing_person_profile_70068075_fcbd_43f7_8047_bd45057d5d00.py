"""coughing-person-profile.
Plan: Continuous anatomical head and neck profile with a round skull, nose, chin and cough rays. Human user reference informs smooth head curvature; this is an attached profile, not a detached stick figure.
Keyshape: HRECT_L, exact SOLO48 inset envelope.
Reference construction: No useful Lucide subject match.
Omissions: Ear detail; three cough rays reduced to two.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '70068075-fcbd-43f7-8047-bd45057d5d00'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_22/head side cough_70068075-fcbd-43f7-8047-bd45057d5d00.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'coughing-person-profile'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('head', 'side', 'cough')

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

        curve('back',(8,40),((8,36),(10,33),(8,29)),((5,24),(4,22),(4,19)),((4,12),(9,8),(16,8)),((23,8),(28,12),(28,19)))
        path('face',(28,19),[(32,25),(26,25),(26,31),((22,35),4,4,True),(22,40)])
        self.relate('connect','back','face')
        self.add_dot('eye',(18,20))
        self.add_line('cough-mid',(38,31),(44,31))
        self.add_line('cough-low',(35,40),(40,40))
