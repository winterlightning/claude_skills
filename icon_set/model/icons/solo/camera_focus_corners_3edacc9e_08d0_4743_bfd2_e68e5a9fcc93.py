'Square Camera Focus Viewfinder.\nPlan: Four mirrored rounded focus brackets. Each corner has radius4 and arms12; exact extrema6..42.\nReference: Lucide scan: four quarter-circle corners with tangent straight arms.\nKeyshape: SQUARE; constructed to exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3edacc9e-08d0-4743-bfd2-e68e5a9fcc93'
SOURCE_PATH = 'pictographic-primitives/other/square focus_3edacc9e-08d0-4743-bfd2-e68e5a9fcc93.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'camera-focus-corners'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('camera', 'focus', 'corners')

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

        for j,(sx,sy) in enumerate(((1,1),(-1,1),(-1,-1),(1,-1))):
         def pt(x,y):return (24+sx*x,24+sy*y)
         path(f'corner-{j}',pt(6,18),[pt(14,18),(pt(18,14),4,4,sx*sy<0),pt(18,6)])
