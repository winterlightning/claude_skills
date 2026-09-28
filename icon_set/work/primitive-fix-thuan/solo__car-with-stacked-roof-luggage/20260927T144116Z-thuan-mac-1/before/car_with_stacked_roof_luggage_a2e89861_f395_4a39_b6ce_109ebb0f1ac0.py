# Final repair: Restore two stacked suitcases using8-unit tiers; small-circle wheels remain separate.
'Car with Stacked Roof Luggage\nPlan: Two luggage tiers integrate into car roof; wheel radii and baseline shared.\nReference: Lucide car original and atomic-debug: paired wheel/body construction.\nReduction: Omit doors; retain two stacked luggage pieces.\nKeyshape: HRECT_L; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a2e89861-f395-4a39-b6ce-109ebb0f1ac0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_09/car truck luggage_a2e89861-f395-4a39-b6ce-109ebb0f1ac0.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'car-with-stacked-roof-luggage'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    keywords = ('car', 'with', 'stacked', 'roof', 'luggage')

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

        path('body',(6,30),[(14,22),(34,22),(42,30),(6,30)],True)
        for x in (14,34):circle(f'wheel-{x}',x,40,2)
        self.add_polyline('lower-case',(14,22),(14,14),(34,14),(34,22));self.relate('connect','body','lower-case')
        self.add_polyline('upper-case',(20,14),(20,6),(28,6),(28,14));self.relate('connect','lower-case','upper-case')
