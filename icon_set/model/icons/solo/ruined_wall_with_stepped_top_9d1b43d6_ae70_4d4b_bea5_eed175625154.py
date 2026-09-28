'Ruined Wall with Stepped Top\nPlan: Stepped ruin wall with round entrance and extended base; asymmetric stepped silhouette retained.\nReference: No useful exact Lucide match; supplied reference governs the subject.\nReduction: Retain the defining silhouette and visible parts.\nKeyshape: SQUARE; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9d1b43d6-ae70-4d4b-bea5-eed175625154'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_33/ruin_9d1b43d6-ae70-4d4b-bea5-eed175625154.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'ruined-wall-with-stepped-top'
    keyshape = Keyshape.SQUARE
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    keywords = ('ruined', 'wall', 'with', 'stepped', 'top')

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

        self.add_polyline('wall',(6,42),(6,24),(14,24),(14,16),(24,16),(24,6),(34,6),(34,26),(42,26),(42,42),(30,42))
        path('door',(30,42),[(30,32),((18,32),6,6,False),(18,42),(6,42)])
        self.relate('connect','wall','door')
