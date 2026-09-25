"""chess-pawn: next hundred AI review; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd4337f67-2dcc-4438-9e59-dbeedde31139'
SOURCE_PATH = 'pictographic-primitives/hobbies/chess pawn_d4337f67-2dcc-4438-9e59-dbeedde31139.svg'
AUTHOR = 'gpt-6'

class ChessPawn(Solo48):
    icon_id = 'chess-pawn'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'hobbies'
    categories = ('hobbies', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('chess', 'pawn', 'hobbies', 'solo-ai-next100')

    def build(self):
        # Plan: A pawn retains its oval head, tapered neck and broad pedestal; true ellipse geometry replaces irregular head segments.
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
        path('head',(24,4),[('A',(24,20),12,8,True),('A',(24,4),12,8,True)],True)
        poly('neck',(18,19),(14,34),(34,34),(30,19));join('neck','head')
        path('base',(14,34),[('L',(34,34)),('A',(40,40),6,6,True),('L',(40,44)),('L',(8,44)),('L',(8,40)),('A',(14,34),6,6,True)],True);join('base','neck')
