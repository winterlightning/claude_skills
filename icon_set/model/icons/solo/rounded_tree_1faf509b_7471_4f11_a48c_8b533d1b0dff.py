'Simple Deciduous Tree.\nPlan: Three-lobed crown, shared trunk and ground, symmetric about24. Bounds6..42.\nReference: Lucide tree-deciduous: lobed silhouette and single shared trunk.\nKeyshape: SQUARE, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1faf509b-7471-4f11-a48c-8b533d1b0dff'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_40/woodland_1faf509b-7471-4f11-a48c-8b533d1b0dff.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'rounded-tree'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('rounded', 'tree')

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

        path('crown',(6,22),[((14,14),8,8,True),((34,14),10,8,True),((42,22),8,8,True),((34,30),8,8,True),(24,30),(14,30),((6,22),8,8,True)],True)
        self.add_polyline('trunk',(24,22),(24,30),(24,42));self.relate('connect','trunk','crown')
        self.add_polyline('ground',(6,42),(24,42),(42,42));self.relate('connect','ground','trunk')
