'Whole Mangosteen Fruit.\nPlan: Round fruit body with three lobed crown and short stem; bounds8,4..40,44. Omit overlapping calyx seams.\nReference: No useful mangosteen Lucide match; source crown and round body kept as coherent outline.\nKeyshape: VRECT_L, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3b4eb865-d202-4a0c-bb39-24d21fd9db07'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_20/fruit mangosteen_3b4eb865-d202-4a0c-bb39-24d21fd9db07.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'mangosteen-with-rounded-crown'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('mangosteen', 'with', 'rounded', 'crown')

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

        path('fruit',(12,18),[((8,28),16,16,False),((40,28),16,16,False),((36,18),16,16,False)])
        path('crown',(12,18),[((12,10),4,4,True),((20,10),4,4,True),((28,10),4,4,True),((36,10),4,4,True),((36,18),4,4,True),(12,18)])
        self.relate('connect','fruit','crown')
        self.add_line('stem',(24,4),(24,6));self.relate('connect','stem','crown')
