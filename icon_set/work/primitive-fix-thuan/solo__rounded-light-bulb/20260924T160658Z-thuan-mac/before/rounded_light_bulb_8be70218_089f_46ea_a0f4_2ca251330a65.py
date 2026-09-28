'Simple Electric Light Bulb.\nPlan: Broad glass bulb narrowing into rounded base. Envelope10,4..38,44. Shared base seam, no filament.\nReference: Lucide lightbulb: one rounded glass contour and attached base.\nKeyshape: VRECT_M, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8be70218-089f-46ea-a0f4-2ca251330a65'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_25/lightbulb_8be70218-089f-46ea-a0f4-2ca251330a65.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'rounded-light-bulb'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('rounded', 'light', 'bulb')

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

        path('bulb',(10,18),[((38,18),14,14,True),((32,32),6,14,True),(32,34),(32,40),((28,44),4,4,True),(20,44),((16,40),4,4,True),(16,34),(16,32),((10,18),6,14,True)],True)
        self.add_line('base-seam',(16,34),(32,34));self.relate('connect','base-seam','bulb')
