'Human Foot.\nPlan: Left-facing bare foot with curved toe, sole and heel and two open ankle contours. Bounds6..42; natural asymmetric silhouette.\nReference: Human reference vocabulary; Lucide footprints smooth anatomical contours, source side profile preserved.\nKeyshape: SQUARE, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '701d2de1-4e8d-4d6a-a231-6a023e70c571'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_22/heel_701d2de1-4e8d-4d6a-a231-6a023e70c571.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'foot-and-ankle-profile'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('foot', 'and', 'ankle', 'profile')

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

        path('foot',(30,6),[(30,16),((22,28),8,12,True),(10,32),((6,36),4,4,False),((12,42),6,6,False),(32,42),((42,32),10,10,False),(38,20),(38,6)])
