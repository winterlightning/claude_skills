"""cauldron: next hundred AI review; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e709f0a8-cd5c-4a9b-8b47-1734cea8a46a'
SOURCE_PATH = 'pictographic-primitives/holidays/cauldron_e709f0a8-cd5c-4a9b-8b47-1734cea8a46a.svg'
AUTHOR = 'gpt-6'

class Cauldron(Solo48):
    icon_id = 'cauldron'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'holidays'
    aliases = ()
    keywords = ('cauldron', 'holidays', 'solo-ai-next100')

    def build(self):
        # Plan: A broad round-bellied cauldron has a flared lip and paired shoulders. Preserve the source rounded cooking vessel.
        # Reference: Lucide cooking-pot original and atomic-debug construction.

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
        path('pot',(8,8),[('L',(40,8)),('A',(40,16),4,4,True),('L',(44,24)),('C',(24,40),(43,36),(35,40)),('C',(4,24),(13,40),(5,36)),('L',(8,16)),('A',(8,8),4,4,True)],True)
