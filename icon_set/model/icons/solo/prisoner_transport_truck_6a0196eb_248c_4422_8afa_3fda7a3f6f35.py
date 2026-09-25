"""Prisoner Transport Truck.

Symbol plan: Right-facing barred truck, two wheels and rounded cab; extremes4,8,44,40. Simplify passenger to round head; omit cabin window and shoulders due spacing.
Construction references: Lucide truck: wheels interrupt chassis and cab curves into roof. Source establishes barred transport compartment.
Source SVG establishes subject; geometry is authored fresh on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6a0196eb-248c-4422-8afa-3fda7a3f6f35'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/crime/deliver issue prisoner_6a0196eb-248c-4422-8afa-3fda7a3f6f35.svg'
AUTHOR = 'gpt-6'


class PrisonerTransportTruck(Solo48):
    icon_id = 'prisoner-transport-truck'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "crime"
    aliases = ()
    keywords = ('prisoner', 'transport', 'truck')

    def build(self):
        def path(name, start, steps, closed=False):
            ids = []
            point = start
            for i, step in enumerate(steps):
                member = f"{name}-{i}"
                if len(step) == 2:
                    self.add_line(member, point, step)
                    point = step
                else:
                    end, rx, ry, sweep = step
                    self.add_arc(member, point, end, radius_x=rx, radius_y=ry, sweep=sweep)
                    point = end
                ids.append(member)
            self.add_contour(name, *ids, closed=closed)

        def circle(name, x, y, r):
            path(name, (x-r,y), [((x+r,y),r,r,True), ((x-r,y),r,r,True)], True)

        path('box',(10,36),[(4,28),(4,12),((8,8),4,4,True),(16,8),(28,8),(28,16),(28,28),(24,36),(18,36)])
        path('cab',(28,16),[(36,16),((44,24),8,8,True),(44,28),(42,36)])
        self.add_line('chassis',(24,36),(34,36))
        circle('wheel-left',14,36,4);circle('wheel-right',38,36,4)
        path('head',(16,16),[((20,20),4,4,True),((16,24),4,4,True),((12,20),4,4,True),((16,16),4,4,True)],True)
        self.add_line('bar-top',(16,8),(16,16))
        self.add_line('bar-bottom',(16,24),(16,28))
        for a,b in [('box','cab'),('box','chassis'),('head','bar-top'),('head','bar-bottom'),('box','bar-top'),('box','wheel-left'),('chassis','wheel-right'),('cab','wheel-right')]:self.relate('connect',a,b)
