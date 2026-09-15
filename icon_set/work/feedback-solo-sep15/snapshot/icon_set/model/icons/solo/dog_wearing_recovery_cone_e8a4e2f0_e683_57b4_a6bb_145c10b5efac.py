"""Dog Wearing Recovery Cone.

Plan: Right-facing pointed-ear dog behind a broad funnel collar; two legs descend from its lower edge. Collar is physical equipment.
Centerline extremes: (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e8a4e2f0-e683-57b4-a6bb-145c10b5efac'
SOURCE_PATH = 'pictographic-primitives/pets/pet cone_e8a4e2f0-e683-57b4-a6bb-145c10b5efac.svg'
AUTHOR = 'gpt-6'

class DogWearingRecoveryCone(Solo48):
    icon_id = 'dog-wearing-recovery-cone'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/pets"
    aliases = ()
    keywords = ('dog', 'cone', 'recovery', 'e-collar', 'vet', 'injury', 'pet')

    def build(self):
        # Plan: Trace the rounded muzzle and ear above the recovery cone; preserve one straight shared cone rim and open the full head counter.

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
        poly('cone',(6,28),(14,24),(34,14),(42,10),(36,32),(18,40),closed=True)
        path('head',(14,24), [('L',(14,14)),('C',(22,10),(14,12),(18,10)),('L',(22,6)),('C',(34,14),(28,6),(32,10))]);join('head','cone')
        line('leg-left',(18,40),(18,42));line('leg-right',(36,32),(42,42));join('leg-left','cone');join('leg-right','cone')
