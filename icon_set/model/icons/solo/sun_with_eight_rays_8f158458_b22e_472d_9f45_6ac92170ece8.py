'Bright Sunny Weather Icon.\nPlan: Disk radius10 and eight symmetric rays. Cardinal endpoints radius20, diagonal endpoints14/14; inner ray endpoints at19 cardinal and13/13 diagonal.\nReference: Lucide sun: central disk and radial marks with consistent clearance.\nKeyshape: CIRCLE; constructed to exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8f158458-b22e-472d-9f45-6ac92170ece8'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_37/sunshine_8f158458-b22e-472d-9f45-6ac92170ece8.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'sun-with-eight-rays-8f158458'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('sun', 'with', 'eight', 'rays')

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

        circle('disk',24,24,10)
        for j,(dx,dy) in enumerate(((1,0),(-1,0),(0,1),(0,-1))):self.add_line(f'ray-{j}',(24+19*dx,24+19*dy),(24+20*dx,24+20*dy))
        for j,(dx,dy) in enumerate(((1,1),(-1,1),(1,-1),(-1,-1))):self.add_line(f'diagonal-{j}',(24+13*dx,24+13*dy),(24+14*dx,24+14*dy))
