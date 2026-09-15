"""diamond-money: next hundred AI review; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5d9db826-3f1d-489d-b7b6-bf5b50bbe949'
SOURCE_PATH = 'icons-json/money/diamond_5d9db826-3f1d-489d-b7b6-bf5b50bbe949.json'
AUTHOR = 'gpt-6'

class Diamond(Solo48):
    icon_id = 'diamond-money'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    aliases = ()
    keywords = ('diamond', 'money', 'solo-ai-next100')

    def build(self):
        # Plan: Keep the faceted diamond with a wide shoulder and centered bottom point. Paired facets retain symmetry and clear openings.
        # Reference: Lucide gem original and atomic-debug construction.

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
        poly('gem',(14,8),(34,8),(44,22),(24,40),(4,22),closed=True)
        poly('across',(4,22),(18,22),(30,22),(44,22));poly('facets',(14,8),(18,22),(24,40),(30,22),(34,8));join('across','gem');join('facets','gem');join('across','facets')
