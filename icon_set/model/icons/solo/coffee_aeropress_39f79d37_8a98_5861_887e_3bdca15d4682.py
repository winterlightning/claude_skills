"""coffee-aeropress: next hundred AI review; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '39f79d37-8a98-5861-887e-3bdca15d4682'
SOURCE_PATH = 'icons-json/drinks/coffee aeropress_39f79d37-8a98-5861-887e-3bdca15d4682.json'
AUTHOR = 'gpt-6'

class CoffeeAeropress(Solo48):
    icon_id = 'coffee-aeropress'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'drinks'
    aliases = ()
    keywords = ('coffee', 'aeropress', 'drinks', 'solo-ai-next100')

    def build(self):
        # Plan: Preserve the press plunger, straight chamber and flared lower filter stand. Shared vertical walls and wide bands keep the mechanism readable.
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
        line('top',(12,4),(36,4));poly('chamber',(16,4),(16,24),(16,34),(8,40),(12,44),(36,44),(40,40),(32,34),(32,24),(32,4));join('top','chamber')
        line('band',(8,24),(40,24));line('base-band',(16,34),(32,34));join('band','chamber');join('base-band','chamber')
