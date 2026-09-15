"""book-open-b5768591: next fifty AI review; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b5768591-30d0-458a-8f42-f8fa19890c4e'
SOURCE_PATH = 'icons-json/content/book open_b5768591-30d0-458a-8f42-f8fa19890c4e.json'
AUTHOR = 'gpt-6'

class BookOpenB5768591(Solo48):
    icon_id = 'book-open-b5768591'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'content'
    aliases = ()
    keywords = ('book', 'open', 'content', 'solo-ai-next50')

    def build(self):
        # Plan: An open book with an exposed lower page layer. The secondary contour follows the spread eight units below its principal edge; outer attachments remain exact.
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
        path('spread',(24,12),[('C',(4,8),(18,8),(10,8)),('L',(4,24)),('L',(4,32)),('C',(24,40),(12,32),(18,34)),('C',(44,32),(30,34),(36,32)),('L',(44,24)),('L',(44,8)),('C',(24,12),(38,8),(30,8))],True)
        path('page-edge',(4,24),[('C',(24,32),(12,24),(18,26)),('C',(44,24),(30,26),(36,24))]);line('spine',(24,12),(24,32));join('page-edge','spread');join('spine','spread');join('spine','page-edge')
