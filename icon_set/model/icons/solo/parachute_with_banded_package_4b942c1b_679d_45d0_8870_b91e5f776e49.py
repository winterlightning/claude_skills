from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4b942c1b-679d-45d0-8870-b91e5f776e49'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/delivery/delivery parachute_4b942c1b-679d-45d0-8870-b91e5f776e49.svg'
AUTHOR = "gpt-6"


class Drawing(Solo48):
    icon_id = 'parachute-with-banded-package'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/delivery"
    aliases = ()
    keywords = ('parachute', 'package', 'parcel', 'canopy', 'delivery', 'airdrop', 'band', 'cargo')

    def build(self):
        # Plan: symmetric canopy and banded parcel; two equal corner suspension cords.
        # Centerline extremes: (8,4)-(40,44). Construction: Original parachute; Lucide package for banded box.
        def path(name,*points,closed=False):
            self.add_polyline(name,*points,closed=closed)
        def circle(name,x,y,r):
            self.add_arc(name+'-top',(x-r,y),(x+r,y),radius_x=r)
            self.add_arc(name+'-bottom',(x+r,y),(x-r,y),radius_x=r)
            self.add_contour(name,name+'-top',name+'-bottom',closed=True)
        def join(a,b):
            self.relate('connect',a,b)

        axis, radius, canopy_y = 24,16,20
        self.add_arc('canopy',(axis-radius,canopy_y),(axis+radius,canopy_y),radius_x=radius)
        self.add_line('canopy-edge',(8,20),(40,20));join('canopy','canopy-edge')

        path('parcel',(14,28),(34,28),(34,36),(34,44),(14,44),(14,36),closed=True)
        self.add_line('band',(14,36),(34,36));join('band','parcel')
        for side in (-1,1):
            self.add_line('cord-'+str(side),(24+side*16,20),(24+side*10,28))
            for part in ('canopy','canopy-edge','parcel'):join('cord-'+str(side),part)
