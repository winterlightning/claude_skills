"""Browser Window Bookmark.

Plan: rounded browser outline (4,8)-(44,40); header at18 and attached ribbon.
Lucide bookmark: coherent notch and paired ribbon walls. Header ornaments omitted for clearance.
Reference: pictographic-primitives/websites/app window bookmark_0300f94b-1f76-5f22-bc53-bf12f22d8680.svg
Authored directly on SOLO48; no source geometry was scaled or traced.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0300f94b-1f76-5f22-bc53-bf12f22d8680'
SOURCE_PATH = 'pictographic-primitives/websites/app window bookmark_0300f94b-1f76-5f22-bc53-bf12f22d8680.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'browser-window-bookmark'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'websites'
    categories = ('websites', 'primitives')
    aliases = ()
    keywords = ('browser', 'window', 'bookmark')

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

        box('window',4,8,44,40)
        self.add_line('header-left',(4,18),(24,18))
        self.add_line('header-middle',(24,18),(35,18))
        self.add_line('header-right',(35,18),(44,18))
        self.add_polyline('ribbon',(24,18),(24,31),(29,27),(35,31),(35,18))
        for part in ('header-left','header-middle','header-right'):
            self.relate('connect','window',part)
            self.relate('connect','ribbon',part)
