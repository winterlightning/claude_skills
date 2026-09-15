"""book-open-a147931e: next fifty AI review; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a147931e-057f-4518-b391-cf08f66084de'
SOURCE_PATH = 'pictographic-primitives/content/book open_a147931e-057f-4518-b391-cf08f66084de.svg'
AUTHOR = 'gpt-6'

class BookOpenA147931e(Solo48):
    icon_id = 'book-open-a147931e'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'content'
    aliases = ()
    keywords = ('book', 'open', 'content', 'solo-ai-next50')

    def build(self):
        # Plan: A wide open reader has two sparse text rules per page. Shared page and text parameters keep mirrored margins and eight-unit row spacing.
        # Reference: Lucide book-open-text original and atomic-debug construction.

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
        path('spread',(24,12),[('C',(4,8),(18,8),(10,8)),('L',(4,36)),('C',(24,40),(10,36),(18,36)),('C',(44,36),(30,36),(38,36)),('L',(44,8)),('C',(24,12),(38,8),(30,8))],True)
        line('spine',(24,12),(24,40));join('spine','spread')
        for side in (-1,1):
         x=lambda d:24+side*d
         for y in (20,28):line(f'text-{side}-{y}',(x(9),y),(x(11),y))
