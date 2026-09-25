"""Poodle Head.

Plan: Cloud-like topknot, long rounded pompom ears and narrow squared face. Mirrored lobes share radii.
Centerline extremes: (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e314897f-f4bf-493a-bfcc-5a3f735b207b'
SOURCE_PATH = 'pictographic-primitives/pets/poodle_e314897f-f4bf-493a-bfcc-5a3f735b207b.svg'
AUTHOR = 'gpt-6'

class PoodleHead(Solo48):
    icon_id = 'poodle-head'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "pets"
    aliases = ()
    keywords = ('dog', 'poodle', 'head', 'breed', 'topknot', 'groomed', 'pet')

    def build(self):
        # Plan: Trace the original poodle haircut: three broad crown puffs above a long face and paired ears. Shared roots preserve the silhouette and open facial counter.

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
        path('hair',(15,20), [('C',(6,18),(10,24),(6,23)),('C',(16,12),(6,12),(10,10)),('C',(24,6),(16,8),(20,6)),('C',(32,12),(28,6),(32,8)),('C',(42,18),(38,10),(42,12)),('C',(33,20),(42,23),(38,24)),('C',(24,22),(30,24),(28,24)),('C',(15,20),(20,24),(18,24))],True)
        path('face',(15,20), [('L',(15,33)),('A',(33,33),9,9,False),('L',(33,20))]);join('face','hair')
        path('left-ear',(6,18), [('L',(6,36)),('C',(15,36),(6,44),(15,44)),('L',(15,33))]);join('left-ear','hair');join('left-ear','face')
        path('right-ear',(42,18), [('L',(42,36)),('C',(33,36),(42,44),(33,44)),('L',(33,33))]);join('right-ear','hair');join('right-ear','face')
        self.add_dot('nose',(24,32))
