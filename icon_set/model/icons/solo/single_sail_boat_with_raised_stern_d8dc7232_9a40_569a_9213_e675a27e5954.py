from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd8dc7232-9a40-569a-9213-e675a27e5954'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/crime/piracy ship_d8dc7232-9a40-569a-9213-e675a27e5954.svg'
AUTHOR = "gpt-6"


class Drawing(Solo48):
    icon_id = 'single-sail-boat-with-raised-stern'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/transport"
    aliases = ()
    keywords = ('boat', 'sailing', 'sail', 'mast', 'hull', 'nautical', 'vessel', 'ship')

    def build(self):
        # Plan: one broad square sail, shared mast attachment, asymmetric stepped hull.
        # Centerline envelope: (4,8)-(44,40). Reference: Lucide sailboat: separated sail and curved hull.
        def circle(name, x, y, r):
            self.add_arc(name+'-top', (x-r,y), (x+r,y), radius_x=r)
            self.add_arc(name+'-bottom', (x+r,y), (x-r,y), radius_x=r)
            self.add_contour(name, name+'-top', name+'-bottom', closed=True)
        def path(name, *points, closed=False):
            self.add_polyline(name, *points, closed=closed)
        def join(a,b):
            self.relate('connect', a,b)

        path('sail', (14,8),(34,8),(32,20),(16,20),closed=True)
        self.add_line('mast', (24,20),(24,30)); join('sail','mast')
        path('hull-top',(4,27),(12,30),(24,30),(34,30),(34,24),(44,24),(44,30))
        self.add_bezier('hull-bottom',(44,30),((44,37),(39,40),(32,40)),((14,40),(10,40),(4,27)))
        self.add_contour('hull','hull-top-1','hull-top-2','hull-top-3','hull-top-4','hull-top-5','hull-top-6','hull-bottom',closed=True)
        # Replace the polyline grouping with the complete continuous hull.
        self.contours = [c for c in self.contours if c.contour_id != 'hull-top']
        join('mast','hull')
