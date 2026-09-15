"""console-drawers: next hundred AI review; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0dfae6c3-d260-4699-b330-9a726dacbd9a'
SOURCE_PATH = 'pictographic-primitives/furnitures/console drawers_0dfae6c3-d260-4699-b330-9a726dacbd9a.svg'
AUTHOR = 'gpt-6'

class ConsoleDrawers(Solo48):
    icon_id = 'console-drawers'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'furnitures'
    aliases = ()
    keywords = ('console', 'drawers', 'furnitures', 'solo-ai-next100')

    def build(self):
        # Plan: Keep the low console with open left bay and two right drawers. Repeated grid positions keep shelf spacing even.
        # Reference: No useful exact Lucide match; supplied original silhouette.

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
        poly('cabinet',(4,8),(44,8),(44,34),(4,34),(4,8));line('partition',(24,8),(24,34));line('shelf',(24,21),(44,21));join('partition','cabinet');join('shelf','partition');join('shelf','cabinet')
        for x in (8,40):line(f'leg-{x}',(x,34),(x,40));join(f'leg-{x}','cabinet')
