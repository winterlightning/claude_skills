"""anklet: AI stroke review; parent retained for comparison."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '83499877-9f6d-4f70-975d-59ade9b78b2f'
SOURCE_PATH = 'icons-json/_uncategorized_03/anklet_83499877-9f6d-4f70-975d-59ade9b78b2f.json'
AUTHOR = 'gpt-6'

class Anklet(Solo48):
    icon_id = 'anklet'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized_03'
    aliases = ()
    keywords = ('anklet', '_uncategorized_03', 'solo-ai-first50')

    def build(self):
        # Plan: An open circular band and detached circular charm share the vertical axis. The charm has a clear four-unit ink gap instead of touching the band.
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
        path('band',(8,6), [('C',(6,16),(6,8),(6,12)),('C',(24,28),(6,24),(14,28)),('C',(42,16),(34,28),(42,24)),('C',(40,6),(42,12),(42,8))])
        circle('charm',24,39,3)

