"""chocolate-bar: next hundred AI review; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b591714c-777b-49a0-ad5a-afc8f96f98b0'
SOURCE_PATH = 'icons-json/food/chocolate bar_b591714c-777b-49a0-ad5a-afc8f96f98b0.json'
AUTHOR = 'gpt-6'

class ChocolateBar(Solo48):
    icon_id = 'chocolate-bar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('chocolate', 'bar', 'food', 'solo-ai-next100')

    def build(self):
        # Plan: Keep the exposed chocolate grid and folded wrapper; broad divisions preserve the food silhouette without tiny squares.
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
        poly('bar',(12,22),(12,4),(36,4),(36,22));poly('grid',(12,13),(24,13),(36,13));line('divide',(24,4),(24,22));join('grid','bar');join('divide','grid');join('divide','bar')
        path('wrapper',(8,22),[('L',(16,22)),('L',(24,28)),('L',(40,22)),('L',(40,40)),('A',(36,44),4,4,True),('L',(12,44)),('A',(8,40),4,4,True),('L',(8,22))],True);join('wrapper','bar')
