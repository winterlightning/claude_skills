'Hanging Dome Ceiling Lamp.\n\nSymbol plan: Symmetric ceiling bar, cord and domed shade share x=24. Semicircular shade reaches (4,40)-(44,40), ceiling y=8. Small fitting omitted.\nConstruction reference: Lucide lamp-ceiling: explicit cord-to-shade attachment; retain source ceiling bar and closed flat rim.\nOriginal reference: SOURCE_PATH below.\n'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '76663106-f24c-4da0-9b5d-e969a593f42b'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_24/lamp 2_76663106-f24c-4da0-9b5d-e969a593f42b.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'ceiling-bar-dome-pendant'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('ceiling', 'bar', 'dome', 'pendant')

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

        self.add_polyline('ceiling',(4,8),(24,8),(44,8))
        self.add_line('cord',(24,8),(24,20))
        path('shade',(4,40),[((24,20),20,20,True),((44,40),20,20,True),(4,40)],True)
        self.relate('connect','ceiling','cord')
        self.relate('connect','shade','cord')
