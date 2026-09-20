'Tulip Flower with Leaves.\nPlan: Tulip cup with two pointed outer petals and a central notch, on a straight stem between two broad curved leaves. Tiny central petal omitted for clearance. Bounds6..42.\nReference: Lucide flower: coherent petal silhouette and repeated leaves; source tulip shape retained.\nKeyshape: SQUARE, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '116463a1-6de6-48bb-b7eb-c1f2f14f7def'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_39/violet_116463a1-6de6-48bb-b7eb-c1f2f14f7def.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'tulip-with-leaves-116463a1'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('tulip', 'with', 'leaves', '116463a1')

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

        path('bloom',(16,6),[(24,12),(32,6),(32,16),((24,24),8,8,True),((16,16),8,8,True),(16,6)],True)
        self.add_line('stem',(24,24),(24,42));self.relate('connect','stem','bloom')
        path('leaf-left',(24,42),[(6,26),(6,34),((14,42),8,8,False),(24,42)],True)
        path('leaf-right',(24,42),[(42,26),(42,34),((34,42),8,8,True),(24,42)],True)
        self.relate('connect','leaf-left','stem');self.relate('connect','leaf-right','stem');self.relate('connect','leaf-left','leaf-right')
