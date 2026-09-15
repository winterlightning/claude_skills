"""book-open-1-6ed65acc: next fifty AI review; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6ed65acc-f765-4c0b-9081-3fbba85d281c'
SOURCE_PATH = 'icons-json/content/book open 1_6ed65acc-f765-4c0b-9081-3fbba85d281c.json'
AUTHOR = 'gpt-6'

class BookOpen16ed65acc(Solo48):
    icon_id = 'book-open-1-6ed65acc'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'content'
    aliases = ()
    keywords = ('book', 'open', 'content', 'solo-ai-next50')

    def build(self):
        # Plan: A narrow pocket-sized open book has tall leaves and a shallow curved fold. Vertical proportions distinguish it from wide spreads.
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
        path('spread',(24,10),[('C',(8,4),(20,4),(14,4)),('L',(8,38)),('C',(24,44),(14,38),(20,38)),('C',(40,38),(28,38),(34,38)),('L',(40,4)),('C',(24,10),(34,4),(28,4))],True)
        line('spine',(24,10),(24,44));join('spine','spread')
