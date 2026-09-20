'Tied Garbage Bag.\nPlan: Bulging bag under a flared tied mouth; symmetric about24. Mouth top4, bag bottom44, widest x8/40. Omit creases.\nReference: No useful Lucide bag match; trash offers coherent outline construction but source bag silhouette retained.\nKeyshape: VRECT_L; constructed to exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2e264ef3-07ff-4487-9102-d6a4c7558f1f'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_20/garb_2e264ef3-07ff-4487-9102-d6a4c7558f1f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'tied-garbage-bag'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('tied', 'garbage', 'bag')

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

        path('bag',(20,14),[(28,14),(36,26),((40,36),20,20,True),((32,44),8,8,True),(16,44),((8,36),8,8,True),((12,26),20,20,True),(20,14)],True)
        self.add_polyline('mouth',(20,14),(16,4),(32,4),(28,14))
        self.relate('connect','bag','mouth')
