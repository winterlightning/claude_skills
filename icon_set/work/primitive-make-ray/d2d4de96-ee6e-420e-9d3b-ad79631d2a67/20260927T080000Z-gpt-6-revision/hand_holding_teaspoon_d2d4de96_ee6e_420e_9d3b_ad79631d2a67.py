"""Hand Holding Teaspoon.

Symbol plan: Oval spoon at left; rising shaft connects to a curved gripping thumb and palm; extrema (4,8)-(44,40).
Construction reference: Shared human reference and Lucide hand-grab for simplified grip; utensils for shaft/bowl.
Reduction: Reduced finger creases and used a single-line spoon handle; sideways spoon kept.
Keyshape centerline extremes follow the SOLO48 contract; stroke 4, integer grid.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'd2d4de96-ee6e-420e-9d3b-ad79631d2a67'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hand-holding-teaspoon/20260927T075452Z-thuan-mac-1/reference/tea spoon_d2d4de96-ee6e-420e-9d3b-ad79631d2a67.svg'
AUTHOR = "gpt-6"


class HandHoldingTeaspoon(Solo48):
    icon_id = 'hand-holding-teaspoon'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    categories = ("primitives", "food")
    aliases = ()
    keywords = ('hand', 'holding', 'teaspoon')

    def build(self):
        self.loop('bowl',11,20,7,6)
        self.add_line('shaft',(18,20),(29,17))
        self.path('thumb',(44,40),[(40,30),((36,27),(37,21),(34,17)),(29,17)])
        self.add_line('handle',(29,17),(44,8))
        self.path('fingers',(29,17),[((27,20),(27,23),(27,26)),((27,30),(29,32),(32,32))])
        for a,b in [('shaft','bowl'),('shaft','thumb'),('shaft','handle'),('thumb','handle'),('fingers','thumb'),('fingers','shaft'),('fingers','handle')]:self.relate('connect',a,b)

    def loop(self, name, x, y, rx, ry=None):
        ry = rx if ry is None else ry
        self.add_arc(name+'-top', (x-rx,y), (x+rx,y), radius_x=rx, radius_y=ry)
        self.add_arc(name+'-bottom', (x+rx,y), (x-rx,y), radius_x=rx, radius_y=ry)
        self.add_contour(name, name+'-top', name+'-bottom', closed=True)

    def path(self, name, start, commands, closed=False):
        ids=[]
        point=start
        for i,command in enumerate(commands):
            key=f'{name}-{i}'
            if len(command)==2:
                self.add_line(key, point, command)
                point=command
            else:
                c1,c2,end=command
                self.add_bezier(key, point, (c1,c2,end))
                point=end
            ids.append(key)
        self.add_contour(name, *ids, closed=closed)
