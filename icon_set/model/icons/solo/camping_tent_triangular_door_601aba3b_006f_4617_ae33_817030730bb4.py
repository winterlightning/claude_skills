'Simple Outdoor Camping Tent.\nPlan: Triangular tent with short sidewalls and central entrance sharing ground. Symmetric x24, bounds6..42.\nReference: Lucide tent: triangular roof, central doorway and shared baseline.\nKeyshape: SQUARE, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '601aba3b-006f-4617-ae33-817030730bb4'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_37/tent_601aba3b-006f-4617-ae33-817030730bb4.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'camping-tent-triangular-door'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('camping', 'tent', 'triangular', 'door')

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

        self.add_polyline('shell',(6,34),(24,6),(42,34),(42,42),(32,42),(16,42),(6,42),closed=True)
        self.add_polyline('door',(16,42),(24,26),(32,42));self.relate('connect','door','shell')
