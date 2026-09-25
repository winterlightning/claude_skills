"""High Voltage Electric Power Generator.

Plan: rounded top cap, segmented central insulator and broad lower support; bolts excluded.
VRECT_L extremes8,4,40,44. Repeated ribs use9-unit step; lower support retains slope.
No useful Lucide exact match. Omit fine grooves and use three ribs.
Reference: pictographic-primitives/science/elecricity power_87aae996-0ff2-4205-ac86-1266ba89328e.svg
Authored directly on SOLO48; no source geometry was scaled or traced.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '87aae996-0ff2-4205-ac86-1266ba89328e'
SOURCE_PATH = 'pictographic-primitives/science/elecricity power_87aae996-0ff2-4205-ac86-1266ba89328e.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'electrical-power-generator-component'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'science'
    aliases = ()
    keywords = ('electrical', 'power', 'generator', 'component')

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

        box('cap',12,4,36,12,4)
        for j,y in enumerate((21,30)):
            self.add_line(f'rib-{j}',(16,y),(32,y))
        path('support',(8,44),[('L',(13,39)),('L',(35,39)),('L',(40,44))])
