'Small Sitting Dog.\nPlan: Right-facing seated dog with pointed ear, rounded muzzle, front-leg division and short raised tail. Small face details omitted. Bounds6..42.\nReference: Lucide dog: pointed ears and smooth muzzle; original seated profile and raised tail preserved.\nKeyshape: SQUARE, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '797d409f-7759-414b-ad4d-9d0962e69876'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_24/lapdog_797d409f-7759-414b-ad4d-9d0962e69876.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'seated-lapdog'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('seated', 'lapdog')

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

        path('dog',(24,6),[(30,14),(34,14),((42,22),8,8,True),((34,30),8,8,True),(34,38),((38,42),4,4,False),(24,42),(18,42),((10,34),8,8,True),(12,28),(22,18),(24,6)],True)
        path('tail',(10,34),[((6,26),4,8,True),(6,20)]);self.relate('connect','tail','dog')
        self.add_line('front-leg',(24,30),(24,42));self.relate('connect','front-leg','dog')
