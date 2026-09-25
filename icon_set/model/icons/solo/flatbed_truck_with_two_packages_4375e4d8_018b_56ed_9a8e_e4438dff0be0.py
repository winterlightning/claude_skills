from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4375e4d8-018b-56ed-9a8e-e4438dff0be0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/delivery/delivery truck boxes_4375e4d8-018b-56ed-9a8e-e4438dff0be0.svg'
AUTHOR = "gpt-6"


class Drawing(Solo48):
    icon_id = 'flatbed-truck-with-two-packages'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "delivery"
    aliases = ()
    keywords = ('truck', 'flatbed', 'packages', 'boxes', 'cargo', 'delivery', 'vehicle', 'transport')

    def build(self):
        # Plan: right-facing open flatbed with staggered parcels, same wheel radii.
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

        path('body',(4,26),(44,26),(44,22),(36,12),(28,12),(28,26))
        path('front-box',(4,26),(4,16),(16,16),(16,26));join('front-box','body')
        path('back-box',(12,16),(12,8),(28,8),(28,26));join('back-box','front-box');join('back-box','body')
