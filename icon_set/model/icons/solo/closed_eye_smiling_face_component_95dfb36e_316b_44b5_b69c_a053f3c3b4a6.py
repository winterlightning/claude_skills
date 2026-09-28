"""Smiling Face with Hearts.

Plan: circular face, two mirrored closed eyes and gentle smile. Hearts excluded.
CIRCLE radius20 at24,24. Shared eye radius3. No useful local Lucide smile match.
Reference: pictographic-primitives/smileys/in love heart face_95dfb36e-316b-44b5-b69c-a053f3c3b4a6.svg
Authored directly on SOLO48; no source geometry was scaled or traced.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '95dfb36e-316b-44b5-b69c-a053f3c3b4a6'
SOURCE_PATH = 'pictographic-primitives/smileys/in love heart face_95dfb36e-316b-44b5-b69c-a053f3c3b4a6.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'closed-eye-smiling-face-component'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    categories = ('smileys', 'primitives')
    aliases = ()
    keywords = ('closed', 'eye', 'smiling', 'face', 'component')

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
        for j,x in enumerate((16,32)):
            self.add_arc(f'eye-{j}',(x-3,21),(x+3,21),radius_x=3,radius_y=2,sweep=True)
        self.add_arc('smile',(17,30),(31,30),radius_x=7,radius_y=4,sweep=False)
