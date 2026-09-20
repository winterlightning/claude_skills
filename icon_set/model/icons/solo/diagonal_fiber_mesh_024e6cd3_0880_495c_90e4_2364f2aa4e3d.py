'Woven Mesh Grid Pattern.\nPlan: Crossed series of diagonal strands at12-unit axis intervals; open ends, no enclosing border. Bounds6..42.\nReference: Lucide grid-3x3: regular shared intersections; source diagonal mesh retained.\nKeyshape: SQUARE, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '024e6cd3-0880-495c-90e4-2364f2aa4e3d'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_18/fiberglass_024e6cd3-0880-495c-90e4-2364f2aa4e3d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'diagonal-fiber-mesh'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('diagonal', 'fiber', 'mesh')

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

        for j,(a,b) in enumerate((((6,18),(30,42)),((6,6),(42,42)),((18,6),(42,30)))):self.add_line(f'down-{j}',a,b)
        for j,(a,b) in enumerate((((6,30),(30,6)),((6,42),(42,6)),((18,42),(42,18)))):self.add_line(f'up-{j}',a,b)
        for i in range(3):
         for j in range(3):self.relate('connect',f'down-{i}',f'up-{j}')
