'Customer Support Agent.\nPlan and review: Retained bob/fringe cue, headphones and shoulders; simplified earcups to attached side strokes. Circular jaw radius8, center(24,20), bottom28; shoulder top32: zero ink gap.\nKeyshape: VRECT_L, exact SOLO48 envelope selected for this subject.\nConstruction reference: human_ref/user.svg: circular jaw and broad shoulders; Lucide headphones: headband with attached ear ends.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'be70bb88-f464-4645-872e-be780f9679ac'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_22/headphones woman_be70bb88-f464-4645-872e-be780f9679ac.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'customer-support-agent'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'avatars'
    aliases = ()
    keywords = ('customer', 'support', 'agent')

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

        path('hair',(8,28),[(8,20),((40,20),16,16,True),(40,28)])
        path('fringe',(16,20),[(24,14),(32,20)])
        self.add_arc('jaw',(16,20),(32,20),radius_x=8,sweep=False);self.relate('connect','fringe','jaw')
        self.add_line('ear-left',(8,20),(16,20));self.add_line('ear-right',(32,20),(40,20))
        for side in ('ear-left','ear-right'):
         self.relate('connect',side,'hair');self.relate('connect',side,'jaw');self.relate('connect',side,'fringe')
        self.add_line('body-left',(8,44),(8,40));self.add_arc('body-left-shoulder',(8,40),(20,32),radius_x=12,radius_y=8,sweep=True)
        self.add_line('body-top',(20,32),(28,32));self.add_arc('body-right-shoulder',(28,32),(40,40),radius_x=12,radius_y=8,sweep=True);self.add_line('body-right',(40,40),(40,44))
        self.add_contour('body','body-left','body-left-shoulder','body-top','body-right-shoulder','body-right');self.relate('connect','jaw','body')
