"""book-close-5a3d7973: next fifty AI review; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5a3d7973-ece6-5338-a408-973670de2b0b'
SOURCE_PATH = 'icons-json/content/book close_5a3d7973-ece6-5338-a408-973670de2b0b.json'
AUTHOR = 'gpt-6'

class BookClose5a3d7973(Solo48):
    icon_id = 'book-close-5a3d7973'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'content'
    aliases = ()
    keywords = ('book', 'close', 'content', 'solo-ai-next50')

    def build(self):
        # Plan: A landscape album has a curved spine and a broad lower page band. Horizontal keyshape preserves a distinct album proportion.
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
        path('cover',(44,8),[('L',(12,8)),('A',(4,16),8,8,False),('L',(4,34)),('A',(10,40),6,6,False),('L',(44,40)),('L',(44,30)),('L',(44,8))],True)
        path('pages',(4,34),[('A',(10,30),6,4,True),('L',(44,30))]);join('pages','cover')
