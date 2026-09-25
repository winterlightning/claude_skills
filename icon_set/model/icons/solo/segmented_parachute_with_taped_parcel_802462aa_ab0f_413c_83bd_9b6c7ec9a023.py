from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '802462aa-ab0f-413c-83bd-9b6c7ec9a023'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/delivery/dropshipper parachute box_802462aa-ab0f-413c-83bd-9b6c7ec9a023.svg'
AUTHOR = "gpt-6"


class Drawing(Solo48):
    icon_id = 'segmented-parachute-with-taped-parcel'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "delivery"
    categories = ("delivery", "primitives")
    aliases = ()
    keywords = ('parachute', 'canopy', 'parcel', 'package', 'airdrop', 'delivery', 'tape', 'cargo')

    def build(self):
        # Plan: symmetric domed canopy, diagonal paired cords, taped parcel; central seam divides canopy.
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

        self.add_line('canopy-seam',(24,4),(24,20));join('canopy-seam','canopy');join('canopy-seam','canopy-edge')
