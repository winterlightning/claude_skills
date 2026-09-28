'Hands Supporting Front Facing Car\nPlan: Front car above cupped hands; hands mirror about vertical center.\nReference: No useful exact Lucide match; supplied reference governs the subject.\nReduction: Hands retain cupped gesture; car lamps and tires omitted. Human reference reviewed; no detached head.\nKeyshape: SQUARE; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f7acffbb-95f3-4cdd-98e2-2243774f9339'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_09/car insurance hands_f7acffbb-95f3-4cdd-98e2-2243774f9339.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hands-supporting-front-facing-car'
    keyshape = Keyshape.SQUARE
    category = "objects"
    keywords = ('hands', 'supporting', 'front', 'facing', 'car')

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

        self.add_polyline('car',(14,14),(17,6),(31,6),(34,14),(34,22),(14,22),(14,14))
        self.add_line('windshield',(14,14),(34,14));self.relate('connect','windshield','car')
        for i,x in enumerate([18,30]):self.add_line(f'tire-{i}',(x,22),(x,26));self.relate('connect',f'tire-{i}','car')
        for side in [-1,1]:
         x=lambda a:24+side*a
         self.add_bezier(f'hand-{side}',(x(8),42),((x(8),37),(x(18),38),(x(18),33)),((x(18),29),(x(18),24),(x(18),24)))
         self.add_bezier(f'fingers-{side}',(x(18),33),((x(17),31),(x(16),32),(x(14),34)))
         self.relate('connect',f'hand-{side}',f'fingers-{side}')
