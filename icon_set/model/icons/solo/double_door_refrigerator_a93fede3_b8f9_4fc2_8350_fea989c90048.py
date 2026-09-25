'Double Door Refrigerator.\n\nSymbol plan: Rounded upright refrigerator with a horizontal door seam at y24 and two short handles spaced in the two door panels. Bounds (8,4)-(40,44).\nConstruction reference: Lucide refrigerator: rounded cabinet and structural door separator.\nOriginal reference: SOURCE_PATH below.\n'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a93fede3-b8f9-4fc2-8350-fea989c90048'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_32/refrigerator_a93fede3-b8f9-4fc2-8350-fea989c90048.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'double-door-refrigerator'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('double', 'door', 'refrigerator')

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

        path('cabinet',(12,4),[(36,4),((40,8),4,4,True),(40,24),(40,40),((36,44),4,4,True),(12,44),((8,40),4,4,True),(8,24),(8,8),((12,4),4,4,True)],True)
        self.add_line('seam',(8,24),(40,24))
        self.relate('connect','cabinet','seam')
        for j,y in enumerate((13,33)): self.add_line(f'handle-{j}',(17,y),(17,y+2))
