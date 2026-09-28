'Simple Lily Flower.\nPlan: Pointed three-petal bloom over a straight stem. Petal seams omitted; symmetric x24. Bounds8,4..40,44.\nReference: Lucide flower: coherent repeated petal silhouette; source pointed lily crown retained.\nKeyshape: VRECT_L, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2a90ace3-fd93-45b4-8b42-8e1f04614e29'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_25/lily_2a90ace3-fd93-45b4-8b42-8e1f04614e29.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'lily-flower'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('lily', 'flower')

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

        path('bloom',(8,14),[(16,18),(24,4),(32,18),(40,14),(40,18),((24,34),16,16,True),((8,18),16,16,True),(8,14)],True)
        self.add_line('stem',(24,34),(24,44));self.relate('connect','stem','bloom')
