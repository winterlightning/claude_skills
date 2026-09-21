'Capsule beside Scored Tablet\nPlan: Diagonal capsule beside round scored tablet; separate full outlines.\nReference: Lucide pill: diagonal capsule with central dividing seam.\nReduction: Keep tablet companion and score; capsule proportions rebalanced on grid.\nKeyshape: SQUARE; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7714e4d5-6335-4742-8da2-1f4c701a33dc'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_30/pills_7714e4d5-6335-4742-8da2-1f4c701a33dc.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'capsule-beside-scored-tablet'
    keyshape = Keyshape.SQUARE
    category = "objects"
    keywords = ('capsule', 'beside', 'scored', 'tablet')

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

        # Diagonal capsule with two smooth rounded ends; smaller scored companion.
        self.add_bezier('capsule',(6,22),((6,18),(10,15),(14,11)),((18,7),(20,6),(24,6)),((29,6),(30,10),(30,14)),((30,18),(25,21),(22,24)),((18,28),(14,32),(10,32)),((6,32),(6,27),(6,22)))
        self.add_contour('capsule-outline','capsule',closed=True)
        self.add_line('seam',(12,13),(24,25));self.relate('connect','seam','capsule-outline')
        circle('tablet',36,36,6)
        
