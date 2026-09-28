"""Stressed Person Icon.

Plan: round head, broad smooth shoulders, three zigzag stress marks.
Human user.svg informs shoulders. Avatar head bottom32 /body top36: zero ink gap.
VRECT_L extremes8,4,40,44. No facial detail needed for this generic stressed person.
Reference: pictographic-primitives/work/user man stress_e097b5d9-237a-5a21-8e1e-3426dec249b1.svg
Authored directly on SOLO48; no source geometry was scaled or traced.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e097b5d9-237a-5a21-8e1e-3426dec249b1'
SOURCE_PATH = 'pictographic-primitives/work/user man stress_e097b5d9-237a-5a21-8e1e-3426dec249b1.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'stressed-person'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'work'
    categories = ('work', 'primitives')
    aliases = ()
    keywords = ('stressed', 'person')

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

        self.add_arc('head-top',(18,26),(30,26),radius_x=6,sweep=True)
        self.add_arc('head-bottom',(30,26),(18,26),radius_x=6,sweep=True)
        self.add_contour('head','head-top','head-bottom',closed=True)
        self.add_arc('body-top',(8,44),(40,44),radius_x=16,radius_y=8,sweep=True)
        self.add_contour('body','body-top')
        self.relate('connect','head','body')
        for j,x in enumerate((10,24,38)):
            self.add_polyline(f'stress-{j}',(x-2,4),(x+2,8),(x-2,12))
