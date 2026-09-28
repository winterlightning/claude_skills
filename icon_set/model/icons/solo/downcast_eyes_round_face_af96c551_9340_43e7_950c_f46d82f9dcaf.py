'Disappointed Face With Downcast Eyes.\nSymbol plan: Round blank face with two mirrored downcast curved eyelids, no mouth. Outer circle radius20.\nConstruction reference: human_ref/user.svg: circular head construction; no useful exact Lucide facial-expression match.\nOriginal reference: SOURCE_PATH below.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'af96c551-9340-43e7-950c-f46d82f9dcaf'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_17/face disappointed_af96c551-9340-43e7-950c-f46d82f9dcaf.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'downcast-eyes-round-face'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('downcast', 'eyes', 'round', 'face')

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

        circle('face',24,24,20)
        path('left-eye',(13,20),[((19,17),7,5,False)])
        path('right-eye',(29,17),[((35,20),7,5,False)])
