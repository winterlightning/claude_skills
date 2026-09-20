'Cupcake with Frosting.\nPlan: Domed frosting above tapered wrapper, scalloped drip edge with one deep central drip. Bounds8,4..40,44.\nReference: No local Lucide cupcake match; coherent dome and shared icing/wrapper boundary from source.\nKeyshape: VRECT_L, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '156c4fd4-cbf2-4e71-83f1-9eefe3e7f03c'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_23/icing_156c4fd4-cbf2-4e71-83f1-9eefe3e7f03c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'cupcake-with-dripping-frosting'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('cupcake', 'with', 'dripping', 'frosting')

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

        path('frosting',(8,24),[((14,12),6,12,True),((34,12),10,8,True),((40,24),6,12,True),((30,24),5,4,True),((18,24),6,8,True),((8,24),5,4,True)],True)
        path('wrapper',(8,24),[(12,40),((16,44),4,4,False),(32,44),((36,40),4,4,False),(40,24)])
        self.relate('connect','frosting','wrapper')
