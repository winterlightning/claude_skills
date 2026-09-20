'Pair of Casual Trousers.\nPlan: Mirrored two-leg trousers with waistband and V inseam. Bounds8,4..40,44. Omit pocket stitches.\nReference: No useful Lucide trouser match; source outline and wide crotch opening.\nKeyshape: VRECT_L; constructed to exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a2c03889-7ac9-442f-ab0d-9c1a4fa74e23'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_23/jeans_a2c03889-7ac9-442f-ab0d-9c1a4fa74e23.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'straight-leg-trousers'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('straight', 'leg', 'trousers')

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

        self.add_polyline('trousers',(12,4),(36,4),(40,44),(28,44),(24,22),(20,44),(8,44),closed=True)
        self.add_line('waist',(11,14),(37,14));self.relate('connect','waist','trousers')
