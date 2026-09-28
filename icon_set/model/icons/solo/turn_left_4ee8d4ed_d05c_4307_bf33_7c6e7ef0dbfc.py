"""turn-left: Smooth directional bend; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4ee8d4ed-d05c-4307-bf33-7c6e7ef0dbfc'
SOURCE_PATH = 'pictographic-primitives/transportation/turn left_4ee8d4ed-d05c-4307-bf33-7c6e7ef0dbfc.svg'
AUTHOR = 'gpt-6'

class TurnLeft(Solo48):
    icon_id = 'turn-left'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    categories = ('transportation', 'primitives')
    aliases = ()
    keywords = ('solo-ai-full-set', 'turn-left')

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
        def pt(x,y):return (48-x,y) if False else (x,y)
        path('shaft',pt(8,12),[('L',pt(28,12)),('A',pt(40,24),12,12,True),('L',pt(40,44))])
        path('head',pt(16,4),[('L',pt(8,12)),('L',pt(16,20))]);join('shaft','head')
