'Skewered Round Appetizer\nPlan: Round topping on upright skewer above broad snack and lower base.\nReference: No useful exact Lucide match; supplied reference governs the subject.\nReduction: Retain the defining silhouette and visible parts.\nKeyshape: VRECT_L; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b426a11d-9817-4dc4-b46f-d72c03eb3ff1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_03/appetiser_b426a11d-9817-4dc4-b46f-d72c03eb3ff1.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'skewered-round-appetizer'
    keyshape = Keyshape.VRECT_L
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    keywords = ('skewered', 'round', 'appetizer')

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

        circle('topping',24,13,5)
        self.add_line('skewer-top',(24,4),(24,8));self.relate('connect','skewer-top','topping')
        self.add_line('skewer-bottom',(24,18),(24,26));self.relate('connect','skewer-bottom','topping')
        box('snack',8,26,40,36,5);self.relate('connect','snack','skewer-bottom')
        path('base',(14,36),[(14,40),((18,44),4,4,False),(30,44),((34,40),4,4,False),(34,36)])
        self.relate('connect','snack','base')
