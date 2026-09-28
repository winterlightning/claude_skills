from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '958637b4-0216-5d2f-a6a7-e9708b032af8'
SOURCE_PATH = 'pictographic-primitives/shipping/logistic damaged package_958637b4-0216-5d2f-a6a7-e9708b032af8.svg'
AUTHOR = 'gpt-6'


class DamagedShippingBox(Solo48):
    icon_id = 'damaged-shipping-box'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "shipping"
    categories = ("primitives", "shipping")
    aliases = ()
    keywords = ('box', 'parcel', 'damage', 'tear', 'shipping', 'package')

    def build(self):
        # Plan: Lucide box: preserve shared perspective corners; represent the torn seam with a broad visible break instead of squeezing a zigzag against the bottom edge.

        # Each path owns a coherent stroke; control points preserve smooth tangents.
        def path(n, start, commands, closed=False):
            here = start
            members = []
            for j, c in enumerate(commands):
                k, end, *args = c
                name = f'{n}-{j}'
                if k == 'L': self.add_line(name, here, end)
                elif k == 'A': self.add_arc(name, here, end, radius_x=args[0], radius_y=args[1], sweep=args[2])
                elif k == 'C': self.add_bezier(name, here, (args[0], args[1], end))
                here = end
                members.append(name)
            self.add_contour(n, *members, closed=closed)
        def circle(n, x, y, r):
            path(n, (x-r,y), [('A',(x+r,y),r,r,True), ('A',(x-r,y),r,r,True)], True)
        def box(n, l, t, r, b, rad=4):
            path(n,(l+rad,t), [('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        line = self.add_line
        poly = self.add_polyline
        join = lambda a,b: self.relate('connect',a,b)
        poly('outline',(24,6),(42,15),(42,33),(24,42),(6,33),(6,15),closed=True)
        poly('lid',(6,15),(24,24),(42,15));join('outline','lid')
        poly('tear-top',(24,24),(24,28),(28,30));join('tear-top','lid')
        line('tear-bottom',(24,38),(24,42));join('tear-bottom','outline')
