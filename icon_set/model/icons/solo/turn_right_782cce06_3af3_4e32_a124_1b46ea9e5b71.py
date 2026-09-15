"""turn-right: Smooth directional bend; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '782cce06-3af3-4e32-a124-1b46ea9e5b71'
SOURCE_PATH = 'icons-json/transportation/turn right_782cce06-3af3-4e32-a124-1b46ea9e5b71.json'
AUTHOR = 'gpt-6'

class TurnRight(Solo48):
    icon_id = 'turn-right'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('solo-ai-full-set', 'turn-right')

    def build(self):
        # Plan: A quarter-circle bend joins straight runs; preserve direction and the longer upright stem.
        # Reference: Lucide undo-2: original and atomic-debug geometry.

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
        def pt(x,y):return (48-x,y) if True else (x,y)
        path('shaft',pt(8,12),[('L',pt(28,12)),('A',pt(40,24),12,12,False),('L',pt(40,44))])
        path('head',pt(16,4),[('L',pt(8,12)),('L',pt(16,20))]);join('shaft','head')
