'Simple House with Central Window.\nPlan: Triangular roof with short eaves and broad facade containing one square window. Roof baseline omitted for openness. Bounds6..42.\nReference: Lucide house: coherent gabled outer contour and simple rectangular opening.\nKeyshape: SQUARE, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a64010b4-698e-4833-b3f8-40d48dae2a00'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_36/studio_a64010b4-698e-4833-b3f8-40d48dae2a00.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'house-with-square-window'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('house', 'with', 'square', 'window')

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

        self.add_polyline('house',(6,22),(24,6),(42,22),(38,22),(38,42),(10,42),(10,22),(6,22),closed=True)
        box('window',20,25,28,33,1)
