"""book-open-1: next fifty AI review; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '1d780c55-d1d8-4fad-9a0c-5cfd553331a0'
SOURCE_PATH = 'icons-json/content/book open 1_1d780c55-d1d8-4fad-9a0c-5cfd553331a0.json'
AUTHOR = 'gpt-6'

class BookOpen1(Solo48):
    icon_id = 'book-open-1'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'content'
    aliases = ()
    keywords = ('book', 'open', 'content', 'solo-ai-next50')

    def build(self):
        # Plan: A broad flat-topped open book has softly rounded outer corners and shallow spine transitions. Matching radii replace conversion dents.
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
        path('spread',(24,12),[('A',(20,8),4,4,False),('L',(8,8)),('A',(4,12),4,4,False),('L',(4,32)),('A',(8,36),4,4,False),('L',(16,36)),('C',(24,40),(20,36),(22,38)),('C',(32,36),(26,38),(28,36)),('L',(40,36)),('A',(44,32),4,4,False),('L',(44,12)),('A',(40,8),4,4,False),('L',(28,8)),('A',(24,12),4,4,False)],True)
        line('spine',(24,12),(24,40));join('spine','spread')
