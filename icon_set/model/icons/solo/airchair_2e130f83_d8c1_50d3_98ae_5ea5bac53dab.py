"""airchair: AI stroke review; parent retained for comparison."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '2e130f83-d8c1-50d3-98ae-5ea5bac53dab'
SOURCE_PATH = 'icons-json/symbol/airchair_2e130f83-d8c1-50d3-98ae-5ea5bac53dab.json'
AUTHOR = 'gpt-6'

class Airchair(Solo48):
    icon_id = 'airchair'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('airchair', 'symbol', 'solo-ai-first50')

    def build(self):
        # Plan: A shared vertical axis controls the arched back, continuous arm-and-seat outline, and paired legs. Removed traced dents.
        # Reference: Lucide original/armchair.svg and atomic-debug/armchair.svg.

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
        path('back',(12,21), [('L',(12,16)),('A',(36,16),12,12,True),('L',(36,21))])
        poly('seat',(12,21),(8,21),(10,36),(12,36),(36,36),(38,36),(40,21),(36,21),(32,21),(32,28),(16,28),(16,21),(12,21),closed=True)
        for x in (12,36):
         line(f'leg-{x}',(x,36),(x-2 if x<24 else x+2,44));join(f'leg-{x}','seat')
        join('seat','back')

