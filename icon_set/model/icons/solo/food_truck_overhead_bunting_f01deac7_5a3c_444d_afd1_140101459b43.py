"""Food Truck with Festive Bunting.
Plan: Left-facing truck with one overhead pennant, open serving bay and two integrated wheel arches. Centerline extremes (6,6)-(42,42).
Reference: Lucide truck: distinct cab, body and circular wheels.
Reduction: Two overhead flags reduced to one; two broad awning scallops replace the three small scallops; wheel outlines merge into the chassis.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f01deac7-5a3c-444d-afd1-140101459b43'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/events/food truck_f01deac7-5a3c-444d-afd1-140101459b43.svg'
AUTHOR = 'gpt-6'


class Batch25Icon(Solo48):
    icon_id = 'food-truck-overhead-bunting'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "events"
    aliases = ()
    keywords = ('food', 'truck', 'with', 'festive', 'bunting')

    def build(self):
        self.add_polyline('cord',(6,6),(22,6),(42,6))
        self.add_polyline('pennant',(6,6),(14,15),(22,6))
        self.relate('connect','cord','pennant')
        self.add_line('cab-1',(6,36),(6,28))
        self.add_line('cab-2',(6,28),(14,24))
        self.add_line('cab-3',(14,24),(22,24))
        for i,x in enumerate((22,32)):
            self.add_arc(f'awning-{i}',(x,24),(x+10,24),radius_x=5,radius_y=4,sweep=False)
        self.add_line('rear-1',(42,24),(42,36))
        self.add_arc('wheel-right',(42,36),(30,36),radius_x=6,sweep=True)
        self.add_line('base-right',(30,36),(22,36))
        self.add_line('base-left',(22,36),(18,36))
        self.add_arc('wheel-left',(18,36),(6,36),radius_x=6,sweep=True)
        self.add_contour('truck','cab-1','cab-2','cab-3','awning-0','awning-1','rear-1','wheel-right','base-right','base-left','wheel-left',closed=True)
        self.add_line('cab-divider',(22,24),(22,36))
        self.relate('connect','truck','cab-divider')
