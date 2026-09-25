"""Billiards Eight Ball.

Plan: concentric ball and blank number label. Digit8 is reused through the typeface layout.
CIRCLE center24,24 radii20 and10 leaves6 visible clearance.
No useful Lucide exact match; two clean circular loops retain source construction.
Reference: pictographic-primitives/sports/pool black ball_da44a824-a8a5-4c75-8b61-855bba1f9a37.svg
Authored directly on SOLO48; no source geometry was scaled or traced.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'da44a824-a8a5-4c75-8b61-855bba1f9a37'
SOURCE_PATH = 'pictographic-primitives/sports/pool black ball_da44a824-a8a5-4c75-8b61-855bba1f9a37.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'billiard-ball-blank-label-component'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'sports'
    aliases = ()
    keywords = ('billiard', 'ball', 'blank', 'label', 'component')

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

        circle('ball',24,24,20)
        circle('label',24,24,10)
