'Ship Sailing on Water.\nPlan: Front-facing ship with a pitched hull and a tall narrow deck above a separate wave. Small windows and mast omitted for clearance.\nReference: Lucide ship: pointed bow and raised deckhouse, shared upper structure.\nKeyshape: SQUARE, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e68f3d28-f6f0-4f6d-ad10-cde3965357f3'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_23/hull_e68f3d28-f6f0-4f6d-ad10-cde3965357f3.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'front-view-ship-on-water'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('front', 'view', 'ship', 'on', 'water')

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

        self.add_polyline('hull',(6,22),(12,20),(24,16),(36,20),(42,22),(36,30),(12,30),closed=True)
        self.add_polyline('deck',(12,20),(14,6),(24,6),(34,6),(36,20));self.relate('connect','deck','hull')
        
        path('water',(6,41),[((18,41),6,1,False),((30,41),6,1,True),((42,41),6,1,False)])
