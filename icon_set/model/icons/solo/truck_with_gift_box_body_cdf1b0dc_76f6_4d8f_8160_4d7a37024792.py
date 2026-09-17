from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cdf1b0dc-76f6-4d8f-8160-4d7a37024792'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/delivery/truck gift_cdf1b0dc-76f6-4d8f-8160-4d7a37024792.svg'
AUTHOR = "gpt-6"


class Drawing(Solo48):
    icon_id = 'truck-with-gift-box-body'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/transport"
    aliases = ()
    keywords = ('truck', 'gift', 'box', 'ribbon', 'bow', 'delivery', 'vehicle', 'present')

    def build(self):
        # Plan: left-facing gift truck: cargo rectangle, single ribbon and paired bow loops.
        # Centerline envelope: (4,8)-(44,40). Reference: Lucide gift: paired bow loops and central ribbon; truck wheels.
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

        path('body',(4,26),(4,18),(12,18),(20,26),(44,26),(44,18),(20,18),(20,26),(4,26))
        self.add_line('ribbon',(32,18),(32,26));join('ribbon','body')
        self.add_arc('bow-left',(24,18),(32,18),radius_x=4,radius_y=10)
        self.add_arc('bow-right',(32,18),(40,18),radius_x=4,radius_y=10)
        for a,b in [('bow-left','body'),('bow-right','body'),('bow-left','bow-right'),('bow-left','ribbon'),('bow-right','ribbon')]:join(a,b)
