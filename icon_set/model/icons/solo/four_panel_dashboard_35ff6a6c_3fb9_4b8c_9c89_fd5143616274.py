'Dashboard Grid Panels.\nPlan: Four rounded panels in two staggered columns. Bounds6..42, column gap10 and row gaps9; shared radius2. Smaller panels remain at least8 tall.\nReference: Lucide panels-top-left: coherent rounded panels; source staggered four-panel grid retained.\nKeyshape fitted to exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '35ff6a6c-3fb9-4b8c-9c89-fd5143616274'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_25/layout dashboard_35ff6a6c-3fb9-4b8c-9c89-fd5143616274.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'four-panel-dashboard'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('four', 'panel', 'dashboard')

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

        for j,(l,t,r,b) in enumerate(((6,6,19,25),(29,6,42,16),(6,34,19,42),(29,25,42,42))):box(f'panel-{j}',l,t,r,b,2)
