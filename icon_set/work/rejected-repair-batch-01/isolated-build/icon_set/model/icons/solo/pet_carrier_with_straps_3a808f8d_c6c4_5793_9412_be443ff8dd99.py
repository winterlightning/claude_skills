"""Pet Carrier with Straps.

Plan: Body owns handle attachment and symmetric repeated straps.
Keyshape centerline extremes: (6,6)-(42,42)
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3a808f8d-c6c4-5793-9412-be443ff8dd99'
SOURCE_PATH = 'pictographic-primitives/pets/cat carrier_3a808f8d-c6c4-5793-9412-be443ff8dd99.svg'
AUTHOR = 'gpt-6'

class PetCarrierWithStraps(Solo48):
    icon_id = 'pet-carrier-with-straps'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/pets"
    aliases = ()
    keywords = ('pet-carrier', 'carrier', 'crate', 'travel', 'cat', 'basket', 'transport')

    def build(self):
        # Plan: Broad rounded carrier with parallel straps at shared rim/base stations; Lucide bag corner construction.

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
        path('body',(10,18), [('L',(16,18)),('L',(32,18)),('L',(38,18)),('A',(42,22),4,4,True),('L',(42,38)),('A',(38,42),4,4,True),('L',(32,42)),('L',(16,42)),('L',(10,42)),('A',(6,38),4,4,True),('L',(6,22)),('A',(10,18),4,4,True)],True)
        path('handle',(16,18), [('L',(16,14)),('A',(32,14),8,8,True),('L',(32,18))])
        join('handle','body')
        for x in (16,32):
         line(f'strap-{x}',(x,18),(x,42));join(f'strap-{x}','body');join(f'strap-{x}','handle')
