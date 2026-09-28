'Security Entrance Turnstile.\nPlan and review: Retained rounded upright post, broad right barrier and descending diagonal rotating arm.\nKeyshape: SQUARE, exact SOLO48 envelope.\nConstruction reference: Source render; no useful exact local Lucide match.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a88a3268-2f5c-411d-b518-d58bd16aa4dc'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_39/turnstile_a88a3268-2f5c-411d-b518-d58bd16aa4dc.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'entrance-turnstile'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('entrance', 'turnstile')

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

        box('post',6,6,18,42,3)
        path('barrier',(18,14),[(38,14),((38,22),4,4,True),(18,22)]);self.relate('connect','post','barrier')
        self.add_line('arm',(22,22),(38,38));self.relate('connect','arm','barrier')
