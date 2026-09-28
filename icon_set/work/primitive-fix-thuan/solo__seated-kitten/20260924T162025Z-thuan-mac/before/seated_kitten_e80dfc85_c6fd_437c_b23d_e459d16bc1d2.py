'Sitting Pet Cat.\nPlan: Seated kitten with pointed ears, broad haunches, a tail integrated into the outer silhouette and one foreleg division. Face details omitted.\nReference: Lucide cat: pointed ears and rounded cheeks; source seated body and tail retained.\nKeyshape: VRECT_L, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e80dfc85-c6fd-437c-b23d-e459d16bc1d2'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_24/kitten_e80dfc85-c6fd-437c-b23d-e459d16bc1d2.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'seated-kitten'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('seated', 'kitten')

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

        path('cat',(12,4),[(22,10),(26,10),(36,4),(36,18),(32,26),(40,36),(40,40),((36,44),4,4,True),(24,44),(16,44),((8,36),8,8,True),(8,30),(18,26),(12,18),(12,4)],True)
        
        self.add_line('forelegs',(24,34),(24,44));self.relate('connect','forelegs','cat')
