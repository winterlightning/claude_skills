'Simple Retail Shopping Bag.\nPlan and review: Retained tapered shopping bag, flat base and arched handle. Shortened handle ends inside bag to clear its sloping walls.\nKeyshape: VRECT_L, exact SOLO48 envelope.\nConstruction reference: Lucide shopping-bag: broad body and attached handle; preserve source raised loop.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4eaa0e1d-1e52-4fb7-992c-ee24275c9362'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_05/bag shopping_4eaa0e1d-1e52-4fb7-992c-ee24275c9362.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'simple-retail-shopping-bag'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('simple', 'retail', 'shopping', 'bag')

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

        path('bag',(12,16),[(36,16),(40,40),((36,44),4,4,True),(12,44),((8,40),4,4,True),(12,16)],True)
        path('handle',(18,17),[(18,10),((30,10),6,6,True),(30,17)]);self.relate('connect','handle','bag')
