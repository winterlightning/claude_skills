"""book-close-content: next fifty AI review; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3b4996c8-c930-4df3-8c39-a94d12e8e2d2'
SOURCE_PATH = 'pictographic-primitives/content/book close_3b4996c8-c930-4df3-8c39-a94d12e8e2d2.svg'
AUTHOR = 'gpt-6'

class BookCloseContent(Solo48):
    icon_id = 'book-close-content'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'content'
    categories = ('primitives', 'content')
    aliases = ()
    keywords = ('book', 'close', 'content', 'solo-ai-next50')

    def build(self):
        # Plan: A square bound notebook uses a straight upper page band and an offset vertical spine. Equal corner radii keep the cover clean.
        # Reference: Lucide notebook original and atomic-debug construction.

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
        path('cover',(10,6),[('L',(16,6)),('L',(38,6)),('A',(42,10),4,4,True),('L',(42,18)),('L',(42,38)),('A',(38,42),4,4,True),('L',(16,42)),('L',(10,42)),('A',(6,38),4,4,True),('L',(6,18)),('L',(6,10)),('A',(10,6),4,4,True)],True)
        line('spine',(16,6),(16,42));line('pages',(16,18),(42,18));join('spine','cover');join('pages','spine');join('pages','cover')
