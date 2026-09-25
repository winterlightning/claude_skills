'Car Power Window Switch.\nSymbol plan: Vertical switch body fits VRECT_L(8,4)-(40,44), seam y24. Two opposing chevrons occupy their own bands with8-unit wall clearances.\nConstruction reference: Lucide bot: sparse controls inside one structural body.\nOriginal reference: SOURCE_PATH below.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e8aae3d0-0e34-46f8-b97a-5d2beab999fb'
SOURCE_PATH = 'pictographic-primitives/transportation/power window lockout_e8aae3d0-0e34-46f8-b97a-5d2beab999fb.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'power-window-rocker-switch'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transportation"
    aliases = ()
    keywords = ('power', 'window', 'rocker', 'switch')

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

        self.add_polyline('panel',(8,24),(16,4),(40,4),(40,24),(40,44),(8,44),closed=True)
        self.add_line('seam',(8,24),(40,24));self.relate('connect','panel','seam')
        self.add_polyline('up',(24,16),(28,12),(32,16))
        self.add_polyline('down',(24,32),(28,36),(32,32))
