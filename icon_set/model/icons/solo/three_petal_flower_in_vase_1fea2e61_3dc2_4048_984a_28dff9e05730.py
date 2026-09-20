'Flower in a Vase.\nPlan: Three-lobed blossom above a central stem and bulbous vase. Bounds8,4..40,44. Leaf details omitted to preserve generous spacing and recognizable flower/vase proportions.\nReference: Lucide flower and sprout: lobed blossom, shared stem and leaf junctions.\nKeyshape fitted to exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1fea2e61-3dc2-4048-984a-28dff9e05730'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_23/ikebana_1fea2e61-3dc2-4048-984a-28dff9e05730.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-petal-flower-in-vase'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('three', 'petal', 'flower', 'in', 'vase')

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

        path('bloom',(16,20),[((16,8),8,6,True),(20,8),((28,8),4,4,True),(32,8),((32,20),8,6,True),(24,20),(16,20)],True)
        self.add_line('stem',(24,20),(24,30));self.relate('connect','stem','bloom')
        path('vase',(16,30),[(24,30),(32,30),(30,34),((32,40),4,6,True),((28,44),4,4,True),(20,44),((16,40),4,4,True),((18,34),4,6,True),(16,30)],True)
        self.relate('connect','stem','vase')
