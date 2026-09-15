"""book-open-e1dee87f: next fifty AI review; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e1dee87f-e9eb-5067-afed-727092c03d65'
SOURCE_PATH = 'icons-json/content/book open_e1dee87f-e9eb-5067-afed-727092c03d65.json'
AUTHOR = 'gpt-6'

class BookOpenE1dee87f(Solo48):
    icon_id = 'book-open-e1dee87f'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'content'
    aliases = ()
    keywords = ('book', 'open', 'content', 'solo-ai-next50')

    def build(self):
        # Plan: A soft open book has bowed outer edges and level inner leaves. Its flared silhouette and broad centered lower arc create a distinct flexible binding.
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
        path('spread',(24,12),[('C',(8,8),(18,8),(12,8)),('C',(4,28),(6,14),(4,22)),('L',(4,36)),('C',(24,40),(12,34),(18,36)),('C',(44,36),(30,36),(36,34)),('L',(44,28)),('C',(40,8),(44,22),(42,14)),('C',(24,12),(36,8),(30,8))],True)
        line('spine',(24,12),(24,40));join('spine','spread')
