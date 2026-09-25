'Simple Circular Analog Clock.\nPlan and review: Retained plain circular dial and two hands meeting directly at center. No hub, ticks or numerals added.\nKeyshape: CIRCLE, exact SOLO48 envelope.\nConstruction reference: Lucide clock: plain dial and connected two-hand stroke.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e31a2d89-cd15-4da1-8bfb-d9c0381903ac'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_38/time clock circle_e31a2d89-cd15-4da1-8bfb-d9c0381903ac.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'plain-clock'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('plain', 'clock')

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

        circle('dial',24,24,20);self.add_polyline('hands',(24,13),(24,24),(32,32))
