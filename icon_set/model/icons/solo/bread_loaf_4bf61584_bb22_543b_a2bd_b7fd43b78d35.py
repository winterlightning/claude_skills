"""bread-loaf: next fifty AI review; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4bf61584-bb22-543b-a2bd-b7fd43b78d35'
SOURCE_PATH = 'pictographic-primitives/food/bread loaf_4bf61584-bb22-543b-a2bd-b7fd43b78d35.svg'
AUTHOR = 'gpt-6'

class BreadLoaf(Solo48):
    icon_id = 'bread-loaf'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('bread', 'loaf', 'food', 'solo-ai-next50')

    def build(self):
        # Plan: A loaf in perspective keeps a rounded crown and a single visible slice seam. The right end is deliberately shorter to show depth.
        # Reference: Lucide sandwich original and atomic-debug construction.

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
        path('loaf',(8,40),[('L',(10,22)),('C',(4,16),(6,22),(4,19)),('C',(14,8),(4,10),(8,8)),('L',(34,8)),('C',(44,16),(40,8),(44,10)),('C',(38,22),(44,19),(42,22)),('L',(40,40)),('L',(8,40))],True)
        path('slice',(26,8),[('C',(26,22),(34,10),(34,18)),('L',(30,40))]);join('slice','loaf')
