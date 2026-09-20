'Drinking Glass with Water.\nPlan: Tapered drinking glass and single wavy water surface. Bounds8,4..40,44.\nReference: Lucide glass-water: tapered walls and shared wavy surface.\nKeyshape: VRECT_L, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '34a460c1-99e1-4757-9b55-ce2bf85e1d92'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_21/glass water_34a460c1-99e1-4757-9b55-ce2bf85e1d92.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'tapered-glass-of-water'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('tapered', 'glass', 'of', 'water')

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

        path('glass',(8,4),[(40,4),(38,18),(34,40),((30,44),4,4,True),(18,44),((14,40),4,4,True),(10,18),(8,4)],True)
        path('water',(10,18),[((24,18),7,2,False),((38,18),7,2,True)]);self.relate('connect','glass','water')
