"""Smiling Face with Sparkle.

Plan: round face, closed eyes and broad open smile; sparkle excluded.
CIRCLE radius20. Shared eye radius3. Mouth is one closed elliptical contour.
No useful local Lucide smile match; preserve source expression with clear spacing.
Reference: pictographic-primitives/smileys/shine_ed5be819-6d23-50c8-b0be-1f119dc7acb2.svg
Authored directly on SOLO48; no source geometry was scaled or traced.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ed5be819-6d23-50c8-b0be-1f119dc7acb2'
SOURCE_PATH = 'pictographic-primitives/smileys/shine_ed5be819-6d23-50c8-b0be-1f119dc7acb2.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'broad-smiling-face-component'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/smileys'
    aliases = ()
    keywords = ('broad', 'smiling', 'face', 'component')

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

        circle('face',24,24,20)
        for j,x in enumerate((17,31)):
            self.add_arc(f'eye-{j}',(x-3,19),(x+3,19),radius_x=3,radius_y=2,sweep=True)
        path('mouth',(16,28),[('L',(32,28)),('A',(16,28),8,7,True)],True)
