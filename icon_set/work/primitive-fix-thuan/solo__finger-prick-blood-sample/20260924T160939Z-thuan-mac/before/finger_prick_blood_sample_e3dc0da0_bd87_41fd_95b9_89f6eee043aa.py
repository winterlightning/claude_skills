'Finger Prick Blood Test.\n\nSymbol plan: Hand with raised thumb and right-pointing finger occupies upper half. Blood drop extends from y29 to y40 below finger y20, leaving9 centerline units. Curled finger subdivisions omitted.\nConstruction reference: Lucide hand: coherent rounded digit contour; blood drop is the physical sample.\nOriginal reference: SOURCE_PATH below.\n'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e3dc0da0-bd87-41fd-95b9-89f6eee043aa'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_24/laboratory test blood finger_e3dc0da0-bd87-41fd-95b9-89f6eee043aa.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'finger-prick-blood-sample'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('finger', 'prick', 'blood', 'sample')

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

        path('hand',(4,16),[(16,8),((24,12),8,4,True),(40,12),((40,20),4,4,True),(25,20)])
        path('palm',(4,28),[(16,32),(24,32)])
        path('drop',(39,29),[(44,35),((34,35),5,5,True),(39,29)],True)
