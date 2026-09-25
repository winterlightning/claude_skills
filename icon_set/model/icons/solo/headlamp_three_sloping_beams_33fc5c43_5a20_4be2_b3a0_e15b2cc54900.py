'Low Beam Headlights.\nPlan: D-shaped lamp at right, three parallel sloping beams at left. Lamp box28,10..44,38; rays spanx4..18.\nReference: No useful Lucide headlamp match; rounded lamp and repeated beam series from source.\nKeyshape: HRECT_M; constructed to exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '33fc5c43-5a20-4be2-b3a0-e15b2cc54900'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_01/adaptive light 2_33fc5c43-5a20-4be2-b3a0-e15b2cc54900.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'headlamp-three-sloping-beams'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('headlamp', 'three', 'sloping', 'beams')

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

        path('lamp',(28,10),[((44,24),16,14,True),((28,38),16,14,True),(28,10)],True)
        for j in range(3):self.add_line(f'beam-{j}',(4,16+j*10),(18,10+j*10))
