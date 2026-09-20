'Happy Smiling Face.\nPlan: Face radius20 centered24; paired round eyes radius2, wide shallow smile. Radial envelope22.\nReference: No exact local Lucide smile match; circular face and coherent curved expression from source.\nKeyshape: CIRCLE, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c982e69c-15f7-43bf-aebb-dd507dd53504'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_17/face grin wide_c982e69c-15f7-43bf-aebb-dd507dd53504.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'smiling-face-with-round-eyes'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('smiling', 'face', 'with', 'round', 'eyes')

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

        circle('face',24,24,20)
        for j,x in enumerate((17,31)):circle(f'eye-{j}',x,18,2)
        path('smile',(14,28),[((34,28),10,7,False)])
