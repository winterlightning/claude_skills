'Twisted Licorice Candy.\nPlan: Two interleaved diagonal candy strands in one coherent outline with two widely spaced diagonal divisions. Bounds6..42; deliberate asymmetric twist.\nReference: Lucide candy: diagonal sweet orientation; source twist retained, no wrapper added.\nKeyshape fitted to exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1585cb8b-c5e4-42ee-9bc9-6f53342a6281'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_25/licorice_1585cb8b-c5e4-42ee-9bc9-6f53342a6281.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'twisted-licorice-strands'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('twisted', 'licorice', 'strands')

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

        path('twist',(10,42),[((6,38),4,4,True),(6,34),(18,22),(18,14),(26,6),(34,6),((42,14),8,8,True),(42,18),(30,30),(30,34),(22,42),(10,42)],True)
        self.add_line('seam-upper',(18,22),(42,18));self.relate('connect','twist','seam-upper')
        self.add_line('seam-lower',(6,34),(30,30));self.relate('connect','twist','seam-lower')
