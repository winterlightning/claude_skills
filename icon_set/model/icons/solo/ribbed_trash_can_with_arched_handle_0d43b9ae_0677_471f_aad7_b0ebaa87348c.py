'Trash Can with Lid.\nPlan: Tapered body with two ribs, broad lid and arched handle. Mirrored about24; bounds8,4..40,44.\nReference: Lucide trash-2: lid, upper handle, sparse vertical ribs.\nKeyshape: VRECT_L, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0d43b9ae-0677-471f-aad7-b0ebaa87348c'
SOURCE_PATH = 'pictographic-primitives/other/trash_0d43b9ae-0677-471f-aad7-b0ebaa87348c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'ribbed-trash-can-with-arched-handle'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('ribbed', 'trash', 'can', 'with', 'arched', 'handle')

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

        self.add_polyline('lid',(8,12),(10,12),(16,12),(32,12),(38,12),(40,12))
        path('handle',(16,12),[((32,12),8,8,True)]);self.relate('connect','handle','lid')
        path('bin',(10,12),[(12,40),((16,44),4,4,False),(32,44),((36,40),4,4,False),(38,12)]);self.relate('connect','bin','lid')
        for x in (20,28):self.add_line(f'rib-{x}',(x,22),(x,34))
