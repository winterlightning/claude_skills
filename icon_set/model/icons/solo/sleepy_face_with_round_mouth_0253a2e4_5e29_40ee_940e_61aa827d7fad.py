'Sleepy Face with Closed Eyes.\nPlan: Round face with paired drooping lids and small open round mouth. Radial radius20.\nReference: No exact local Lucide sleepy face match; eye-closed curve construction informs expression.\nKeyshape: CIRCLE, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0253a2e4-5e29-40ee-940e-61aa827d7fad'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_18/face sleepy_0253a2e4-5e29-40ee-940e-61aa827d7fad.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'sleepy-face-with-round-mouth'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('sleepy', 'face', 'with', 'round', 'mouth')

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

        circle('face',24,24,20)
        path('eye-left',(14,18),[((20,18),3,2,False)]);path('eye-right',(28,18),[((34,18),3,2,False)])
        circle('mouth',24,31,3)
