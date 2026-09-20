'Shopping Bag with Price Tag.\nPlan: Shopping bag with one arched handle and an attached hanging tag. The tag opening and second handle are omitted to preserve clear spaces.\nReference: Lucide shopping-bag: rounded body and arch; attached physical price tag retained from source.\nKeyshape: SQUARE, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '13e62362-e504-42d4-92b4-09cbc6528e6c'
SOURCE_PATH = 'pictographic-primitives/shopping/shopping bag tag_13e62362-e504-42d4-92b4-09cbc6528e6c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'shopping-bag-with-attached-tag'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('shopping', 'bag', 'with', 'attached', 'tag')

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

        path('bag',(8,20),[(28,20),(34,20),(36,38),((32,42),4,4,True),(10,42),((6,38),4,4,True),(8,20)],True)
        path('handle',(10,20),[(10,14),((24,14),7,7,True),(24,20)]);self.relate('connect','handle','bag')
        self.add_polyline('tag',(34,20),(34,6),(42,6),(42,14),(34,20),closed=True);self.relate('connect','tag','bag')
