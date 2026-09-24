"""cup-1: next hundred AI review; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f748c868-065c-4348-8b9f-0e60c63d3e9f'
SOURCE_PATH = 'pictographic-primitives/symbol/cup 1_f748c868-065c-4348-8b9f-0e60c63d3e9f.svg'
AUTHOR = 'gpt-6'

class Cup1(Solo48):
    icon_id = 'cup-1'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('cup', 'symbol', 'solo-ai-next100')

    def build(self):
        # Plan: Keep the source cup bowl and a full-size handle opening. Rounded base corners and handle radii are coherent; cup depth and handle profile distinguish this version.
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
        path('cup',(4,8),[('L',(32,8)),('L',(32,16)),('L',(32,30)),('C',(20,40),(32,38),(26,40)),('L',(16,40)),('C',(4,30),(8,40),(4,37)),('L',(4,8))],True)
        poly('handle',(32,16),(40,16),(44,22),(44,28),(40,32),(32,32));join('handle','cup')
