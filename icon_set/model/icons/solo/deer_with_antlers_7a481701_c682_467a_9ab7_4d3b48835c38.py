"""deer-with-antlers.
Plan: Deer side silhouette with rounded rump, raised head, forked antlers and three separated leg strokes. Intentional side-view asymmetry.
Keyshape: SQUARE, exact SOLO48 inset envelope.
Reference construction: No useful Lucide subject match.
Omissions: Far-side overlapping legs and tiny facial details.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7a481701-c682-467a-9ab7-4d3b48835c38'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_18/fawn_7a481701-c682-467a-9ab7-4d3b48835c38.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'deer-with-antlers'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('fawn',)

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

        curve('rump',(6,34),((6,27),(10,24),(16,24)))
        path('back-head',(16,24),[(24,24),(28,18),(34,18),(42,22),(42,28),(34,28),(32,42)])
        self.relate('connect','rump','back-head')
        self.add_line('rear-leg',(6,34),(6,42));self.relate('connect','rear-leg','rump')
        path('belly',(6,34),[(20,34),(24,42)])
        self.relate('connect','belly','rump');self.relate('connect','belly','rear-leg')
        path('antler',(28,18),[(28,10),((32,6),4,4,True),(36,6)]);self.relate('connect','antler','back-head')
        self.add_line('antler-branch',(28,14),(20,6));self.relate('connect','antler-branch','antler')
