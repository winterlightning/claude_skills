"""A broad open-jaw wrench with diagonal rounded-end handle; adjustment screw omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '47ad292e-443e-5fb5-a71a-0d263bd6ed9e'
SOURCE_PATH = 'pictographic-primitives/tools/tools crescent wrench_47ad292e-443e-5fb5-a71a-0d263bd6ed9e.svg'
AUTHOR = 'gpt-6'

class CrescentHeadWrench(Solo48):
    icon_id = 'crescent-head-wrench'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "tools"
    aliases = ()
    keywords = ('wrench', 'crescent wrench', 'spanner', 'adjustable', 'repair', 'mechanic', 'hardware', 'tool')

    def build(self):
        # Plan: Broaden the diagonal shaft at its owning neck; retain crescent jaws and the rounded handle end.

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
        path('outline',(22,6), [('A',(38,22),16,16,True),('L',(36,30)),('L',(42,36)),('A',(36,42),6,6,True),('L',(30,36)),('L',(22,38)),('A',(6,22),16,16,True),('L',(6,14)),('L',(14,22)),('L',(22,14)),('L',(14,6)),('L',(22,6))],True)
