"""A diagonal pacifier with a large round handle.
Plan: SQUARE gives the diagonal shield and two attached lobes room.
Reduction: No component removed; enlarged the handle opening.
Construction: Supplied reference governs the diagonal shield, teat, and ring; no useful exact Lucide match used.
Layout: Diagonal asymmetry follows the source. Handle attaches at shared shield nodes (10,18) and (30,38)."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'fcf2e80c-06a5-42d9-a45c-b4984bad2541'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_05/baby care pacifier_fcf2e80c-06a5-42d9-a45c-b4984bad2541.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'diagonal-pacifier-with-a-round-handle'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    keywords = ('diagonal', 'pacifier', 'with', 'a', 'round', 'handle')

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

        path('shield',(6,14),[((14,6),8,8,True),(42,34),((34,42),8,8,True),(30,38),(10,18),(6,14)],True)
        path('teat',(22,14),[(28,8),((40,20),9,9,True),(34,26)])
        self.relate('connect','teat','shield')
        self.add_bezier('handle',(10,18),((7,21),(6,26),(6,30)),((6,37),(11,42),(18,42)),((23,42),(27,41),(30,38)))
        self.relate('connect','handle','shield')
