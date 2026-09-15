"""Restaurant fork knife (food), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '24a6b06c-3fec-43a0-aca0-b205c99c496b'
SOURCE_PATH = 'pictographic-primitives/food/restaurant fork knife_24a6b06c-3fec-43a0-aca0-b205c99c496b.svg'
AUTHOR = 'gpt-6'

class RestaurantForkKnife(Solo48):
    icon_id = 'restaurant-fork-knife'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('restaurant', 'fork', 'knife', 'food')

    def build(self):
        # Plan: Lucide-style table cutlery: equally spaced fork tines and a coherent rounded butter-knife blade; remove the pinched blade taper.

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
        path('fork',(8,4), [('L',(8,16)),('A',(16,24),8,8,False),('A',(24,16),8,8,False),('L',(24,4))])
        line('middle',(16,4),(16,24));line('fork-handle',(16,24),(16,44))
        join('fork','middle');join('fork','fork-handle');join('middle','fork-handle')
        path('blade',(32,8), [('A',(40,8),4,4,True),('L',(40,28)),('L',(32,28)),('L',(32,8))],True)
        line('knife-handle',(32,28),(32,44));join('blade','knife-handle')
