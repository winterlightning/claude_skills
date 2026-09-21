'Side View Bumper Car\nPlan: Bumper base and body share baseline; seat recess and tall power pole preserve side-view ride silhouette.\nReference: No useful exact Lucide match; supplied reference governs the subject.\nReduction: Retain the defining silhouette and visible parts.\nKeyshape: SQUARE; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c91125d2-c955-4285-9428-03593fb9517d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_08/bumper_c91125d2-c955-4285-9428-03593fb9517d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'side-view-bumper-car'
    keyshape = Keyshape.SQUARE
    category = "objects"
    keywords = ('side', 'view', 'bumper', 'car')

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

        box('bumper',6,34,42,42,4)
        self.add_bezier('nose',(6,34),((6,24),(12,22),(18,22)))
        path('seat',(18,22),[(18,22),((22,26),4,4,False),(28,26),((32,22),4,4,False),(32,18),((36,14),4,4,True),(42,14),(42,34)])
        self.relate('connect','nose','seat')
        self.relate('connect','nose','bumper'); self.relate('connect','seat','bumper')
        self.add_line('pole',(42,6),(42,14));self.relate('connect','pole','seat')
