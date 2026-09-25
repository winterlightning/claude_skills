'Commercial Passenger Airplane.\nPlan: One right-facing aircraft outline with broad swept wings, flared tail and rounded nose. Lower wing widened for clearance. Bounds4,8..44,40.\nReference: Lucide plane: continuous wing/fuselage silhouette; source horizontal heading retained.\nKeyshape fitted to exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3297cd8c-f784-4a07-8f3e-82b7e7146b94'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_01/airbus_3297cd8c-f784-4a07-8f3e-82b7e7146b94.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'airplane-right-facing-full-wings'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('airplane', 'right', 'facing', 'full', 'wings')

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

        path('airplane',(4,18),[(12,22),(20,22),(14,8),(24,8),(34,22),(40,22),((44,26),4,4,True),((40,30),4,4,True),(34,30),(24,40),(12,40),(18,30),(4,30),(6,24),(4,18)],True)
