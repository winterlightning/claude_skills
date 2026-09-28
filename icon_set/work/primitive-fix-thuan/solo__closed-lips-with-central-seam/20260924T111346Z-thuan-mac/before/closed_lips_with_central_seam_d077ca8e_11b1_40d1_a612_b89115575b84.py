'Human Lips Icon.\nSymbol plan: Mirrored two-lobed upper lip and broad lower lip with a shared middle seam. Centerline box(4,10)-(44,38).\nConstruction reference: No useful exact Lucide lips match; use coherent mirrored circular/elliptical arcs.\nOriginal reference: SOURCE_PATH below.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd077ca8e-11b1-40d1-a612-b89115575b84'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_25/lip_d077ca8e-11b1-40d1-a612-b89115575b84.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'closed-lips-with-central-seam'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('closed', 'lips', 'with', 'central', 'seam')

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

        path('outline',(4,24),[(14,12),((24,12),5,2,True),((34,12),5,2,True),(44,24),((24,38),20,14,True),((4,24),20,14,True)],True)
        self.add_line('seam',(4,24),(44,24))
        self.relate('connect','outline','seam')
