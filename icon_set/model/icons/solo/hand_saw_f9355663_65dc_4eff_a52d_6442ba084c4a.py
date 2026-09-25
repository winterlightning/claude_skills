"""Diagonal hand saw with a toothed blade and notched handle. No useful local Lucide saw match; a coherent outline retains two large teeth, blade divider and grip notch.

SOLO48 SQUARE; live visible envelope (4, 4, 44, 44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f9355663-65dc-4eff-a52d-6442ba084c4a'
SOURCE_PATH = 'pictographic-primitives/symbol/saw_f9355663-65dc-4eff-a52d-6442ba084c4a.svg'
AUTHOR = 'gpt-6'


class HandSaw(Solo48):
    icon_id = 'hand-saw'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    aliases = ()
    keywords = ('saw', 'handsaw', 'tool', 'carpentry', 'woodwork', 'cut', 'diy', 'construction')

    def build(self):
        # Plan: A broad rounded handle surrounds one clear opening. Reduce the blade to three strong teeth with clean shared roots, preserving its diagonal direction.

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
        path('outline',(6,12), [('L',(14,6)),('L',(30,22)),('L',(40,32)),('A',(40,38),2,3,True),('L',(36,42)),('L',(20,32)),('L',(16,28)),('L',(16,22)),('L',(10,22)),('L',(10,16)),('L',(6,16)),('L',(6,12))],True)
        poly('divider',(30,22),(24,28),(20,32));join('outline','divider')
