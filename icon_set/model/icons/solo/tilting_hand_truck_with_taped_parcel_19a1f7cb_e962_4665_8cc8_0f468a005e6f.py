from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '19a1f7cb-e962-4665-8cc8-0f468a005e6f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/delivery/warehouse cart package ribbon_19a1f7cb-e962-4665-8cc8-0f468a005e6f.svg'
AUTHOR = "gpt-6"


class Drawing(Solo48):
    icon_id = 'tilting-hand-truck-with-taped-parcel'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "delivery"
    categories = ("delivery", "primitives")
    aliases = ()
    keywords = ('handtruck', 'cart', 'parcel', 'package', 'warehouse', 'delivery', 'wheel', 'trolley')

    def build(self):
        # Plan: tilted parcel rests against the cart frame; one outlined wheel and raised handle.
        # Centerline extremes: (6,6)-(42,42). Construction: Original tilted hand truck; Lucide package for carton.
        def path(name,*points,closed=False):
            self.add_polyline(name,*points,closed=closed)
        def circle(name,x,y,r):
            self.add_arc(name+'-top',(x-r,y),(x+r,y),radius_x=r)
            self.add_arc(name+'-bottom',(x+r,y),(x-r,y),radius_x=r)
            self.add_contour(name,name+'-top',name+'-bottom',closed=True)
        def join(a,b):
            self.relate('connect',a,b)

        path('parcel',(9,14),(18,15),(27,16),(25,34),(7,32),closed=True)
        self.add_line('tape',(18,15),(17,23));join('tape','parcel')
        self.add_bezier('handle',(27,16),((29,8),(29,6),(36,6)),((38,6),(40,6),(42,6)))
        join('handle','parcel')
        circle('wheel',29,37,5);join('wheel','parcel')
        self.add_line('toe',(6,34),(7,32));join('toe','parcel')
