'Two Open Cupped Hands.\nPlan: Mirrored open hands with tall outer fingers and inward palms. Fingers grouped; interior creases omitted. Bounds6..42.\nReference: human_ref human-part vocabulary; Lucide hand: coherent rounded digits and palm, source cupped gesture retained.\nKeyshape: SQUARE, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c1ff8321-3ac1-48fc-bdd4-880798eeea3c'
SOURCE_PATH = 'pictographic-primitives/other/hand holding_c1ff8321-3ac1-48fc-bdd4-880798eeea3c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'two-open-cupped-hands'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('two', 'open', 'cupped', 'hands')

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
         def pt(x,y):return (48-x,y) if flip else (x,y)
         path(f'hand-{j}',pt(10,42),[pt(10,34),pt(6,28),pt(6,10),(pt(14,10),4,4,not flip),pt(14,20),pt(20,26),pt(20,42)])
