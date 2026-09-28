'Cable Car Cabin Hanging from Wire\nPlan: Cable bar with centered hanger and rounded cabin; single broad window.\nReference: Lucide cable-car: central hanger and round cabin corners.\nReduction: One undivided window matches reference.\nKeyshape: SQUARE; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1cbe0fa3-d908-4523-9409-acc3acb54a15'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_34/ski lift_1cbe0fa3-d908-4523-9409-acc3acb54a15.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'cable-car-cabin-hanging-from-wire'
    keyshape = Keyshape.SQUARE
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    keywords = ('cable', 'car', 'cabin', 'hanging', 'from', 'wire')

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

        self.add_line('cable',(6,6),(42,6));self.add_line('hanger',(24,6),(24,16));self.relate('connect','cable','hanger')
        box('cabin',6,16,42,42,6);self.relate('connect','hanger','cabin')
        box('window',15,25,33,33,3)
