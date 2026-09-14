"""antique-axe: AI stroke review; parent retained for comparison."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '934292aa-0c19-5266-ac04-c173d576425d'
SOURCE_PATH = 'icons-json/war/antique axe_934292aa-0c19-5266-ac04-c173d576425d.json'
AUTHOR = 'gpt-6'

class AntiqueAxeVariant2(Solo48):
    icon_id = 'antique-axe-v2'
    variant_of = 'antique-axe'
    variant_label = 'AI stroke review · first 50'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'war'
    aliases = ()
    keywords = ('antique', 'axe', 'war', 'solo-ai-first50')

    def build(self):
        # Plan: One diagonal handle joins a geometric axe head; the blade is a smooth broad arc. Preserved its intentional diagonal orientation.
        # Reference: Lucide original/axe.svg and atomic-debug/axe.svg.

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
        line('handle',(6,42),(28,20))
        path('head',(24,16), [('L',(32,6)),('C',(42,16),(32,12),(37,16)),('C',(32,28),(41,22),(37,27)),('L',(28,20)),('L',(24,16))],True)
        join('handle','head')

