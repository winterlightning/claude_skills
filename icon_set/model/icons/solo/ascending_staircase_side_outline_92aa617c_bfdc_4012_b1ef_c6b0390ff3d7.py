'Ascending Staircase Side Outline\nPlan: Four equal staircase risers ascend right above long baseline; derive steps from one rise/run.\nReference: No useful exact Lucide match; supplied reference governs the subject.\nReduction: Retain the defining silhouette and visible parts.\nKeyshape: SQUARE; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '92aa617c-bfdc-4012-b1ef-c6b0390ff3d7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_36/stair_92aa617c-bfdc-4012-b1ef-c6b0390ff3d7.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'ascending-staircase-side-outline'
    keyshape = Keyshape.SQUARE
    category = "objects"
    keywords = ('ascending', 'staircase', 'side', 'outline')

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

        points=[(6,42),(6,33)]
        for i in range(4):
            x=6+9*i;y=33-9*i
            if i:points.append((x,y))
            points.append((x+9,y))
        self.add_polyline('steps',*points)
        self.add_line('base',(6,42),(42,42));self.relate('connect','base','steps')
