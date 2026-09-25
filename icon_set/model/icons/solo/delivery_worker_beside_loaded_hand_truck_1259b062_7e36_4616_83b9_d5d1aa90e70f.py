from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1259b062-7e36-4616-83b9-d5d1aa90e70f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/delivery/warehouse cart worker_1259b062-7e36-4616-83b9-d5d1aa90e70f.svg'
AUTHOR = "gpt-6"


class Drawing(Solo48):
    icon_id = 'delivery-worker-beside-loaded-hand-truck'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "delivery"
    aliases = ()
    keywords = ('worker', 'cart', 'handtruck', 'parcel', 'delivery', 'courier', 'person', 'warehouse')

    def build(self):
        # Plan: worker at right with detached circular head and upright torso; single parcel cart at left.
        # Centerline envelope: (6,6)-(42,42). Reference: human_ref/full_body_ref.png for worker; parcel and cart from supplied source.
        def circle(name, x, y, r):
            self.add_arc(name+'-top', (x-r,y), (x+r,y), radius_x=r)
            self.add_arc(name+'-bottom', (x+r,y), (x-r,y), radius_x=r)
            self.add_contour(name, name+'-top', name+'-bottom', closed=True)
        def path(name, *points, closed=False):
            self.add_polyline(name, *points, closed=closed)
        def join(a,b):
            self.relate('connect', a,b)

        # human_ref/full_body_ref.png: head bottom 16, torso start 24 -> 4u ink gap.
        circle('head',34,11,5)
        self.add_line('cap-brim',(39,11),(42,11));join('head','cap-brim')
        self.add_line('torso',(34,24),(34,34))
        path('legs',(28,42),(34,34),(40,42));join('torso','legs')
        path('arm',(34,24),(28,31));join('torso','arm')
        self.mark_human_figure('worker',head='head',torso='torso',torso_junction='start')
        path('parcel',(6,18),(16,18),(16,28),(6,28),closed=True)
        path('cart',(6,28),(16,28),(16,10),(20,10));join('parcel','cart')
        circle('wheel',12,39,3)
        self.add_line('axle',(12,28),(12,36));join('axle','cart');join('axle','parcel');join('axle','wheel')
