'Stylized Fire Flame.\n\nSymbol plan: Open flame spiral with one dominant tapered tongue and inner curl. Secondary crown points omitted to preserve clear spacing; deliberate asymmetry retained.\nConstruction reference: Lucide flame: one flowing outline with an inward curl.\nOriginal reference: SOURCE_PATH below.\n'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e904c953-0865-4d74-8329-e7cfe84eaa77'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_19/firefox logo_e904c953-0865-4d74-8329-e7cfe84eaa77.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'curled-fox-flame-emblem'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('curled', 'fox', 'flame', 'emblem')

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

        path('flame',(8,18),[(8,28),((24,44),16,16,False),((40,28),16,16,False),((24,4),16,24,False),(28,16),((20,24),8,8,False),((32,24),6,6,False)])
