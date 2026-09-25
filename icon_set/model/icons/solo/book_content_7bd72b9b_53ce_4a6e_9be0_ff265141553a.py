"""book-content: next fifty AI review; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7bd72b9b-53ce-4a6e-9be0-ff265141553a'
SOURCE_PATH = 'pictographic-primitives/content/book_7bd72b9b-53ce-4a6e-9be0-ff265141553a.svg'
AUTHOR = 'gpt-6'

class BookContent(Solo48):
    icon_id = 'book-content'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'content'
    categories = ('primitives', 'content')
    aliases = ()
    keywords = ('book', 'content', 'solo-ai-next50')

    def build(self):
        # Plan: An upright softcover has a concave exposed page edge at the top-right and a rounded spine. The visible notch distinguishes it from solid hard covers.
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
        path('cover',(40,4),[('L',(14,4)),('A',(8,10),6,6,False),('L',(8,38)),('A',(14,44),6,6,False),('L',(40,44)),('L',(40,16)),('C',(40,4),(36,13),(36,7))],True)
        path('pages',(8,10),[('A',(14,16),6,6,False),('L',(40,16))]);join('pages','cover')
