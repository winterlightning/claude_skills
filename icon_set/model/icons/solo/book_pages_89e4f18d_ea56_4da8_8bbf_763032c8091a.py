"""book-pages: next fifty AI review; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '89e4f18d-ea56-4da8-8bbf-763032c8091a'
SOURCE_PATH = 'icons-json/state/book pages_89e4f18d-ea56-4da8-8bbf-763032c8091a.json'
AUTHOR = 'gpt-6'

class BookPages(Solo48):
    icon_id = 'book-pages'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('book', 'pages', 'state', 'solo-ai-next50')

    def build(self):
        # Plan: A low wide book has rounded page corners and a short recessed center fold. The lower spine is squared, producing a quiet broad spread.
        # Reference: Lucide book-open original and atomic-debug construction.

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
        path('spread',(24,16),[('C',(12,8),(21,10),(17,8)),('L',(4,8)),('L',(4,32)),('A',(12,40),8,8,False),('L',(24,40)),('L',(36,40)),('A',(44,32),8,8,False),('L',(44,8)),('L',(36,8)),('C',(24,16),(31,8),(27,10))],True)
        line('spine',(24,16),(24,40));join('spine','spread')
