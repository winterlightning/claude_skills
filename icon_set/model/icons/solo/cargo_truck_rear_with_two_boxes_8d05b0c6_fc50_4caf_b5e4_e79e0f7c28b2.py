from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8d05b0c6-fc50-4caf-b5e4-e79e0f7c28b2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/delivery/delivery truck boxes_8d05b0c6-fc50-4caf-b5e4-e79e0f7c28b2.svg'
AUTHOR = "gpt-6"


class Drawing(Solo48):
    icon_id = 'cargo-truck-rear-with-two-boxes'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "delivery"
    categories = ("delivery", "primitives")
    aliases = ()
    keywords = ('truck', 'cargo', 'rear', 'boxes', 'loading', 'delivery', 'bumper', 'transport')

    def build(self):
        # Plan: rear truck with two floor-mounted parcels, paired tires and broad bumper.
        # Centerline envelope: (8,4)-(40,44). Reference: Lucide truck: circular wheels, interrupted lower chassis.
        def circle(name, x, y, r):
            self.add_arc(name+'-top', (x-r,y), (x+r,y), radius_x=r)
            self.add_arc(name+'-bottom', (x+r,y), (x-r,y), radius_x=r)
            self.add_contour(name, name+'-top', name+'-bottom', closed=True)
        def path(name, *points, closed=False):
            self.add_polyline(name, *points, closed=closed)
        def join(a,b):
            self.relate('connect', a,b)

        path('body',(8,34),(8,4),(40,4),(40,34))
        self.add_line('bumper',(8,34),(40,34));join('body','bumper')
        for x in (12,36):
            self.add_line('tire-'+str(x),(x,34),(x,44));join('tire-'+str(x),'bumper')
        path('boxes',(16,34),(16,22),(32,22),(32,34));join('boxes','bumper')
        self.add_line('divider',(24,22),(24,34));join('divider','boxes');join('divider','bumper')
        self.add_line('roof-detail',(17,13),(31,13))
