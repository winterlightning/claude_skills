'Car Front View.\nPlan: Broad front body, tapered windshield, paired headlights and short tires. Bounds4,8..44,40.\nReference: Lucide car-front: tapered cabin, rounded body and paired lamps.\nKeyshape: HRECT_L, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a678adda-8e3f-4b9e-b599-298896c2a8ef'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_38/transporter 5_a678adda-8e3f-4b9e-b599-298896c2a8ef.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'front-view-car'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('front', 'view', 'car')

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

        path('body',(8,18),[(40,18),((44,22),4,4,True),(44,32),((40,36),4,4,True),(38,36),(10,36),(8,36),((4,32),4,4,True),(4,22),((8,18),4,4,True)],True)
        self.add_polyline('windshield',(8,18),(14,8),(34,8),(40,18));self.relate('connect','body','windshield')
        for x in (14,34):self.add_dot(f'light-{x}',(x,27))
        for x in (10,38):self.add_line(f'tire-{x}',(x,36),(x,40));self.relate('connect',f'tire-{x}','body')
