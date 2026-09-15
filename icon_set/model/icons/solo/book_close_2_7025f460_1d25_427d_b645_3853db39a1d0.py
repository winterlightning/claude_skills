"""book-close-2: next fifty AI review; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7025f460-1d25-427d-b645-3853db39a1d0'
SOURCE_PATH = 'icons-json/content/book close 2_7025f460-1d25-427d-b645-3853db39a1d0.json'
AUTHOR = 'gpt-6'

class BookClose2(Solo48):
    icon_id = 'book-close-2'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'content'
    aliases = ()
    keywords = ('book', 'close', 'content', 'solo-ai-next50')

    def build(self):
        # Plan: A compact square journal has an upper rolled page edge and large rounded bottom corners. Its format and corner radii distinguish it from tall books.
        # Reference: Lucide book original and atomic-debug construction.

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
        path('cover',(42,6),[('L',(14,6)),('A',(6,14),8,8,False),('L',(6,30)),('A',(18,42),12,12,False),('L',(30,42)),('A',(42,30),12,12,False),('L',(42,18)),('L',(42,6))],True)
        path('pages',(6,14),[('A',(12,18),6,4,False),('L',(42,18))]);join('pages','cover')
