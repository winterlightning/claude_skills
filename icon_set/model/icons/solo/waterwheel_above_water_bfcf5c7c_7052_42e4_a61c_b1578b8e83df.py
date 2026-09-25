'Traditional Water Mill Wheel.\nPlan: Circular waterwheel radius12 centered24,18 with four radial spokes and one low wave at40..42. Duplicate rim, hub ring and diagonal spokes omitted to open the quadrants. Overall bounds6..42.\nReference: Lucide ship-wheel: circular rim and radial shared spokes; source water line retained.\nKeyshape fitted to exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bfcf5c7c-7052-42e4-a61c-b1578b8e83df'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_40/waterwheel_bfcf5c7c-7052-42e4-a61c-b1578b8e83df.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'waterwheel-above-water'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('waterwheel', 'above', 'water')

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

        circle('rim',24,18,12)
        self.add_polyline('spoke-horizontal',(12,18),(24,18),(36,18));self.relate('connect','spoke-horizontal','rim')
        self.add_polyline('spoke-vertical',(24,6),(24,18),(24,30));self.relate('connect','spoke-vertical','rim');self.relate('connect','spoke-horizontal','spoke-vertical')
        path('water',(6,41),[((18,41),6,1,False),((30,41),6,1,True),((42,41),6,1,False)])
