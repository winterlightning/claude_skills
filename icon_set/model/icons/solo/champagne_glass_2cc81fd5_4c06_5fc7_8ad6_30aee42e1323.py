"""champagne-glass: next hundred AI review; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '2cc81fd5-4c06-5fc7-8ad6-30aee42e1323'
SOURCE_PATH = 'icons-json/drinks/champagne glass_2cc81fd5-4c06-5fc7-8ad6-30aee42e1323.json'
AUTHOR = 'gpt-6'

class ChampagneGlass(Solo48):
    icon_id = 'champagne-glass'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'drinks'
    aliases = ()
    keywords = ('champagne', 'glass', 'drinks', 'solo-ai-next100')

    def build(self):
        # Plan: Keep the generous angular bowl and long central stem; mirrored bowl walls smooth into the stem junction.
        # Reference: Lucide wine original and atomic-debug construction.

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
        path('bowl',(12,4),[('L',(36,4)),('L',(40,18)),('C',(24,28),(40,25),(29,26)),('C',(8,18),(19,26),(8,25)),('L',(12,4))],True)
        line('stem',(24,28),(24,44));line('foot',(12,44),(36,44));join('stem','bowl');join('stem','foot')
