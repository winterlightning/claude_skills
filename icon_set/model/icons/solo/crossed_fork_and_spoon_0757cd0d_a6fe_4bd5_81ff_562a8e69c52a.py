'Crossed Fork and Spoon.\n\nSymbol plan: Crossed spoon and fork handles share junction(28,30). Fork reduced to two widely separated tines; round spoon bowl radius5 replaces source oval for readable opening.\nConstruction reference: Lucide utensils-crossed: diagonal tools with a clear central crossing; source spoon retained.\nOriginal reference: SOURCE_PATH below.\n'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0757cd0d-a6fe-4bd5-81ff-562a8e69c52a'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_39/utensil_0757cd0d-a6fe-4bd5-81ff-562a8e69c52a.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'crossed-fork-and-spoon'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('crossed', 'fork', 'and', 'spoon')

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

        circle('spoon',37,11,5)
        self.add_polyline('spoon-handle',(34,15),(28,30),(7,42))
        self.relate('connect','spoon','spoon-handle')
        path('fork',(6,6),[(6,14),((14,22),8,8,False),((22,14),8,8,False),(22,6)])
        self.add_polyline('fork-handle',(14,22),(28,30),(42,42))
        self.relate('connect','fork','fork-handle')
        self.relate('connect','fork-handle','spoon-handle')
