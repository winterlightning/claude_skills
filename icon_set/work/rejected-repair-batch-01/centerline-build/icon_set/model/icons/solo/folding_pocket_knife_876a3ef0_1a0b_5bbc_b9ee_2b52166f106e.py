"""A folding knife with a horizontal rounded handle and raised pointed blade; small pivot dot omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '876a3ef0-1a0b-5bbc-b9ee-2b52166f106e'
SOURCE_PATH = 'pictographic-primitives/tools/folding pocket knife_876a3ef0-1a0b-5bbc-b9ee-2b52166f106e.svg'
AUTHOR = 'gpt-6'

class FoldingPocketKnife(Solo48):
    icon_id = 'folding-pocket-knife'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/tools"
    aliases = ()
    keywords = ('pocket knife', 'knife', 'folding', 'blade', 'penknife', 'camping', 'outdoor', 'tool')

    def build(self):
        # Plan: A single smooth cutting edge bows away from the blade back; both blade roots share the rounded handle rim.

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
        path('handle',(12,30), [('L',(24,30)),('L',(36,30)),('A',(42,36),6,6,True),('A',(36,42),6,6,True),('L',(12,42)),('A',(6,36),6,6,True),('A',(12,30),6,6,True)],True)
        path('blade',(36,30), [('L',(12,6)),('C',(24,30),(12,18),(12,22))]);join('blade','handle')
