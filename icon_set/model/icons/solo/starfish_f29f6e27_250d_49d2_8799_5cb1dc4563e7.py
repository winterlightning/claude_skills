'Rounded Five Pointed Sea Starfish.\nPlan and review: Retained all five rounded arms. Simplified small central ring to a dot for clearance.\nKeyshape: SQUARE, exact SOLO48 envelope.\nConstruction reference: Source render; no useful exact local Lucide match.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f29f6e27-250d-49d2-8799-5cb1dc4563e7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_36/starfish_f29f6e27-250d-49d2-8799-5cb1dc4563e7.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'starfish'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('starfish',)

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

        curve('star',(24,6),((28,6),(27,20),(32,20)),((36,20),(42,16),(42,20)),((42,24),(32,27),(32,30)),((32,34),(38,42),(34,42)),((30,42),(28,34),(24,34)),((20,34),(18,42),(14,42)),((10,42),(16,34),(16,30)),((16,27),(6,24),(6,20)),((6,16),(12,20),(16,20)),((21,20),(20,6),(24,6)))
        self.add_dot('center',(24,25))
