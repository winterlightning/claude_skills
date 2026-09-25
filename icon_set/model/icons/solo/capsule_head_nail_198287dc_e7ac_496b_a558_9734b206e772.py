'Metal Construction Nail.\n\nSymbol plan: A broad horizontal capsule head and centered tapering shaft. Head extremes (10,4)-(38,16), shaft width 8 reaches tip y=44.\nConstruction reference: Lucide hard-hat brim: simple cap with a separately joined stem; source requires capsule rather than domed head.\nOriginal reference: SOURCE_PATH below.\n'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '198287dc-e7ac-496b-a558-9734b206e772'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_36/stud_198287dc-e7ac-496b-a558-9734b206e772.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'capsule-head-nail'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('capsule', 'head', 'nail')

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

        path('head',(16,4),[(32,4),((32,16),6,6,True),(28,16),(20,16),(16,16),((16,4),6,6,True)],True)
        path('shaft',(20,16),[(20,36),(24,44),(28,36),(28,16)])
        self.relate('connect','head','shaft')
