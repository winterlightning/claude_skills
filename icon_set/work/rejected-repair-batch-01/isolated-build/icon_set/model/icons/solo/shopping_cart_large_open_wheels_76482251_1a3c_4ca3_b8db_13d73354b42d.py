"""Shopping Cart. Lucide shopping-cart contour principles. Broad rounded basket, short angled grip and relatively larger detached wheel rings; no rail in source."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '76482251-1a3c-4ca3-b8db-13d73354b42d'
SOURCE_PATH = 'pictographic-primitives/shopping/shopping cart_76482251-1a3c-4ca3-b8db-13d73354b42d.svg'
AUTHOR = 'gpt-6'

class ShoppingCartLargeOpenWheels(Solo48):
    icon_id = 'shopping-cart-large-open-wheels'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/shopping"
    aliases = ()
    keywords = ('cart', 'shopping', 'trolley', 'basket', 'wheels', 'retail', 'supermarket')

    def build(self):
        # Plan: Deepen the rounded basket uniformly, preserving two large circular wheels and a shared handle attachment.

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
        path('basket',(4,14), [('L',(36,14)),('L',(44,14)),('L',(44,20)),('A',(40,24),4,4,True),('L',(8,24)),('A',(4,20),4,4,True),('L',(4,14))],True)
        line('grip',(36,14),(42,8));join('grip','basket')
        for j,x in enumerate((14,34)): circle(f'wheel-{j}',x,36,4)
