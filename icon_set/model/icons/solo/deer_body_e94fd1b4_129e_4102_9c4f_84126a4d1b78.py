"""A standing stag with an upright head and forked antlers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e94fd1b4-129e-4102-9c4f-84126a4d1b78'
SOURCE_PATH = 'pictographic-primitives/animals/deer body_e94fd1b4-129e-4102-9c4f-84126a4d1b78.svg'
AUTHOR = 'gpt-6'


class StandingStag(Solo48):
    icon_id = 'standing-stag'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('deer', 'stag', 'antlers', 'standing', 'buck', 'wildlife', 'forest', 'animal')

    def build(self):
        # Plan: Trace a clear neck and muzzle with a rounded back and belly. The branching antler rises from the forehead, with its tips held away from the head.

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
        path('body',(6,42), [('L',(6,34)),('L',(6,30)),('A',(12,24),6,6,True),('L',(26,24)),('L',(30,16)),('L',(38,16)),('L',(42,22)),('L',(36,26)),('L',(36,42))])
        path('belly',(6,34), [('L',(20,34)),('A',(28,42),8,8,True)]);join('body','belly')
        line('tail',(12,24),(6,18));join('tail','body')
        poly('antler',(38,16),(34,8),(34,6));poly('tine',(26,6),(28,8),(34,8),(42,6));join('antler','tine');join('antler','body')
