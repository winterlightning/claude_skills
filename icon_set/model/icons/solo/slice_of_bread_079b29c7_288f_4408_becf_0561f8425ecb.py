'Slice of Bread.\nPlan: Rounded upper crust with shoulder notches and broad flat slice base. Symmetric x24; bounds6..42.\nReference: No useful local Lucide bread match; recognizable source loaf-slice contour.\nKeyshape: SQUARE, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '079b29c7-288f-4408-becf-0561f8425ecb'
SOURCE_PATH = 'pictographic-primitives/other/bread_079b29c7-288f-4408-becf-0561f8425ecb.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'slice-of-bread'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('slice', 'of', 'bread')

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

        path('bread',(14,6),[(34,6),((42,14),8,8,True),(42,18),((38,22),4,4,True),(38,42),(10,42),(10,22),((6,18),4,4,True),(6,14),((14,6),8,8,True)],True)
