'Compact Sedan Car.\nPlan: Side-view sedan with tapered cabin, window divider and equal round wheels. Body ends at outer wheel sides and underside joins inner wheel sides. Bounds4,8..44,40.\nReference: Lucide car-front construction adapted to source side silhouette and paired wheels.\nKeyshape: HRECT_L, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a8826295-f724-421c-a77c-9ad80c607681'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_39/vehicle_a8826295-f724-421c-a77c-9ad80c607681.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'small-sedan'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('small', 'sedan')

    def build(self):
        def path(name, start, steps, closed=False):
            members = []
            point = start
            for index, step in enumerate(steps):
                member = f"{name}-{index}"
                if len(step) == 2:
                    self.add_line(member, point, step)
                    point = step
                else:
                    end, rx, ry, sweep = step
                    self.add_arc(member, point, end, radius_x=rx, radius_y=ry, sweep=sweep)
                    point = end
                members.append(member)
            self.add_contour(name, *members, closed=closed)

        def circle(name, x, y, radius):
            path(name, (x-radius,y), [((x+radius,y),radius,radius,True),
                 ((x-radius,y),radius,radius,True)], True)

        def box(name, left, top, right, bottom, radius):
            r = radius
            path(name, (left+r,top), [(right-r,top), ((right,top+r),r,r,True),
                 (right,bottom-r), ((right-r,bottom),r,r,True), (left+r,bottom),
                 ((left,bottom-r),r,r,True), (left,top+r), ((left+r,top),r,r,True)], True)

        circle('rear-wheel',12,35,5);circle('front-wheel',36,35,5)
        path('body',(7,35),[(4,30),(4,24),((8,20),4,4,True),(10,20),(18,8),(24,8),(30,8),(38,20),(40,20),((44,24),4,4,True),(44,30),(41,35)])
        self.add_polyline('window',(10,20),(24,20),(38,20));self.relate('connect','window','body')
        self.add_line('divider',(24,8),(24,20));self.relate('connect','divider','body');self.relate('connect','divider','window')
        self.relate('connect','body','rear-wheel');self.relate('connect','body','front-wheel')
        self.add_line('underside',(17,35),(31,35));self.relate('connect','underside','rear-wheel');self.relate('connect','underside','front-wheel')
