'Laundry Water Basin Symbol.\n\nSymbol plan: Basin top repeats four half-elliptical waves around y14, reaching y10. Rounded base reaches y38.\nConstruction reference: No useful exact Lucide match; use regular repeated arcs and tangent rounded bottom corners.\nOriginal reference: SOURCE_PATH below.\n'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a34c8292-28f1-49c8-8eb5-6cace792aaf8'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_36/strait_a34c8292-28f1-49c8-8eb5-6cace792aaf8.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'water-basin'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('water', 'basin')

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

        path('basin',(4,14),[((14,14),5,4,False),((24,14),5,4,True),((34,14),5,4,False),((44,14),5,4,True),(44,30),((36,38),8,8,True),(12,38),((4,30),8,8,True),(4,14)],True)
