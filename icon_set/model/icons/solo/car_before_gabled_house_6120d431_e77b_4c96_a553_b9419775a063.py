'Car before Gabled House\nPlan: Car foreground at lower left before a gabled house; interrupted house walls reflect occlusion.\nReference: No useful exact Lucide match; supplied reference governs the subject.\nReduction: Small headlights and wheel detail omitted to keep front car and house readable.\nKeyshape: SQUARE; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6120d431-e77b-4c96-a553-b9419775a063'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_29/parking resident_6120d431-e77b-4c96-a553-b9419775a063.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'car-before-gabled-house'
    keyshape = Keyshape.SQUARE
    category = "objects"
    keywords = ('car', 'before', 'gabled', 'house')

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

        self.add_polyline('house',(18,14),(18,14),(30,6),(42,14),(42,34),(35,34))
        
        path('car',(6,30),[(10,22),(22,22),(26,30),(26,38),(6,38),(6,30)],True)
        self.add_line('windshield',(6,30),(26,30));self.relate('connect','windshield','car')
        for i,x in enumerate([10,22]):
            self.add_line(f'tire-{i}',(x,38),(x,42));self.relate('connect',f'tire-{i}','car')
