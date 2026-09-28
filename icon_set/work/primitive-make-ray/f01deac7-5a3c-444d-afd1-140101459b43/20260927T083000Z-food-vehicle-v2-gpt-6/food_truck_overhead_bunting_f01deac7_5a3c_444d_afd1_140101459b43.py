"""Food Truck with Festive Bunting.
Plan: Left-facing truck with one overhead pennant, open serving bay and two integrated wheel arches. Centerline extremes (6,6)-(42,42).
Reference: Lucide truck: distinct cab, body and circular wheels.
Reduction: Both overhead flags retained; two broad awning scallops replace the three small scallops; wheel outlines merge into the chassis.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'f01deac7-5a3c-444d-afd1-140101459b43'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__food-truck-overhead-bunting/20260927T075459Z-thuan-mac-1/reference/food truck_f01deac7-5a3c-444d-afd1-140101459b43.svg'
AUTHOR = 'gpt-6'


class Batch25Icon(Solo48):
    icon_id = 'food-truck-overhead-bunting'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "events"
    categories = ("primitives", "events")
    aliases = ()
    keywords = ('food', 'truck', 'with', 'festive', 'bunting')

    def build(self):
        # Two pennants above a left-facing serving van. Repeated arches share radii.
        self.add_line('cord',(6,6),(42,6))
        for i,left in enumerate((8,28)):
            self.add_polyline(f'pennant-{i}',(left,6),(left+6,14),(left+12,6))
            self.relate('connect','cord',f'pennant-{i}')

        def line(name,a,b):
            self.add_line(name,a,b)
        line('cab-front',(6,34),(6,29))
        line('cab-slope',(6,29),(13,22))
        line('cab-roof',(13,22),(22,22))
        for i,x in enumerate((22,32)):
            self.add_arc(f'awning-{i}',(x,22),(x+10,22),radius_x=5,radius_y=4,sweep=False)
        line('rear',(42,22),(42,34))
        line('rear-step',(42,34),(38,34))
        line('rear-wheel-side',(38,34),(38,38))
        self.add_arc('rear-wheel',(38,38),(30,38),radius_x=4,sweep=True)
        line('rear-wheel-return',(30,38),(30,34))
        line('middle-base',(30,34),(18,34))
        line('front-wheel-side',(18,34),(18,38))
        self.add_arc('front-wheel',(18,38),(10,38),radius_x=4,sweep=True)
        line('front-wheel-return',(10,38),(10,34))
        line('front-base',(10,34),(6,34))
        self.add_contour('truck','cab-front','cab-slope','cab-roof','awning-0','awning-1','rear','rear-step','rear-wheel-side','rear-wheel','rear-wheel-return','middle-base','front-wheel-side','front-wheel','front-wheel-return','front-base',closed=True)
        line('cab-divider',(22,22),(22,34))
        self.relate('connect','truck','cab-divider')
