"""Running person escaping.

Plan: runner with circular head and bent limbs, three detached motion trails on right.
Human full_body_ref.png owns anatomy. Head(22,10),r4; upper torso junction(22,22):
8 centerline /4 ink gap, vertical tangent aligns head and upper torso.
SQUARE extremes6,6,42,42. Four source trails reduced to three for clearance.
Reference: pictographic-primitives/wayfinding/safety fire exit 1_fa846b07-6bb3-4c07-8266-8826d3da97b9.svg
Authored directly on SOLO48; no source geometry was scaled or traced.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fa846b07-6bb3-4c07-8266-8826d3da97b9'
SOURCE_PATH = 'pictographic-primitives/wayfinding/safety fire exit 1_fa846b07-6bb3-4c07-8266-8826d3da97b9.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'running-person-with-motion-trails'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'wayfinding'
    aliases = ()
    keywords = ('running', 'person', 'with', 'motion', 'trails')

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

        circle('head',22,10,4)
        self.add_bezier('torso',(22,22),((22,25),(20,28),(18,31)))
        self.add_polyline('arms',(6,28),(14,22),(22,22),(28,27))
        self.add_polyline('legs',(8,42),(12,36),(18,31),(25,39),(28,39))
        self.relate('connect','torso','arms')
        self.relate('connect','torso','legs')
        for j,y in enumerate((14,26,38)):
            self.add_arc(f'trail-{j}',(38,y),(42,y+2),radius_x=5,radius_y=5,sweep=False)
        self.mark_human_figure('runner',head='head',torso='torso',torso_junction='start')
