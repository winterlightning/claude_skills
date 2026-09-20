'Simple Friendly Toy Robot.\nPlan: Wide round head, paired eyes, tapered body and side appendages. Curved open underside. Bounds8,4..40,44.\nReference: Lucide bot: round rectangle head and paired eye points, attached mechanical body.\nKeyshape: VRECT_L, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f089ee26-f142-4c1c-b152-ec7a121e0b4b'
SOURCE_PATH = 'pictographic-primitives/other/robot toy_f089ee26-f142-4c1c-b152-ec7a121e0b4b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'toy-robot'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('toy', 'robot')

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

        box('head',8,4,40,22,4)
        self.add_dot('eye-left',(17,13));self.add_dot('eye-right',(31,13))
        path('body',(24,22),[(16,32),(16,44),((32,44),8,6,True),(32,32),(24,22)]);self.relate('connect','body','head')
        path('arm-left',(16,32),[((16,44),8,6,False)]);path('arm-right',(32,32),[((32,44),8,6,True)])
        self.relate('connect','arm-left','body');self.relate('connect','arm-right','body')
