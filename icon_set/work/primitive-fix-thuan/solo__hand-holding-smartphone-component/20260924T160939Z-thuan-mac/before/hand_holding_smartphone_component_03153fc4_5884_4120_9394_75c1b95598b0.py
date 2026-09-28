"""Hand Squeezing Smartphone Sides.

Plan: upright phone held by a continuous cupped hand, excluding squeeze arrows.
Lucide hand: coherent palm curve and bent thumb. VRECT_L extremes8,4,40,44.
Curled finger stack reduced to one grip division, retaining the cupping palm and thumb.
Reference: pictographic-primitives/phones/squeeze sides 1_03153fc4-5884-4120-9394-75c1b95598b0.svg
Authored directly on SOLO48; no source geometry was scaled or traced.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '03153fc4-5884-4120-9394-75c1b95598b0'
SOURCE_PATH = 'pictographic-primitives/phones/squeeze sides 1_03153fc4-5884-4120-9394-75c1b95598b0.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'hand-holding-smartphone-component'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/phones'
    aliases = ()
    keywords = ('hand', 'holding', 'smartphone', 'component')

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

        box('phone',8,4,30,36)
        path('hand',(16,44),[('L',(30,44)),('A',(40,34),10,10,False),('L',(40,22)),
            ('L',(30,22))])
        self.relate('connect','phone','hand')
        self.add_line('grip',(8,25),(16,25))
        self.relate('connect','phone','grip')
