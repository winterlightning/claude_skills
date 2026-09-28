'Traditional Tepee Camping Tent.\nPlan: Crossed poles continuing into triangular sides, ground and central door. Mirrored about24. Bounds6..42.\nReference: Lucide tent: crossed poles and sparse triangular doorway.\nKeyshape: SQUARE, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c2a76793-9b3f-4a82-a7ee-a4c12448e598'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_37/tepee_c2a76793-9b3f-4a82-a7ee-a4c12448e598.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'tepee-tent'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('tepee', 'tent')

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

        self.add_polyline('pole-left',(15,6),(24,18),(42,42));self.add_polyline('pole-right',(33,6),(24,18),(6,42));self.relate('connect','pole-left','pole-right')
        self.add_polyline('ground',(6,42),(16,42),(32,42),(42,42));self.relate('connect','ground','pole-left');self.relate('connect','ground','pole-right')
        self.add_polyline('door',(16,42),(24,32),(32,42));self.relate('connect','door','ground')
