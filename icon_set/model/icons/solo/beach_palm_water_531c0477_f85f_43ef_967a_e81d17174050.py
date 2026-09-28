"""beach-palm-water: AI stroke review; parent retained for comparison."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '531c0477-f85f-43ef-967a-e81d17174050'
SOURCE_PATH = 'pictographic-primitives/recreation/beach palm water_531c0477-f85f-43ef-967a-e81d17174050.svg'
AUTHOR = 'gpt-6'

class BeachPalmWater(Solo48):
    icon_id = 'beach-palm-water'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'recreation'
    categories = ('primitives', 'recreation')
    aliases = ()
    keywords = ('beach', 'palm', 'water', 'recreation', 'solo-ai-first50')

    def build(self):
        # Plan: A deliberately tilted beach umbrella sits above a regular wave run. The canopy reaches its exact top extreme with a smooth tangent; omitted the tiny top spike.
        # Reference: Lucide original/umbrella.svg and atomic-debug/umbrella.svg.

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
        path('canopy',(10,24), [('C',(29,6),(10,13),(20,6)),('C',(38,12),(33,6),(36,8)),('L',(24,18)),('L',(10,24))],True)
        line('pole',(24,18),(29,30));join('pole','canopy')
        path('water',(6,42), [('C',(12,38),(9,42),(9,38)),('C',(18,42),(15,38),(15,42)),('C',(24,38),(21,42),(21,38)),('C',(30,42),(27,38),(27,42)),('C',(36,38),(33,42),(33,38)),('C',(42,42),(39,38),(39,42))])

