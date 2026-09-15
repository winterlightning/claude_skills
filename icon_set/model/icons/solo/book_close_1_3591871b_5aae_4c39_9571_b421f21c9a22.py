"""book-close-1: next fifty AI review; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3591871b-5aae-4c39-9571-b421f21c9a22'
SOURCE_PATH = 'icons-json/content/book close 1_3591871b-5aae-4c39-9571-b421f21c9a22.json'
AUTHOR = 'gpt-6'

class BookClose1(Solo48):
    icon_id = 'book-close-1'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'content'
    aliases = ()
    keywords = ('book', 'close', 'content', 'solo-ai-next50')

    def build(self):
        # Plan: A clothbound notebook has a clear vertical spine and a broad curved lower page edge. This binding differs from the left-roll hardback.
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
        path('cover',(12,4),[('L',(18,4)),('L',(36,4)),('A',(40,8),4,4,True),('L',(40,34)),('L',(40,40)),('A',(36,44),4,4,True),('L',(18,44)),('L',(12,44)),('A',(8,40),4,4,True),('L',(8,8)),('A',(12,4),4,4,True)],True)
        poly('spine',(18,4),(18,34),(18,44));join('spine','cover')
        path('page-edge',(18,34),[('C',(40,34),(26,38),(32,38))]);join('page-edge','spine');join('page-edge','cover')
