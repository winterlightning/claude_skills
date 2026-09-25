'Long-Neck Glass Wine Bottle\nPlan: Bottle with narrow neck, sloping shoulders and rounded lower body; symmetric axis24.\nReference: Lucide milk original and atomic-debug: neck, shoulders and body as one coherent contour.\nReduction: Remove cap band so the neck retains usable clearance.\nKeyshape: VRECT_M; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1c186379-46fe-4d91-a4a2-3c981a619762'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_31/pinot_1c186379-46fe-4d91-a4a2-3c981a619762.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'long-neck-glass-wine-bottle'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    keywords = ('long', 'neck', 'glass', 'wine', 'bottle')

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

        path('bottle',(20,4),[(28,4),(28,16),(38,26),(38,40),((34,44),4,4,True),(14,44),((10,40),4,4,True),(10,26),(20,16),(20,4)],True)
