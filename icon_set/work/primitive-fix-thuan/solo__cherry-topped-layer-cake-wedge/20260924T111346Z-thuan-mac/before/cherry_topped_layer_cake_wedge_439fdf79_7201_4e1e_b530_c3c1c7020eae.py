'Cherry Topped Layer Cake Wedge\nPlan: Cake wedge, single layer seam and round cherry on top.\nReference: No useful exact Lucide match; supplied reference governs the subject.\nReduction: Single layer retained with cherry and stem; perspective reduced to triangular top.\nKeyshape: VRECT_L; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '439fdf79-7201-4e1e-b530-c3c1c7020eae'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_14/dessert_439fdf79-7201-4e1e-b530-c3c1c7020eae.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'cherry-topped-layer-cake-wedge'
    keyshape = Keyshape.VRECT_L
    category = "objects"
    keywords = ('cherry', 'topped', 'layer', 'cake', 'wedge')

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

        path('cake',(8,26),[(40,26),(40,40),((36,44),4,4,True),(8,44),(8,26)],True)
        self.add_line('layer',(8,35),(40,35));self.relate('connect','layer','cake')
        self.add_line('top-left',(8,26),(20,18));self.relate('connect','top-left','cake')
        self.add_bezier('top-right',(30,16),((36,18),(40,21),(40,26)));self.relate('connect','top-right','cake')
        circle('cherry',25,12,5);self.relate('connect','cherry','top-left');self.relate('connect','cherry','top-right')
        self.add_bezier('stem',(25,7),((25,5),(29,4),(32,4)));self.relate('connect','stem','cherry')
