'Pocket Wallet with Button Strap.\nPlan: Rounded wallet with broad right button tab; lower body contour stops short of tab to preserve a clear opening. Layered lip omitted. Bounds4,8..44,40.\nReference: Lucide wallet: rounded main body and attached overlapping button tab.\nKeyshape: HRECT_L, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '311f16ae-477a-42b9-8cd8-2a52430b8df1'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_17/ewallet_311f16ae-477a-42b9-8cd8-2a52430b8df1.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'wallet-with-button-tab'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('wallet', 'with', 'button', 'tab')

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

        path('wallet',(40,18),[(40,12),((36,8),4,4,False),(8,8),((4,12),4,4,False),(4,36),((8,40),4,4,False),(18,40)])
        path('tab',(30,18),[(40,18),(44,18),(44,36),(40,36),(30,36),((30,18),9,9,True)],True);self.relate('connect','tab','wallet')
        self.add_dot('button',(34,27))
