'Water Tap Faucet.\nPlan: Left-down spout, horizontal inlet and central valve stem with crossbar. Bounds6..42. One outline and two true attachments.\nReference: No useful local Lucide faucet match; source physical connections and rounded pipe elbow.\nKeyshape: SQUARE, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1bf11cfe-b2be-48cc-97f3-4d58300679e0'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_18/faucet_1bf11cfe-b2be-48cc-97f3-4d58300679e0.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'tap-faucet-with-crossbar-handle'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('tap', 'faucet', 'with', 'crossbar', 'handle')

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

        path('pipe',(6,42),[(6,30),((18,18),12,12,True),(24,18),(42,18),(42,30),(20,30),((18,32),2,2,False),(18,42),(6,42)],True)
        self.add_line('stem',(24,6),(24,18));self.relate('connect','stem','pipe')
        self.add_polyline('handle',(14,6),(24,6),(34,6));self.relate('connect','stem','handle')
