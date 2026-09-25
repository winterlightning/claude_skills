'Leafy Herb Sprig.\nPlan: Diagonal herb stem with three outlined pointed leaves: paired lower leaves share a node, terminal leaf ends the stem. Two leaves omitted from the source to preserve open leaf interiors. Bounds6..42.\nReference: Lucide sprout: shared stem and branching leaves; source five-leaf count and diagonal growth retained.\nKeyshape fitted to exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '237b3f7c-da2a-4811-9f1a-e857b7bfa693'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_37/tarragon_237b3f7c-da2a-4811-9f1a-e857b7bfa693.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'tarragon-sprig'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('tarragon', 'sprig')

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

        self.add_polyline('stem',(6,42),(18,30),(30,18))
        path('left-leaf',(6,16),[((18,30),12,14,True),((6,16),12,14,True)],True)
        path('right-leaf',(18,30),[((42,42),24,12,True),((18,30),24,12,True)],True)
        path('tip-leaf',(30,18),[((42,6),12,12,True),((30,18),12,12,True)],True)
        for name in ('left-leaf','right-leaf','tip-leaf'):self.relate('connect',name,'stem')
        self.relate('connect','left-leaf','right-leaf')
