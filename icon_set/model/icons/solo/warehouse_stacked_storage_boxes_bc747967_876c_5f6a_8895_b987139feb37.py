'Warehouse with Stacked Storage Boxes.\nPlan: Arched warehouse encloses a three-box stack sharing its floor. Exact bounds6..42. Omit tape and roof tick.\nReference: Lucide warehouse: coherent building outline and integrated interior storage.\nKeyshape: SQUARE; constructed to exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bc747967-876c-5f6a-8895-b987139feb37'
SOURCE_PATH = 'pictographic-primitives/shipping/warehouse storage_bc747967-876c-5f6a-8895-b987139feb37.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'warehouse-stacked-storage-boxes'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'shipping'
    aliases = ()
    keywords = ('warehouse', 'stacked', 'storage', 'boxes')

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

        path('building',(6,42),[(6,18),((42,18),18,12,True),(42,42),(32,42),(16,42),(6,42)],True)
        self.add_polyline('lower-boxes',(16,42),(16,32),(20,32),(24,32),(28,32),(32,32),(32,42))
        self.add_polyline('upper-box',(20,32),(20,24),(28,24),(28,32))
        self.add_line('box-divider',(24,32),(24,42))
        self.relate('connect','building','lower-boxes'); self.relate('connect','building','box-divider');self.relate('connect','lower-boxes','upper-box');self.relate('connect','lower-boxes','box-divider')
