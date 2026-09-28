'Car Wheel Fender.\nPlan: Right-facing front car section with curved roof and attached circular wheel; hood lifted for clearance. Hub omitted. Bounds4,8..44,40.\nReference: Lucide car: smooth hood and attached circular wheel; deliberate cropped section follows source.\nKeyshape: HRECT_L, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3db3961f-b690-449d-b4da-3a42295c5b5d'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_18/fender_3db3961f-b690-449d-b4da-3a42295c5b5d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'front-car-section-with-wheel'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('front', 'car', 'section', 'with', 'wheel')

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

        circle('wheel',30,34,6)
        path('upper-body',(4,8),[(14,8),((26,18),12,10,True),(40,18),((44,22),4,4,True),(44,26),(36,34)]);self.relate('connect','upper-body','wheel')
        path('lower-body',(4,20),[(4,30),((8,34),4,4,False),(24,34)]);self.relate('connect','lower-body','wheel')
