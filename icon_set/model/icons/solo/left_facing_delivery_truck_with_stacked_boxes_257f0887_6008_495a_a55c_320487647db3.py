from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '257f0887-6008-495a-a55c-320487647db3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/delivery/delivery truck packages_257f0887-6008-495a-a55c-320487647db3.svg'
AUTHOR = "gpt-6"


class Drawing(Solo48):
    icon_id = 'left-facing-delivery-truck-with-stacked-boxes'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "delivery"
    aliases = ()
    keywords = ('truck', 'delivery', 'boxes', 'packages', 'vehicle', 'cargo', 'wheel', 'transport')

    def build(self):
        # Plan: left-facing truck with two cargo boxes stacked; paired wheel definition.
        # Centerline envelope: (4,8)-(44,40). Reference: Lucide truck: circular wheels, interrupted lower chassis.
        def circle(name, x, y, r):
            self.add_arc(name+'-top', (x-r,y), (x+r,y), radius_x=r)
            self.add_arc(name+'-bottom', (x+r,y), (x-r,y), radius_x=r)
            self.add_contour(name, name+'-top', name+'-bottom', closed=True)
        def path(name, *points, closed=False):
            self.add_polyline(name, *points, closed=closed)
        def join(a,b):
            self.relate('connect', a,b)

        for x in (12,36):
            circle('wheel-'+str(x),x,37,3)
            self.add_line('suspension-'+str(x),(x,26),(x,34))
            join('suspension-'+str(x),'wheel-'+str(x));join('suspension-'+str(x),'body')

        path('body',(4,26),(4,18),(12,10),(20,10),(20,26),(44,26),(44,8),(28,8),(28,16),(20,16))
        self.add_line('cab-bottom',(4,26),(20,26));join('cab-bottom','body');join('cab-bottom','suspension-12')
        self.add_line('stack',(28,16),(44,16));join('stack','body')
