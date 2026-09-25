from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '319237a6-0547-5bd1-8445-07f23d7b1b15'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/delivery/damaged package broken_319237a6-0547-5bd1-8445-07f23d7b1b15.svg'
AUTHOR = "gpt-6"


class Drawing(Solo48):
    icon_id = 'shipping-package-with-zigzag-crack'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "delivery"
    aliases = ()
    keywords = ('package', 'box', 'shipping', 'crack', 'damage', 'tape', 'parcel', 'delivery')

    def build(self):
        # Plan: square carton, short tape and detached zigzag fracture.
        # Centerline envelope: (6,6)-(42,42). Reference: Lucide package: simple carton geometry.
        def circle(name, x, y, r):
            self.add_arc(name+'-top', (x-r,y), (x+r,y), radius_x=r)
            self.add_arc(name+'-bottom', (x+r,y), (x-r,y), radius_x=r)
            self.add_contour(name, name+'-top', name+'-bottom', closed=True)
        def path(name, *points, closed=False):
            self.add_polyline(name, *points, closed=closed)
        def join(a,b):
            self.relate('connect', a,b)

        path('box',(6,6),(42,6),(42,42),(6,42),closed=True)
        self.add_line('tape',(24,6),(24,14));join('box','tape')
        path('crack',(27,22),(21,28),(27,34))
