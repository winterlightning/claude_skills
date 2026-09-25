"""Hexagonal Network Migration Arrow.

Plan: five radius3 nodes around open-topped hexagonal network; arrow and chevrons excluded.
SQUARE extremes6,6,42,42. Nodes own connection cardinal points; every spoke split at those points.
No useful Lucide exact match; regular node sizes and shared endpoints preserve construction.
Reference: pictographic-primitives/programing/migration hub_293c7663-04e3-4a88-9038-3812935570a5.svg
Authored directly on SOLO48; no source geometry was scaled or traced.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '293c7663-04e3-4a88-9038-3812935570a5'
SOURCE_PATH = 'pictographic-primitives/programing/migration hub_293c7663-04e3-4a88-9038-3812935570a5.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'hexagonal-node-network-component'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'programing'
    aliases = ()
    keywords = ('hexagonal', 'node', 'network', 'component')

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

        for name,x,y in [('ul',9,9),('ur',39,9),('ll',9,29),('lr',39,29),('bottom',24,39)]:
            circle(name,x,y,3)
        self.add_line('left',(9,12),(9,26))
        self.add_line('right',(39,12),(39,26))
        self.add_line('lower-left',(12,29),(21,39))
        self.add_line('lower-right',(36,29),(27,39))
        for line,a,b in [('left','ul','ll'),('right','ur','lr'),('lower-left','ll','bottom'),('lower-right','lr','bottom')]:
            self.relate('connect',line,a)
            self.relate('connect',line,b)
