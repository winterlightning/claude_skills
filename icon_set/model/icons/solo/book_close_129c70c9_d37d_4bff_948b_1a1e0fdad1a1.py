"""book-close: next fifty AI review; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '129c70c9-d37d-4bff-948b-1a1e0fdad1a1'
SOURCE_PATH = 'icons-json/content/book close_129c70c9-d37d-4bff-948b-1a1e0fdad1a1.json'
AUTHOR = 'gpt-6'

class BookClose(Solo48):
    icon_id = 'book-close'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'content'
    aliases = ()
    keywords = ('book', 'close', 'content', 'solo-ai-next50')

    def build(self):
        # Plan: A classic tall hardback uses a rounded lower page roll and square fore-edge. Kept a single generous page band rather than adding small decoration.
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
        path('cover',(40,4),[('L',(14,4)),('A',(8,10),6,6,False),('L',(8,38)),('A',(14,44),6,6,False),('L',(40,44)),('C',(40,34),(37,42),(37,36)),('L',(40,4))],True)
        path('pages',(8,38),[('A',(14,34),6,4,True),('L',(40,34))]);join('pages','cover')
