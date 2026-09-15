"""paintbrush-symbol: Smooth broad paintbrush; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '34da4047-8adb-44d7-8fac-ef87b6b6b4ee'
SOURCE_PATH = 'icons-json/symbol/paintbrush_34da4047-8adb-44d7-8fac-ef87b6b6b4ee.json'
AUTHOR = 'gpt-6'

class PaintbrushSymbol(Solo48):
    icon_id = 'paintbrush-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('solo-ai-full-set', 'paintbrush-symbol')

    def build(self):
        # Plan: Preserve diagonal handle and tapered soft bristles; broaden the grip and use one exact bottom curve extreme.
        # Reference: Lucide paintbrush: original and atomic-debug geometry.

        # Typed path helpers preserve each continuous stroke and its round joins.
        def path(name, start, commands, closed=False):
            members = []
            here = start
            for index, command in enumerate(commands):
                ident = f"{name}-{index}"
                kind, end, *args = command
                if kind == "L" and tuple(end) == tuple(here):
                    continue
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
        path('handle',(17,24),[('L',(34,6)),('C',(42,12),(39,6),(42,7)),('L',(27,33)),('L',(17,24))],True)
        path('bristle',(17,24),[('C',(11,32),(12,24),(11,28)),('C',(6,42),(11,37),(9,40)),('L',(12,42)),('C',(27,33),(21,42),(27,39))]);join('bristle','handle')
