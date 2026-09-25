"""Cat Head with Heart.

Plan: symmetric cat face with ear corners and one intrinsic T nose; excludes heart and thought dot.
Lucide cat informs the ear/cheek silhouette. SQUARE extremes6,6,42,42.
No eye detail in source; preserve its quiet face.
Reference: pictographic-primitives/pets/cat breeding_340243a4-2ac7-4e3b-ad02-cba7341dd731.svg
Authored directly on SOLO48; no source geometry was scaled or traced.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '340243a4-2ac7-4e3b-ad02-cba7341dd731'
SOURCE_PATH = 'pictographic-primitives/pets/cat breeding_340243a4-2ac7-4e3b-ad02-cba7341dd731.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'cat-head-affection-component'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'pets'
    aliases = ()
    keywords = ('cat', 'head', 'affection', 'component')

    def build(self):

        def path(name, start, commands, closed=False):
            point, members = start, []
            for index, command in enumerate(commands):
                kind, end, *args = command
                member = f'{name}-{index}'
                if kind == 'L':
                    self.add_line(member, point, end)
                elif kind == 'A':
                    self.add_arc(member, point, end, radius_x=args[0], radius_y=args[1], sweep=args[2])
                else:
                    self.add_bezier(member, point, (args[0], args[1], end))
                point = end
                members.append(member)
            self.add_contour(name, *members, closed=closed)
        def circle(name, x, y, radius):
            path(name, (x-radius,y), [('A',(x+radius,y),radius,radius,True),
                 ('A',(x-radius,y),radius,radius,True)], True)
        def box(name, l, t, r, b, radius=4):
            path(name,(l+radius,t),[('L',(r-radius,t)),('A',(r,t+radius),radius,radius,True),
                ('L',(r,b-radius)),('A',(r-radius,b),radius,radius,True),('L',(l+radius,b)),
                ('A',(l,b-radius),radius,radius,True),('L',(l,t+radius)),
                ('A',(l+radius,t),radius,radius,True)],True)

        path('head',(6,6),[('L',(17,14)),('A',(31,14),14,14,True),('L',(42,6)),
            ('L',(42,25)),('A',(25,42),17,17,True),('L',(23,42)),
            ('A',(6,25),17,17,True),('L',(6,6))],True)
        self.add_polyline('nose',(20,27),(24,27),(28,27))
        self.add_line('mouth',(24,27),(24,33))
        self.relate('connect','nose','mouth')
