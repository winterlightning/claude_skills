from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c5352ba7-8705-433f-bfb4-5f356398c838'
SOURCE_PATH = 'pictographic-primitives/animals/spider hang_c5352ba7-8705-433f-bfb4-5f356398c838.svg'
AUTHOR = 'gpt-6'


class HangingSpider(Solo48):
    icon_id = 'hanging-spider'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('spider', 'thread', 'hanging', 'web', 'arachnid', 'legs', 'halloween', 'drop')

    def build(self):
        # Plan: One capsule body owns four equally spaced leg roots per side and a hanging thread; mirrored legs diverge to preserve clearance.

        # Each path owns a coherent stroke; control points preserve smooth tangents.
        def path(n, start, commands, closed=False):
            here = start
            members = []
            for j, c in enumerate(commands):
                k, end, *args = c
                name = f'{n}-{j}'
                if k == 'L': self.add_line(name, here, end)
                elif k == 'A': self.add_arc(name, here, end, radius_x=args[0], radius_y=args[1], sweep=args[2])
                elif k == 'C': self.add_bezier(name, here, (args[0], args[1], end))
                here = end
                members.append(name)
            self.add_contour(n, *members, closed=closed)
        def circle(n, x, y, r):
            path(n, (x-r,y), [('A',(x+r,y),r,r,True), ('A',(x-r,y),r,r,True)], True)
        def box(n, l, t, r, b, rad=4):
            path(n,(l+rad,t), [('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        line = self.add_line
        poly = self.add_polyline
        join = lambda a,b: self.relate('connect',a,b)
        path('body',(18,14), [('A',(24,8),6,6,True),('A',(30,14),6,6,True),('L',(30,22)),('L',(30,30)),('L',(30,38)),('A',(24,44),6,6,True),('A',(18,38),6,6,True),('L',(18,30)),('L',(18,22)),('L',(18,14))],True)
        line('thread',(24,4),(24,8));join('thread','body')
        for side in (-1,1):
         x=24+side*6;outer=24+side*16
         poly(f'upper-{side}',(x,14),(outer,10),(outer,6));join(f'upper-{side}','body')
         line(f'middle-{side}',(x,22),(outer,20));join(f'middle-{side}','body')
         line(f'lower-{side}',(x,30),(outer,32));join(f'lower-{side}','body')
         line(f'bottom-{side}',(x,38),(24+side*10,44));join(f'bottom-{side}','body')
