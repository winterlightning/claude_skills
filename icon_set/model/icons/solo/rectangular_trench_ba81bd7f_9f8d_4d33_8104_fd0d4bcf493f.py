'Rectangular U-Shaped Trench.\nPlan: U-shaped excavation profile with broad top shoulders and rounded inside corners. Bounds4,8..44,40; inner floor26.\nReference: No useful Lucide trench match; one coherent U-shaped contour.\nKeyshape: HRECT_L; constructed to exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ba81bd7f-9f8d-4d33-8104-fd0d4bcf493f'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_38/trench_ba81bd7f-9f8d-4d33-8104-fd0d4bcf493f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'rectangular-trench'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('rectangular', 'trench')

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

        path('trench',(4,8),[(14,8),(14,20),((20,26),6,6,False),(28,26),((34,20),6,6,False),(34,8),(44,8),(44,40),(4,40),(4,8)],True)
