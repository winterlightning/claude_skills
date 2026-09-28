"""domed-canister-vacuum-with-hose.
Plan: Canister vacuum with rounded dome, one wheel, a continuous arching hose, and a separate floor nozzle. Tangent circular hose corners.
Keyshape: SQUARE, exact SOLO48 inset envelope.
Reference construction: No useful Lucide subject match.
Omissions: Small hose collar and canister midline.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b34fe2ce-a231-4d6b-854b-56f36cacf58b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_11/cleaning vacuum 1_b34fe2ce-a231-4d6b-854b-56f36cacf58b.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'domed-canister-vacuum-with-hose'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('cleaning', 'vacuum', '1')

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

        path('body',(16,38),[(6,38),(6,28),((16,18),10,10,True),((26,28),10,10,True),(26,38),(24,38)])
        circle('wheel',20,38,4);self.relate('connect','body','wheel')
        path('hose',(16,18),[(16,14),((24,6),8,8,True),(34,6),((42,14),8,8,True),(42,34)])
        self.relate('connect','hose','body')
        box('nozzle',34,34,42,42,1);self.relate('connect','hose','nozzle')
