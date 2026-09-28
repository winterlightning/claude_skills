'Recreational Hang Glider.\nPlan and review: Retained broad triangular wing, central spar and hanging triangular control frame.\nKeyshape: HRECT_L, exact SOLO48 envelope.\nConstruction reference: Source render; no useful exact local Lucide match.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0c4ade2d-4939-47ee-8228-ac86ee181f91'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_22/hang glider_0c4ade2d-4939-47ee-8228-ac86ee181f91.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'triangular-hang-glider-solo'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('triangular', 'hang', 'glider', 'solo')

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

        path('wing',(4,28),[(24,8),(44,28),((4,28),20,4,False)],True)
        self.add_line('spar',(24,8),(24,30));self.relate('connect','spar','wing')
        path('frame',(14,40),[(24,30),(34,40),(14,40)],True);self.relate('connect','frame','spar')
