# Final repair: Small-circle exception heads preserve two occupants with exact8-unit head-to-shoulder centerline gap.
'Car with Two Seated Occupants\nPlan: Frontal car with mirrored occupant heads; broad body and two short tires.\nReference: Shared human user.svg and Lucide car: circular heads and paired car construction.\nReduction: Omit shoulders and lights only in first fit; preserve two people as circular heads, subject to visual review.\nKeyshape: SQUARE; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1f4d1069-f84c-4b28-abe2-500ccee986de'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_10/carpool_1f4d1069-f84c-4b28-abe2-500ccee986de.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'car-with-two-seated-occupants'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    keywords = ('car', 'with', 'two', 'seated', 'occupants')

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

        box('body',6,6,42,38,4)
        for x in (17,31):
            circle(f'head-{x}',x,17,2)
            self.add_line(f'shoulders-{x}',(x-2,27),(x+2,27))
        for x in (10,38):
            self.add_line(f'tire-{x}',(x,38),(x,42));self.relate('connect',f'tire-{x}','body')
