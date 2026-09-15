"""alcove: AI stroke review; parent retained for comparison."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5c5e171c-ba31-4513-a36c-dbb30aad9abc'
SOURCE_PATH = 'icons-json/_uncategorized_01/alcove_5c5e171c-ba31-4513-a36c-dbb30aad9abc.json'
AUTHOR = 'gpt-6'

class Alcove(Solo48):
    icon_id = 'alcove'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized_01'
    aliases = ()
    keywords = ('alcove', '_uncategorized_01', 'solo-ai-first50')

    def build(self):
        # Plan: Two concentric semicircular arches share an axis; the inner doorway meets the broad threshold with exact endpoints. Removed uneven arch radii.
        # Reference: No useful exact Lucide match; geometric construction from the supplied subject.

        # Typed path helpers preserve each continuous stroke and its round joins.
        def path(name, start, commands, closed=False):
            members = []
            here = start
            for index, command in enumerate(commands):
                ident = f"{name}-{index}"
                kind, end, *args = command
                if kind == "L":
                    self.add_line(ident, here, end)
                elif kind == "A":
                    rx, ry, sweep = args
                    self.add_arc(ident, here, end, radius_x=rx, radius_y=ry, sweep=sweep)
                elif kind == "C":
                    c1, c2 = args
                    self.add_bezier(ident, here, (c1, c2, end))
                members.append(ident)
                here = end
            self.add_contour(name, *members, closed=closed)
        def circle(name, cx, cy, r):
            path(name, (cx-r,cy), [("A",(cx+r,cy),r,r,True), ("A",(cx-r,cy),r,r,True)], True)
        def rounded(name, x0, y0, x1, y1, r):
            path(name, (x0+r,y0), [
                ("L",(x1-r,y0)), ("A",(x1,y0+r),r,r,True),
                ("L",(x1,y1-r)), ("A",(x1-r,y1),r,r,True),
                ("L",(x0+r,y1)), ("A",(x0,y1-r),r,r,True),
                ("L",(x0,y0+r)), ("A",(x0+r,y0),r,r,True)], True)
        line = self.add_line
        poly = self.add_polyline
        join = lambda a,b: self.relate("connect",a,b)
        path('outer',(8,44), [('L',(8,20)),('A',(40,20),16,16,True),('L',(40,44)),('L',(8,44))],True)
        path('inner',(16,36), [('L',(16,20)),('A',(32,20),8,8,True),('L',(32,36)),('L',(16,36))],True)
        line('threshold-left',(8,44),(16,36));line('threshold-right',(40,44),(32,36))
        for n in ('threshold-left','threshold-right'):
         join(n,'inner');join(n,'outer')

