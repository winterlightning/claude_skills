'Car beside Raised Boom Gate\nPlan: Raised boom at left over front car; eight-unit-wide gate post and broad windshield.\nReference: No useful exact Lucide match; supplied reference governs the subject.\nReduction: Remove barrier stripes and tiny lamps; raised gate arm and car remain.\nKeyshape: SQUARE; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3174776c-73dc-4890-9691-92194e9c2a36'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_29/parking ramp 1_3174776c-73dc-4890-9691-92194e9c2a36.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'car-raised-boom-gate'
    keyshape = Keyshape.SQUARE
    category = "primitives-generate"
    keywords = ('car', 'raised', 'boom', 'gate')

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

        self.add_polyline('post',(6,42),(6,20),(14,20),(14,42),(6,42))
        self.add_polyline('boom',(14,20),(24,6),(42,6));self.relate('connect','boom','post')
        self.add_polyline('car',(22,38),(22,30),(26,20),(38,20),(42,30),(42,38),(22,38))
        self.add_line('windshield',(22,30),(42,30));self.relate('connect','windshield','car')
        for i,x in enumerate([26,38]):
            self.add_line(f'tire-{i}',(x,38),(x,42));self.relate('connect',f'tire-{i}','car')
