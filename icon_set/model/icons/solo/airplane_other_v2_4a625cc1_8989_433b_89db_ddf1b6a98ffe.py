"""airplane-other: AI stroke review; parent retained for comparison."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4a625cc1-8989-433b-89db-ddf1b6a98ffe'
SOURCE_PATH = 'icons-json/other/airplane_4a625cc1-8989-433b-89db-ddf1b6a98ffe.json'
AUTHOR = 'gpt-6'

class AirplaneOtherVariant2(Solo48):
    icon_id = 'airplane-other-v2'
    variant_of = 'airplane-other'
    variant_label = 'AI stroke review · first 50'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'other'
    aliases = ()
    keywords = ('airplane', 'other', 'solo-ai-first50')

    def build(self):
        # Plan: A diagonal airplane keeps purposeful wing and tail corners; the nose is a single tangent curve whose right extreme is exactly x=42.
        # Reference: Lucide original/plane.svg and atomic-debug/plane.svg.

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
        path('plane',(6,31), [('L',(12,28)),('L',(18,30)),('L',(26,22)),('L',(14,10)),('L',(20,6)),('L',(32,14)),('L',(36,10)),('C',(42,14),(40,6),(42,8)),('C',(38,22),(42,18),(40,20)),('L',(18,42)),('L',(12,42)),('L',(6,31))],True)

