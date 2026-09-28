'Delivery Truck with Rounded Cab Roof\nPlan: Cargo box and cab share a dividing wall; identical wheels attach at exact endpoints.\nReference: Lucide truck original and atomic-debug: cargo rectangle, forward cab, matched wheels.\nReduction: Drop inner cab window to protect the wheel and cargo spacing.\nKeyshape: HRECT_L; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f862f688-d254-4ad5-8434-53daeef19bc9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_14/delivery truck cargo_f862f688-d254-4ad5-8434-53daeef19bc9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'delivery-truck-with-rounded-cab-roof'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    keywords = ('delivery', 'truck', 'with', 'rounded', 'cab', 'roof')

    def build(self):

        def path(name, start, steps, closed=False):
            members, point = [], start
            for index, step in enumerate(steps):
                member = f"{name}-{index}"
                if len(step) == 2:
                    self.add_line(member, point, step)
                    point = step
                else:
                    end, rx, ry, sweep = step
                    self.add_arc(member, point, end, radius_x=rx, radius_y=ry, sweep=sweep)
                    point = end
                members.append(member)
            self.add_contour(name, *members, closed=closed)
        def ellipse(name,x,y,rx,ry):
            path(name,(x-rx,y),[((x+rx,y),rx,ry,True),((x-rx,y),rx,ry,True)],True)
        def circle(name,x,y,r):
            ellipse(name,x,y,r,r)
        def box(name,l,t,r,b,rad=4):
            path(name,(l+rad,t),[(r-rad,t),((r,t+rad),rad,rad,True),(r,b-rad),((r-rad,b),rad,rad,True),(l+rad,b),((l,b-rad),rad,rad,True),(l,t+rad),((l+rad,t),rad,rad,True)],True)

        path('body',(4,25),[(4,8),(26,8),(26,17),(36,17),((44,25),8,8,True),(4,25)],True)
        for x in (12,36):circle(f'wheel-{x}',x,37,3)
        self.add_line('division',(26,17),(26,25));self.relate('connect','division','body')
