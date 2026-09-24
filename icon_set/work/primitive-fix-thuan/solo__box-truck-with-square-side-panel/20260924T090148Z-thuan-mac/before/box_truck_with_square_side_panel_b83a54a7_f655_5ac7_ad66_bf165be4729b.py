from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b83a54a7-f655-5ac7-ad66-bf165be4729b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/delivery/delivery truck_b83a54a7-f655-5ac7-ad66-bf165be4729b.svg'
AUTHOR = "gpt-6"


class Drawing(Solo48):
    icon_id = 'box-truck-with-square-side-panel'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/transport"
    aliases = ()
    keywords = ('truck', 'box', 'vehicle', 'panel', 'cargo', 'delivery', 'transport', 'wheels')

    def build(self):
        # Plan: right-facing box truck with square inset panel and matching circular wheels.
        # Centerline envelope: (4,8)-(44,40). Reference: Lucide truck: circular wheels, interrupted lower chassis.
        def circle(name, x, y, r):
            self.add_arc(name+'-top', (x-r,y), (x+r,y), radius_x=r)
            self.add_arc(name+'-bottom', (x+r,y), (x-r,y), radius_x=r)
            self.add_contour(name, name+'-top', name+'-bottom', closed=True)
        def path(name, *points, closed=False):
            self.add_polyline(name, *points, closed=closed)
        def join(a,b):
            self.relate('connect', a,b)

        for x in (12,36):circle('wheel-'+str(x),x,37,3)
        path('body',(4,26),(4,8),(28,8),(28,26),(44,26),(44,22),(36,16),(28,16))
        path('panel',(12,16),(20,16),(20,24),(12,24),closed=True)
