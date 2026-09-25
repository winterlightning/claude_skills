"""bowl: next fifty AI review; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '139ac791-1f3c-444f-b1a9-bb6088d099c8'
SOURCE_PATH = 'pictographic-primitives/symbol/bowl_139ac791-1f3c-444f-b1a9-bb6088d099c8.svg'
AUTHOR = 'gpt-6'

class Bowl(Solo48):
    icon_id = 'bowl'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    categories = ('symbol', 'state')
    aliases = ()
    keywords = ('bowl', 'symbol', 'solo-ai-next50')

    def build(self):
        # Plan: A plain footed bowl keeps a continuous elliptical basin and broad flat foot. One shared axis controls both sides, with no unnecessary steam or utensils.
        # Reference: Lucide soup original and atomic-debug construction.

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
        path('bowl',(4,8),[('L',(44,8)),('C',(32,32),(44,20),(38,28)),('L',(32,40)),('L',(16,40)),('L',(16,32)),('C',(4,8),(10,28),(4,20))],True)
