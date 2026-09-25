from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '734736e5-bf3e-4609-a14a-a79a08ae1a13'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/delivery/delivery parachute_734736e5-bf3e-4609-a14a-a79a08ae1a13.svg'
AUTHOR = "gpt-6"


class Drawing(Solo48):
    icon_id = 'parachute-carrying-taped-parcel'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "delivery"
    aliases = ()
    keywords = ('parachute', 'parcel', 'package', 'delivery', 'canopy', 'tape', 'airdrop', 'cargo')

    def build(self):
        # Plan: symmetric domed canopy, diagonal paired cords, taped parcel; plain canopy.
        # Centerline extremes: (8,4)-(40,44). Construction: Original parachute; Lucide package for clear parcel divisions.
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

        path('parcel',(16,32),(24,32),(32,32),(32,44),(16,44),closed=True)
        for side in (-1,1):
            self.add_line('cord-'+str(side),(24+side*16,20),(24+side*8,32))
            for part in ('canopy','canopy-edge','parcel'):join('cord-'+str(side),part)
        self.add_line('tape',(24,32),(24,36));join('tape','parcel')
