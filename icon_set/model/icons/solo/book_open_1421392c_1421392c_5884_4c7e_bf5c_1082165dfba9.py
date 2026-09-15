"""book-open-1421392c: next fifty AI review; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '1421392c-5884-4c7e-bf5c-1082165dfba9'
SOURCE_PATH = 'icons-json/content/book open_1421392c-5884-4c7e-bf5c-1082165dfba9.json'
AUTHOR = 'gpt-6'

class BookOpen1421392c(Solo48):
    icon_id = 'book-open-1421392c'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'content'
    aliases = ()
    keywords = ('book', 'open', 'content', 'solo-ai-next50')

    def build(self):
        # Plan: An open volume with one leaf lifting on the left. The asymmetric turning leaf is intentional; broad empty pages retain clarity.
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
        path('spread',(24,16),[('L',(14,8)),('L',(4,12)),('L',(4,34)),('L',(14,32)),('L',(24,40)),('C',(44,34),(30,34),(38,34)),('L',(44,10)),('C',(24,16),(38,10),(30,10))],True)
        line('spine',(24,16),(24,40));line('leaf',(14,8),(14,32));join('spine','spread');join('leaf','spread')
