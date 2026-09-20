'Front Loading Washing Machine.\nPlan: Rounded cabinet with two control points and broad circular door. Control separator omitted to preserve openings. Bounds8,4..40,44.\nReference: Lucide washing-machine: rounded shell, top controls and circular front door.\nKeyshape: VRECT_L, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c2a943ba-cacb-5a74-a64e-f06eba88f8ee'
SOURCE_PATH = 'pictographic-primitives/wayfinding/laundry machine_c2a943ba-cacb-5a74-a64e-f06eba88f8ee.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'front-loading-washing-machine-c2a943ba'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('front', 'loading', 'washing', 'machine', 'c2a943ba')

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

        box('cabinet',8,4,40,44,4)
        for x in (17,31):self.add_dot(f'control-{x}',(x,13))
        circle('door',24,28,7)
