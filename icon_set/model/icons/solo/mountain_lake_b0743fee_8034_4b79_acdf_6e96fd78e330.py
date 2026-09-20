'Mountain and Lake Nature Landscape.\nPlan: Two mountain peaks above a shared shore, long shallow wave and short foreground ripple. Bounds6..42.\nReference: Lucide mountain: angular unequal peaks and coherent baseline; source lake waves retained.\nKeyshape: SQUARE, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b0743fee-8034-4b79-acdf-6e96fd78e330'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_24/lake_b0743fee-8034-4b79-acdf-6e96fd78e330.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'mountain-lake'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('mountain', 'lake')

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

        self.add_polyline('mountains',(6,22),(18,6),(28,16),(32,12),(42,22),closed=True)
        path('wave',(6,32),[((18,32),6,1,False),((30,32),6,1,True),((42,32),6,1,False)])
        self.add_line('ripple',(18,42),(30,42))
