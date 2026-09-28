"""cup: next hundred AI review; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'db8ea339-df43-4389-a7c4-43da211daa67'
SOURCE_PATH = 'pictographic-primitives/symbol/cup_db8ea339-df43-4389-a7c4-43da211daa67.svg'
AUTHOR = 'gpt-6'

class Cup(Solo48):
    icon_id = 'cup'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    categories = ('symbol', 'state')
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
        path('cup',(4,8),[('L',(32,8)),('L',(32,16)),('L',(32,30)),('A',(22,40),10,10,True),('L',(14,40)),('A',(4,30),10,10,True),('L',(4,8))],True)
        path('handle',(32,16),[('L',(36,16)),('A',(44,24),8,8,True),('A',(36,32),8,8,True),('L',(32,32))]);join('handle','cup')
