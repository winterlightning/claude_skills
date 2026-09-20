'Cute Teddy Bear Toy.\nPlan: Blank rounded head with integrated ears and one coherent seated body-and-feet contour. Two rounded feet and a broad central notch retain the teddy silhouette. Bounds8,4..40,44; inner ears and separate finger lines omitted.\nReference: No useful local Lucide teddy match; source seated toy proportions and rounded construction.\nKeyshape fitted to exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd06262b9-37c7-4bc4-9fe3-489ad5036090'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_37/teddy bear_d06262b9-37c7-4bc4-9fe3-489ad5036090.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'seated-teddy-bear'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('seated', 'teddy', 'bear')

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

        path('head',(14,14),[((10,8),4,6,True),((18,8),4,4,True),((30,8),12,4,True),((38,8),4,4,True),((34,14),4,6,True),((14,14),10,12,True)],True)
        path('body',(14,24),[((8,34),6,10,False),(8,38),((20,38),6,6,False),(20,36),(28,36),(28,38),((40,38),6,6,False),(40,34),((34,24),6,10,False)])
        self.relate('connect','head','body')
