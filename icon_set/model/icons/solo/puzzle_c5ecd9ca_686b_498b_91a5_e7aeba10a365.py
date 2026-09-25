"""puzzle: Smooth puzzle piece; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c5ecd9ca-686b-498b-91a5-e7aeba10a365'
SOURCE_PATH = 'pictographic-primitives/state/puzzle_c5ecd9ca-686b-498b-91a5-e7aeba10a365.svg'
AUTHOR = 'gpt-6'

class Puzzle(Solo48):
    icon_id = 'puzzle'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('solo-ai-full-set', 'puzzle')

    def build(self):
        # Plan: Preserve all three tab and socket features with broad bridges between them.
        # Reference: Lucide puzzle: original and atomic-debug geometry.

        # Typed path helpers preserve each continuous stroke and its round joins.
        def path(name, start, commands, closed=False):
            members = []
            here = start
            for index, command in enumerate(commands):
                ident = f"{name}-{index}"
                kind, end, *args = command
                if kind == "L" and tuple(end) == tuple(here):
                    continue
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
        path('piece',(19,16),[('L',(8,16)),('L',(8,24)),('C',(14,29),(12,24),(14,25)),('C',(8,34),(14,33),(12,34)),('L',(8,44)),('L',(21,44)),('C',(26,36),(19,40),(21,36)),('C',(31,44),(31,36),(33,40)),('L',(40,44)),('L',(40,16)),('L',(29,16)),('C',(24,4),(34,9),(30,4)),('C',(19,16),(18,4),(14,9))],True)
