'Sealed Cardboard Delivery Box.\nPlan and review: Retained broad front panel, trapezoid box top, shared seam and short sealing tape.\nKeyshape: SQUARE, exact SOLO48 envelope.\nConstruction reference: Lucide package: shared box seams; source front-facing trapezoid top.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '914ee8a0-de65-4f53-99b9-83539e10ea79'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_36/stuff_914ee8a0-de65-4f53-99b9-83539e10ea79.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'sealed-shipping-box'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('sealed', 'shipping', 'box')

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

        path('box',(6,16),[(14,6),(34,6),(42,16),(42,42),(6,42),(6,16)],True)
        self.add_polyline('edge',(6,16),(24,16),(42,16));self.relate('connect','edge','box')
        self.add_line('tape',(24,6),(24,26));self.relate('connect','tape','box');self.relate('connect','tape','edge')
