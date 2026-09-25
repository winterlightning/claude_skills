'Two Wheeled Pedal Bicycle.\nPlan: Equal radius7 wheels at11/37,y33, with straight slanted seat post and bent handlebar fork. Rising crossbar attaches above the wheels. Bounds4,8..44,40; hub and pedal detail omitted.\nReference: Lucide bike: equal round wheels and sparse frame; source bicycle has no rider, so none added.\nKeyshape fitted to exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9806d070-4409-411b-96b2-db1e999f5b9a'
SOURCE_PATH = 'pictographic-primitives/other/bike_9806d070-4409-411b-96b2-db1e999f5b9a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'bicycle-with-straight-seat-post'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('bicycle', 'with', 'straight', 'seat', 'post')

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

        circle('rear-wheel',11,33,7);circle('front-wheel',37,33,7)
        self.add_line('seat-post',(11,26),(16,10));self.relate('connect','seat-post','rear-wheel')
        self.add_line('saddle',(14,10),(20,10));self.relate('connect','seat-post','saddle')
        self.add_polyline('fork',(37,26),(34,16),(32,8),(28,8));self.relate('connect','fork','front-wheel')
        self.add_line('frame',(11,26),(34,16));self.relate('connect','frame','seat-post');self.relate('connect','frame','rear-wheel');self.relate('connect','frame','fork')
