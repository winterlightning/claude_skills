'Classic Fedora Hat.\nPlan: Pinched fedora crown with exact quarter-circle top corners, flat band boundary and broad curved brim. Bounds4,10..44,38; extra band seam omitted.\nReference: Lucide crown: coherent headwear outline; source fedora retained with rounded brim and central pinch.\nKeyshape fitted to exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd4df5f83-83b6-42eb-bb26-3de3bfdb5f17'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_18/fedora_d4df5f83-83b6-42eb-bb26-3de3bfdb5f17.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'fedora-with-curved-brim'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('fedora', 'with', 'curved', 'brim')

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

        path('crown',(10,28),[(14,14),((18,10),4,4,True),(24,12),(30,10),((34,14),4,4,True),(38,28)])
        path('brim',(10,28),[((4,32),6,4,False),((24,38),20,6,False),((44,32),20,6,False),((38,28),6,4,False)])
        self.add_line('band',(10,28),(38,28))
        self.relate('connect','crown','brim');self.relate('connect','band','brim');self.relate('connect','band','crown')
