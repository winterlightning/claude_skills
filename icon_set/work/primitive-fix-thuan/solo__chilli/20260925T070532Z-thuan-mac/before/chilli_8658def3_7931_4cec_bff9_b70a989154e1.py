"""chilli: next hundred AI review; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8658def3-7931-4cec-bff9-b70a989154e1'
SOURCE_PATH = 'pictographic-primitives/symbol/chilli_8658def3-7931-4cec-bff9-b70a989154e1.svg'
AUTHOR = 'gpt-6'

class Chilli(Solo48):
    icon_id = 'chilli'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('chilli', 'symbol', 'solo-ai-next100')

    def build(self):
        # Plan: A curved pepper retains a pointed tip, broad body and a short curved stem; the belly fullness differentiates the two peppers.
        # Reference: No useful exact Lucide match; supplied original silhouette.

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
        path('pepper',(4,24),[('C',(32,18),(16,27),(24,22)),('C',(40,20),(36,14),(40,16)),('C',(22,40),(44,28),(34,40)),('C',(4,24),(12,40),(7,31))],True)
        path('stem',(40,20),[('C',(44,12),(43,18),(44,15)),('C',(40,8),(44,9),(43,8))]);join('stem','pepper')
