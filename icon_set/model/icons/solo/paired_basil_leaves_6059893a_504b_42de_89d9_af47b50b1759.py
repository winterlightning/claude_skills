'Two Basil Leaves.\nPlan: Unequal pointed leaf pair on a shared stem. Large upper-right leaf and smaller left leaf; omit tiny veins. Bounds6..42.\nReference: Lucide leaf: pointed organic contour and connected stem; asymmetry follows source.\nKeyshape: SQUARE; constructed to exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6059893a-504b-42de-89d9-af47b50b1759'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_39/vegetable basil leaf_6059893a-504b-42de-89d9-af47b50b1759.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'paired-basil-leaves'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('paired', 'basil', 'leaves')

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

        path('right-leaf',(24,32),[(24,24),((42,6),18,18,True),(42,14),((24,32),18,18,True)],True)
        path('left-leaf',(24,32),[((6,14),18,18,True),((24,32),18,18,True)],True)
        self.add_line('stem',(24,32),(20,42));self.relate('connect','stem','right-leaf');self.relate('connect','stem','left-leaf');self.relate('connect','right-leaf','left-leaf')
