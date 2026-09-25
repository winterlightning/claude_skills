'Hands Pointing in Opposite Directions.\nPlan: Opposing pointing hands share one outline definition rotated180 degrees. Index fingers remain8 wide and palms are offset for separation. Bounds6..42; thumb joint detail simplified.\nReference: human_ref construction for human parts; Lucide hand: rounded digits with one coherent palm outline; source opposed gestures.\nKeyshape fitted to exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0998d16d-9a1b-484a-9195-ce50de19084e'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_19/fingers point opposite direction_0998d16d-9a1b-484a-9195-ce50de19084e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'opposing-pointing-hands'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('opposing', 'pointing', 'hands')

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

        for j,flip in enumerate((False,True)):
         def pt(x,y):return (48-x,48-y) if flip else (x,y)
         path(f'hand-{j}',pt(6,18),[pt(6,12),pt(12,6),pt(16,10),pt(28,10),(pt(28,18),4,4,True),pt(18,18),pt(16,22),pt(10,22),(pt(6,18),4,4,True)],True)
