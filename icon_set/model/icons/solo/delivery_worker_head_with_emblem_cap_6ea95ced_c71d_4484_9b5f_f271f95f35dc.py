from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6ea95ced-c71d-4484-9b5f-f271f95f35dc'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/delivery/delivery man give_6ea95ced-c71d-4484-9b5f-f271f95f35dc.svg'
AUTHOR = "gpt-6"


class Drawing(Solo48):
    icon_id = 'delivery-worker-head-with-emblem-cap'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/people"
    aliases = ()
    keywords = ('worker', 'delivery', 'cap', 'head', 'portrait', 'courier', 'uniform', 'person')

    def build(self):
        # Plan: symmetric cap with circular emblem and open circular face; no tiny eyes.
        # Centerline envelope: (8,4)-(40,44). Reference: human_ref/user.svg circular head vocabulary; reference cap silhouette.
        def circle(name, x, y, r):
            self.add_arc(name+'-top', (x-r,y), (x+r,y), radius_x=r)
            self.add_arc(name+'-bottom', (x+r,y), (x-r,y), radius_x=r)
            self.add_contour(name, name+'-top', name+'-bottom', closed=True)
        def path(name, *points, closed=False):
            self.add_polyline(name, *points, closed=closed)
        def join(a,b):
            self.relate('connect', a,b)

        path('crown',(8,24),(8,8),(16,4),(32,4),(40,8),(40,24))
        self.add_line('brim',(8,24),(40,24));join('crown','brim')
        circle('emblem',24,14,2)
        self.add_arc('face-left',(8,28),(16,44),radius_x=20,sweep=False)
        self.add_line('temple-left',(8,24),(8,28));join('face-left','temple-left');join('brim','temple-left');join('crown','temple-left')
        self.add_arc('face-right',(40,28),(32,44),radius_x=20)
        self.add_line('temple-right',(40,24),(40,28));join('face-right','temple-right');join('brim','temple-right');join('crown','temple-right')

