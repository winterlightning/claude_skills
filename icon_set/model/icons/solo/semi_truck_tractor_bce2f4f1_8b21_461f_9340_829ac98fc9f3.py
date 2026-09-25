'Semi Truck Tractor.\nPlan: Side-view tractor cab with high chassis, three equal wheels and short axle connections. Window division joins the windscreen edge.\nReference: Lucide truck: stepped cab and attached wheels; source three-wheel tractor layout retained.\nKeyshape: HRECT_L, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bce2f4f1-8b21-461f-9340-829ac98fc9f3'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_38/truck cargo 1_bce2f4f1-8b21-461f-9340-829ac98fc9f3.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'semi-truck-tractor'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('semi', 'truck', 'tractor')

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

        for j,x in enumerate((7,23,41)):circle(f'wheel-{j}',x,37,3)
        self.add_polyline('cab',(28,24),(28,8),(36,8),(40,16),(44,20),(44,24),(41,24),(28,24))
        self.add_polyline('chassis',(4,24),(7,24),(23,24),(28,24));self.relate('connect','chassis','cab')
        for j,x in enumerate((7,23,41)):self.add_line(f'axle-{j}',(x,24),(x,34));self.relate('connect',f'axle-{j}',f'wheel-{j}');self.relate('connect',f'axle-{j}','cab' if j==2 else 'chassis')
        self.add_line('windshield',(32,16),(40,16));self.relate('connect','windshield','cab')
