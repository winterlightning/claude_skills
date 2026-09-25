"""truck-style: Balanced delivery truck; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '76d08941-ee75-5b6a-94d2-97d9d4c45931'
SOURCE_PATH = 'pictographic-primitives/delivery/truck style_76d08941-ee75-5b6a-94d2-97d9d4c45931.svg'
AUTHOR = 'gpt-6'

class TruckStyle(Solo48):
    icon_id = 'truck-style'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'delivery'
    categories = ('delivery', 'primitives')
    aliases = ()
    keywords = ('solo-ai-full-set', 'truck-style')

    def build(self):
        # Plan: Preserve cargo and cab proportions with full round wheels; curve the body shoulders into the wheel junctions.
        # Reference: Lucide truck: original and atomic-debug geometry.

        # Typed path helpers preserve each continuous stroke and its round joins.
        def path(name, start, commands, closed=False):
            members = []
            here = start
            for index, command in enumerate(commands):
                ident = f"{name}-{index}"
                kind, end, *args = command
                if kind == "L" and tuple(end) == tuple(here):
                    continue
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
        rear=11;front=37;r=5
        path('body',(4,8),[('L',(24,8)),('L',(24,18)),('L',(35,16)),('L',(44,22)),('C',(front+r,35),(44,30),(front+r,32)),('A',(front-r,35),r,r,True),('L',(24,35)),('L',(rear+r,35)),('A',(rear-r,35),r,r,True),('C',(4,24),(rear-r,31),(4,29)),('L',(4,8))],True)
        for name,cx in [('rear',rear),('front',front)]:path(name,(cx-r,35),[('A',(cx+r,35),r,r,True)]);join(name,'body')
        line('cargo',(24,18),(24,35));join('cargo','body')
