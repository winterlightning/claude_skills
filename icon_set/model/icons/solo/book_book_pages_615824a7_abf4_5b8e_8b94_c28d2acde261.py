"""book-book-pages: next fifty AI review; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '615824a7-abf4-5b8e-8b94-c28d2acde261'
SOURCE_PATH = 'pictographic-primitives/content/book book pages_615824a7-abf4-5b8e-8b94-c28d2acde261.svg'
AUTHOR = 'gpt-6'

class BookBookPages(Solo48):
    icon_id = 'book-book-pages'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'content'
    categories = ('primitives', 'content')
    aliases = ()
    keywords = ('book', 'pages', 'content', 'solo-ai-next50')

    def build(self):
        # Plan: A broad open book with gently arched pages. Shared left-page controls are reflected for exactly balanced page widths and a centered spine.
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
        path('spread',(24,14),[('C',(12,8),(20,10),(16,8)),('C',(4,10),(8,8),(6,9)),('L',(4,36)),('C',(12,34),(6,35),(8,34)),('C',(24,40),(16,34),(20,36)),('C',(36,34),(28,36),(32,34)),('C',(44,36),(40,34),(42,35)),('L',(44,10)),('C',(36,8),(42,9),(40,8)),('C',(24,14),(32,8),(28,10))],True)
        line('spine',(24,14),(24,40));join('spine','spread')
