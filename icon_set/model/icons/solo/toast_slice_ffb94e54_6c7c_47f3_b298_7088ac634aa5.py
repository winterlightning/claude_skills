'Single Slice of Toast.\nPlan: Rounded bread dome with stepped shoulders and broad flat lower crust. Bounds6..42. Omit inset duplicate crust.\nReference: No exact Lucide toast match; continuous rounded silhouette from source.\nKeyshape: SQUARE; constructed to exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ffb94e54-6c7c-47f3-b298-7088ac634aa5'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_38/toast_ffb94e54-6c7c-47f3-b298-7088ac634aa5.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'toast-slice'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('toast', 'slice')

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

        path('bread',(14,6),[(34,6),((42,14),8,8,True),((38,22),8,10,True),(38,38),((34,42),4,4,True),(14,42),((10,38),4,4,True),(10,22),((6,14),8,10,True),((14,6),8,8,True)],True)
