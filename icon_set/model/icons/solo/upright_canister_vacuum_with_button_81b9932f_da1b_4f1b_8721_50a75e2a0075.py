'Upright Canister Vacuum with Button\nPlan: Upright canister with button and looping hose descending to flared head.\nReference: No useful exact Lucide match; supplied reference governs the subject.\nReduction: Remove lower seam; preserve upright canister, control and flared head.\nKeyshape: SQUARE; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '81b9932f-da1b-4f1b-8721-50a75e2a0075'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_11/cleaning vacuum_81b9932f-da1b-4f1b-8721-50a75e2a0075.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'upright-canister-vacuum-with-button'
    keyshape = Keyshape.SQUARE
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    keywords = ('upright', 'canister', 'vacuum', 'with', 'button')

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

        box('body',6,23,24,42,5);self.add_dot('button',(15,32))
        path('hose',(14,23),[(14,12),((36,12),11,6,True),(36,34)]);self.relate('connect','hose','body')
        self.add_polyline('head',(33,42),(33,34),(41,34),(42,42),(33,42));self.relate('connect','head','hose')
