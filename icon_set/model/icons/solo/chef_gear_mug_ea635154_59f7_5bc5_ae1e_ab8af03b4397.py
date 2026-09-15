"""chef-gear-mug: next hundred AI review; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ea635154-59f7-5bc5-ae1e-ab8af03b4397'
SOURCE_PATH = 'icons-json/drinks/chef gear mug_ea635154-59f7-5bc5-ae1e-ab8af03b4397.json'
AUTHOR = 'gpt-6'

class ChefGearMug(Solo48):
    icon_id = 'chef-gear-mug'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'drinks'
    aliases = ()
    keywords = ('chef', 'gear', 'mug', 'drinks', 'solo-ai-next100')

    def build(self):
        # Plan: Keep the upright mug with a broad handle and lightly rounded base. Its taller cup body distinguishes it from the low cups.
        # Reference: Lucide coffee original and atomic-debug construction.

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
        path('cup',(6,6),[('L',(30,6)),('L',(30,14)),('L',(30,28)),('L',(30,34)),('A',(22,42),8,8,True),('L',(14,42)),('A',(6,34),8,8,True),('L',(6,6))],True)
        path('handle',(30,14),[('L',(35,14)),('A',(42,21),7,7,True),('A',(35,28),7,7,True),('L',(30,28))]);join('handle','cup')
