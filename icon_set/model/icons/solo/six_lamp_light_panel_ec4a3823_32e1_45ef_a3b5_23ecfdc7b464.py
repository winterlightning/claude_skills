'Rectangular Stadium Floodlight.\nPlan: Rounded panel with six lamps on an equal two-by-three grid and central support. Lamps reduced to solid points. Bounds4,8..44,40.\nReference: No useful exact Lucide floodlight match; rounded housing and shared grid parameters preserve six-lamp identity.\nKeyshape: HRECT_L, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ec4a3823-32e1-45ef-a3b5-23ecfdc7b464'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_25/light 3_ec4a3823-32e1-45ef-a3b5-23ecfdc7b464.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'six-lamp-light-panel'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('six', 'lamp', 'light', 'panel')

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

        path('panel',(8,8),[(40,8),((44,12),4,4,True),(44,32),((40,36),4,4,True),(24,36),(8,36),((4,32),4,4,True),(4,12),((8,8),4,4,True)],True)
        for y in (17,27):
         for x in (13,24,35):self.add_dot(f'lamp-{x}-{y}',(x,y))
        self.add_line('support',(24,36),(24,40));self.relate('connect','support','panel')
