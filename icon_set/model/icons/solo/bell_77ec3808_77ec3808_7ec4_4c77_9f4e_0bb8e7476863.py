"""bell-77ec3808: AI stroke review; parent retained for comparison."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '77ec3808-7ec4-4c77-9f4e-0bb8e7476863'
SOURCE_PATH = 'pictographic-primitives/symbol/bell_77ec3808-7ec4-4c77-9f4e-0bb8e7476863.svg'
AUTHOR = 'gpt-6'

class Bell77ec3808(Solo48):
    icon_id = 'bell-77ec3808'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    categories = ('symbol', 'state')
    aliases = ()
    keywords = ('bell', 'symbol', 'solo-ai-first50')

    def build(self):
        # Plan: A symmetric bell shoulder flows into a gently flared skirt; retained the uncluttered silhouette without adding a clapper.
        # Reference: Lucide original/bell.svg and atomic-debug/bell.svg.

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
        path('bell',(4,40), [('C',(12,24),(10,34),(12,31)),('L',(12,20)),('A',(36,20),12,12,True),('L',(36,24)),('C',(44,40),(36,31),(38,34)),('L',(4,40))],True)

