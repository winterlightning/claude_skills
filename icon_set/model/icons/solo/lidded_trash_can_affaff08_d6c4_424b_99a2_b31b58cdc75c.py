'Garbage Bin with Lid.\nPlan: Tapered waste bin, broad lid and raised handle; three ribs reduced to two. Bounds8,4..40,44.\nReference: Lucide trash-2: lid, centered handle and sparse vertical ribs.\nKeyshape: VRECT_L, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'affaff08-d6c4-424b-99a2-b31b58cdc75c'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_38/trash can_affaff08-d6c4-424b-99a2-b31b58cdc75c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'lidded-trash-can'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('lidded', 'trash', 'can')

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
        self.add_polyline('handle',(16,12),(16,4),(32,4),(32,12));self.relate('connect','handle','lid')
        path('bin',(10,12),[(12,40),((16,44),4,4,False),(32,44),((36,40),4,4,False),(38,12)]);self.relate('connect','bin','lid')
        for x in (20,28):self.add_line(f'rib-{x}',(x,22),(x,34))
