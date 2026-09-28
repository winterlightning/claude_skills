'Ladder in a Room.\nPlan: Leaning ladder within two open room walls and floor. Perspective corner reduced; two rungs plus floor-level step. Bounds6..42.\nReference: No local Lucide ladder match; repeated rung construction and source room enclosure.\nKeyshape: SQUARE, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '68e8e8af-8c77-4a05-a6b5-c03e10d88d01'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_22/home improvement 5_68e8e8af-8c77-4a05-a6b5-c03e10d88d01.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'ladder-in-room-corner'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('ladder', 'in', 'room', 'corner')

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

        self.add_polyline('room',(6,6),(6,42),(14,42),(26,42),(42,42),(42,6))
        self.add_polyline('rail-left',(22,10),(20,18),(17,30),(14,42));self.add_polyline('rail-right',(34,10),(32,18),(29,30),(26,42));self.relate('connect','rail-left','room');self.relate('connect','rail-right','room')
        for j,(a,b) in enumerate((((20,18),(32,18)),((17,30),(29,30)))):self.add_line(f'rung-{j}',a,b);self.relate('connect',f'rung-{j}','rail-left');self.relate('connect',f'rung-{j}','rail-right')
