'Simple Manual Toothbrush.\nSymbol plan: Diagonal round-ended toothbrush shaft with three repeated bristles. Bristle roots(26,30),(34,22),(42,14), each extending8 left and8 up. Body outline thickness and extra bristles omitted; extrema(6,6)-(42,42).\nConstruction reference: Lucide brush: coherent diagonal tool and rounded end construction.\nOriginal reference: SOURCE_PATH below.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c34cfd53-4164-42f5-92e3-fa800780972e'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_38/toothbrush_c34cfd53-4164-42f5-92e3-fa800780972e.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'diagonal-manual-toothbrush'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('diagonal', 'manual', 'toothbrush')

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

        self.add_polyline('handle',(6,42),(26,30),(34,22),(42,14))
        for j,(x,y) in enumerate(((26,30),(34,22),(42,14))):
            self.add_line(f'bristle-{j}',(x,y),(x-8,y-8))
            self.relate('connect','handle',f'bristle-{j}')
