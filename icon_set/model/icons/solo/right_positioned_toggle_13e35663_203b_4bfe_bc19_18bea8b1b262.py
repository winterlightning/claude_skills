'Toggle Switch On.\nPlan: Horizontal capsule box4,10..44,38, end radius14; right knob radius5 at30,24.\nReference: Lucide toggle-right: capsule and offset round knob with clear enclosing gap.\nKeyshape: HRECT_M; constructed to exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '13e35663-203b-4bfe-bc19-18bea8b1b262'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_38/toggle large off_13e35663-203b-4bfe-bc19-18bea8b1b262.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'right-positioned-toggle'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('right', 'positioned', 'toggle')

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

        path('track',(18,10),[(30,10),((30,38),14,14,True),(18,38),((18,10),14,14,True)],True)
        circle('knob',30,24,5)
