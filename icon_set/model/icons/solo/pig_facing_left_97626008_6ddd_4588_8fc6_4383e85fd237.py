'Standing Farm Pig.\n\nSymbol plan: One integrated left-facing pig contour, with snout, pointed ear, two legs and attached short curled tail. No coin slot or decorative eye added.\nConstruction reference: Lucide piggy-bank: integrated legs and snout, rounded back; no coin slot added.\nOriginal reference: SOURCE_PATH below.\n'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '97626008-6ddd-4588-8fc6-4383e85fd237'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_18/farrow_97626008-6ddd-4588-8fc6-4383e85fd237.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'pig-facing-left'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('pig', 'facing', 'left')

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

        path('pig',(4,20),[(10,20),(12,16),(10,8),(20,14),(32,14),((40,22),8,8,True),(40,32),(36,40),(28,40),(28,32),(20,32),(16,40),(8,40),(8,30),(4,30),(4,20)],True)
        path('tail',(40,22),[((44,18),4,4,False)])
        self.relate('connect','pig','tail')
