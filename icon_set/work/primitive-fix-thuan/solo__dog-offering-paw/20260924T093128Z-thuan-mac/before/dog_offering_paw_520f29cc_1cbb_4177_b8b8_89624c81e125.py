"""Dog Offering Paw.

Plan: Left-facing seated dog, pointed ear, projecting muzzle, raised forepaw and upward curling tail. Lower body owns broad haunch.
Centerline extremes: (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '520f29cc-1cbb-4177-b8b8-89624c81e125'
SOURCE_PATH = 'pictographic-primitives/pets/dog giving hand paw_520f29cc-1cbb-4177-b8b8-89624c81e125.svg'
AUTHOR = 'gpt-6'

class DogOfferingPaw(Solo48):
    icon_id = 'dog-offering-paw'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/pets'
    aliases = ()
    keywords = ('dog', 'paw', 'shake', 'trick', 'training', 'sitting', 'pet')

    def build(self):
        # Plan: Trace the seated dog and raised paw with a smooth extended foreleg and rounded haunch; broaden the neck and paw counter.

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
        path('dog',(28,20), [('L',(24,6)),('L',(18,12)),('L',(10,14)),('L',(10,24)),('L',(20,24)),('L',(20,32)),('L',(12,32)),('A',(12,40),6,4,False),('L',(20,42)),('C',(38,28),(34,42),(38,34)),('L',(28,20))],True)
        path('tail',(38,28), [('A',(42,16),4,12,False)]);join('tail','dog')
