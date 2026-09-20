'Hydrofoil Boat on Waves.\nPlan: Streamlined hull spans6..42 at14..24, canopy reaches6, short supporting foil ends30 and one wave spans38..42. Second wave omitted to separate foil from water.\nReference: Lucide sailboat: coherent hull and attached upper structure; source hydrofoil support retained.\nKeyshape fitted to exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cfc8139d-77a2-4608-975d-e1d524f2d534'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_23/hydrofoil_cfc8139d-77a2-4608-975d-e1d524f2d534.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hydrofoil-raised-above-waves'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('hydrofoil', 'raised', 'above', 'waves')

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

        path('hull',(6,22),[((14,14),8,8,True),(18,14),(34,14),(42,14),((30,24),12,10,True),(22,24),(6,24),(6,22)],True)
        self.add_polyline('canopy',(18,14),(18,6),(26,6),(34,14));self.relate('connect','canopy','hull')
        self.add_line('foil',(22,24),(22,30));self.relate('connect','foil','hull')
        path('water',(6,40),[((18,40),6,2,False),((30,40),6,2,True),((42,40),6,2,False)])
