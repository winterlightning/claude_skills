"""book-open: next fifty AI review; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '03b427a0-f791-44b1-9798-ea43bb973886'
SOURCE_PATH = 'icons-json/content/book open_03b427a0-f791-44b1-9798-ea43bb973886.json'
AUTHOR = 'gpt-6'

class BookOpen(Solo48):
    icon_id = 'book-open'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'content'
    aliases = ()
    keywords = ('book', 'open', 'content', 'solo-ai-next50')

    def build(self):
        # Plan: A tall rounded open volume uses a deeper central fold and matching curled upper and lower pages. Square bounds create a substantial upright spread.
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
        path('spread',(24,12),[('C',(12,6),(21,8),(17,6)),('L',(6,6)),('L',(6,36)),('L',(12,36)),('C',(24,42),(17,36),(21,38)),('C',(36,36),(27,38),(31,36)),('L',(42,36)),('L',(42,6)),('L',(36,6)),('C',(24,12),(31,6),(27,8))],True)
        line('spine',(24,12),(24,42));join('spine','spread')
