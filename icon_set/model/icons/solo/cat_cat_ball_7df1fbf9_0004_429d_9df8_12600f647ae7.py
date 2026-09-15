"""cat-cat-ball: next hundred AI review; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7df1fbf9-0004-429d-9df8-12600f647ae7'
SOURCE_PATH = 'icons-json/pets/cat cat ball_7df1fbf9-0004-429d-9df8-12600f647ae7.json'
AUTHOR = 'gpt-6'

class CatCatBall(Solo48):
    icon_id = 'cat-cat-ball'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'pets'
    aliases = ()
    keywords = ('cat', 'ball', 'pets', 'solo-ai-next100')

    def build(self):
        # Plan: A basketball-like cat ball has a true circular outline and mirrored panel arcs around a centered cross.
        # Reference: Lucide disc original and atomic-debug construction.

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
        path('rim',(24,4),[('A',(44,24),20,20,True),('A',(24,44),20,20,True),('A',(4,24),20,20,True),('A',(24,4),20,20,True)],True)
        poly('horizontal',(4,24),(24,24),(44,24));poly('vertical',(24,4),(24,24),(24,44));join('horizontal','rim');join('vertical','rim');join('horizontal','vertical')
        for side in (-1,1):
         x=lambda d:24+side*d
         path(f'panel-{side}',(x(14),10),[('C',(x(9),24),(x(10),14),(x(9),19)),('C',(x(14),38),(x(9),29),(x(10),34))]);join(f'panel-{side}','rim');join(f'panel-{side}','horizontal')
