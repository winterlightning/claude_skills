"""cocktail: next hundred AI review; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4e9eff0a-91b1-4736-8893-c4364a52e7a0'
SOURCE_PATH = 'pictographic-primitives/symbol/cocktail_4e9eff0a-91b1-4736-8893-c4364a52e7a0.svg'
AUTHOR = 'gpt-6'

class Cocktail(Solo48):
    icon_id = 'cocktail'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    categories = ('symbol', 'state')
    aliases = ()
    keywords = ('cocktail', 'symbol', 'solo-ai-next100')

    def build(self):
        # Plan: Keep the rounded cocktail bowl, central stem and angled straw, with a wider opening and clean shared lip contact.
        # Reference: Lucide martini original and atomic-debug construction.

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
        path('bowl',(8,16),[('L',(31,16)),('L',(40,16)),('A',(24,32),16,16,True),('A',(8,16),16,16,True)],True)
        poly('straw',(24,24),(31,16),(35,6),(40,4));join('straw','bowl')
        line('stem',(24,32),(24,44));line('foot',(16,44),(32,44));join('stem','bowl');join('stem','foot')
