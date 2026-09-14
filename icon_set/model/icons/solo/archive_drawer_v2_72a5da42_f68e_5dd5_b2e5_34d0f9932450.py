"""archive-drawer: AI stroke review; parent retained for comparison."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '72a5da42-f68e-5dd5-b2e5-34d0f9932450'
SOURCE_PATH = 'icons-json/content/archive drawer_72a5da42-f68e-5dd5-b2e5-34d0f9932450.json'
AUTHOR = 'gpt-6'

class ArchiveDrawerVariant2(Solo48):
    icon_id = 'archive-drawer-v2'
    variant_of = 'archive-drawer'
    variant_label = 'AI stroke review · first 50'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'content'
    aliases = ()
    keywords = ('archive', 'drawer', 'content', 'solo-ai-first50')

    def build(self):
        # Plan: One storage drawer with a raised back and a central handle cut into its front edge. Rounded outer corners replace the traced polygon.
        # Reference: Lucide original/archive.svg and atomic-debug/archive.svg.

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
        poly('back',(8,24),(8,8),(40,8),(40,24))
        path('front',(8,24), [('L',(18,24)),('L',(18,32)),('L',(30,32)),('L',(30,24)),('L',(40,24)),('A',(44,28),4,4,True),('L',(44,36)),('A',(40,40),4,4,True),('L',(8,40)),('A',(4,36),4,4,True),('L',(4,28)),('A',(8,24),4,4,True)],True)
        join('back','front')

