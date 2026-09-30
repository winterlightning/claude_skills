"""Telescope Monitoring a Signal.

Plan: horizontal telescope barrel, projecting rim and narrow eyepiece; waveform excluded.
Lucide telescope informs stepped barrel and distinct rim; source horizontal pose retained.
HRECT_M extremes4,10,44,38. Broad rim replaces a tight doubled outline.
Reference: pictographic-primitives/science/distro for opentelemetry preview_da27d8c0-78b0-4a2c-a763-9f3f95ddde79.svg
Authored directly on SOLO48; no source geometry was scaled or traced.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'da27d8c0-78b0-4a2c-a763-9f3f95ddde79'
SOURCE_PATH = 'pictographic-primitives/science/distro for opentelemetry preview_da27d8c0-78b0-4a2c-a763-9f3f95ddde79.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'horizontal-telescope-component'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'science'
    categories = ('science', 'primitives')
    aliases = ()
    keywords = ('horizontal', 'telescope', 'component')

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

        path('barrel',(4,18),[('L',(15,18)),('A',(23,10),8,8,True),('L',(44,10)),
            ('L',(44,38)),('L',(23,38)),('A',(15,30),8,8,True),('L',(4,30)),('L',(4,18))],True)
        self.add_line('rim',(35,10),(35,38))
        self.relate('connect','barrel','rim')
